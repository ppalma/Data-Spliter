#!/usr/bin/python

#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
# Copyright:    
#----------------------------------------------------------------------------

import gtk
import pygtk
import gtk.glade
import gnome.ui
from Picker import Picker
import ConfigParser
import sys,os
from time import gmtime, strftime
from socket import *
import time,datetime


BASE_PATH = '/opt/Data-Spliter'
CONFIG_FILE = '%s/ds.cfg'%BASE_PATH
GLADE_FILE = '%s/ds.glade'%BASE_PATH
locations = {}


def quit(widget):
	gtk.main_quit()  
	sys.exit(0)

def on_btnRefresh_clicked(widget):

	config.read(CONFIG_FILE)
	for w in  widget.get_parent().get_parent().get_children():
		if type(w) is gtk.VBox:
			for child in w.get_children():
				if type(child) is gtk.Label:
					section = child.get_text()
				if type(child) is gtk.HBox:
					for entry in  child.get_children():
						if type(entry) is gtk.Entry:
							entry.set_text(config.get(section,entry.get_name()))
def on_btnSave_clicked(widget):

	for w in  widget.get_parent().get_parent().get_children():
		if type(w) is gtk.VBox:
			for child in w.get_children():
				if type(child) is gtk.Label:
					section = child.get_text()
					if not config.has_section(section):
						config.add_section(section) 
				if type(child) is gtk.HBox:
					for entry in  child.get_children():
						if type(entry) is gtk.Entry:
							config.set(section,entry.get_name(),entry.get_text())
	with open(CONFIG_FILE, 'wb') as configfile:
    		config.write(configfile)	


def read_config():
	vbox = wTree.get_widget('vbox')
	vbox.show()
	if not vbox.get_children():
		for sec in config.sections():
			secVbox = gtk.VBox(False,0)		
			label = gtk.Label()
			hsep = gtk.HSeparator()
		
			label.set_text(sec)
		
			label.show()
			hsep.show()	
			secVbox.show()

			secVbox.pack_start(label,True,True,0)
			
			for item in config.items(sec):
				hbox = gtk.HBox(True,0)
				hbox.show()
				itemLabel = gtk.Label()
				entry = gtk.Entry()
				entry.set_text(item[1])
				entry.set_name(item[0])
				itemLabel.set_text(item[0])
				itemLabel.show()
				entry.show()	
				hbox.pack_start(itemLabel,True,True,0)
				hbox.pack_start(entry,True,True,0)
				secVbox.pack_start(hbox,True,True,0)
			
			vbox.pack_start(secVbox, True, True, 0)
			vbox.pack_start(hsep, True, True, 0)
		btnSave = gtk.Button(stock=gtk.STOCK_SAVE)
		btnRefresh = gtk.Button(stock=gtk.STOCK_REFRESH)
		btnRefresh.connect('clicked',on_btnRefresh_clicked)
		btnSave.connect('clicked',on_btnSave_clicked)
		btnSave.show()
		btnRefresh.show()
		hbox = gtk.HBox(False,0)
		hbox.show()
		hbox.pack_end(btnSave,False,False,0)			
		hbox.pack_end(btnRefresh,False,False,0)			
		vbox.pack_start(hbox, False, False, 0)

def waveman2disk_init():
	config.read(CONFIG_FILE)
        cmd = 'scp %s@%s:/usr/local/Earthworm/Run_OVC/Params/wave_serverV.d .'%(
                                config.get('WAVEMAN2DISK','user'),
                                config.get('WAVEMAN2DISK','server'))
	os.system(cmd)	
	f = open('./wave_serverV.d','r')
	for line in f:
		sline = line.split(' ')
		if sline[0] == 'Tank':
			location = sline[5]
			station = sline[1][0:-1]
			comp = sline[1][-1]
			
			if not locations.has_key(location):
				locations[location] = {station:[comp]}	
			else:
				if not locations[location].has_key(station):
					locations[location].update( {station:[comp]} )
				else:	
					locations[location][station].append(comp)
	f.close()
	os.system('rm -f ./wave_serverV.d')
	wTree.get_widget('dateeditFrom').set_time( 0 )
	wTree.get_widget('dateeditTo').set_time( 0 )
	wTree.get_widget('comboboxDataFormat').set_active( 0 )
	wTree.get_widget('comboboxOutputFormat').set_active( 0 )
	
	table =  wTree.get_widget('tableLocation')
	#tree = gtk.TreeView()
	tree =  wTree.get_widget('treeviewLocations')

	tree.get_selection().set_mode(gtk.SELECTION_MULTIPLE)



	languages = gtk.TreeViewColumn()
	languages.set_title("Locations")

        cell = gtk.CellRendererText()
        languages.pack_start(cell, True)
        languages.add_attribute(cell, "text", 0)

        treestore = gtk.TreeStore(str)

	for k in locations:
        	treestore.append(None, [sname[k]])

        tree.append_column(languages)
        tree.set_model(treestore)
#	table.attach(tree,0,1,1,2)
	table.show_all()	
def on_treeviewLocations_select_cursor_row(widget):
	print 'asdf'

def on_treeviewLocations_row_activated(widget,index,column):
	print 'on_treeviewLocations_row_activated (double click)'

def on_treeviewLocations_columns_changed(widget):
	print'on_treeviewLocations_columns_changed'
def on_treeviewLocations_cursor_changed(widget):
	#print 'on_treeviewLocations_cursor_changed'
	
	selection = widget.get_selection()
    	model, selected = selection.get_selected_rows()
    	iters = [model.get_iter(path) for path in selected]
    	
	vbox = wTree.get_widget('vboxStations')
	
	for ch in vbox.get_children():
		vbox.remove(ch)					

	for iter in iters:
		for name,alias in sname.iteritems():	
			if alias == model.get_value(iter,0):
				for stations in locations[name]:
					hbox = gtk.HBox()
					hbox.pack_start(gtk.Label(stations))
					#for com in locations[name][stations]:
					for com in ['E','N','Z']:
						cb = gtk.CheckButton(com)
						try:
							locations[name][stations].index(com)
							cb.set_active(True)
						except:
							cb.set_active(False)
						cb.connect(
							"toggled", 
							on_checkbutton_toggled, 
							(name ,stations ,com )
							)
						hbox.pack_end(cb, True,True,1)
					vbox.pack_end(hbox,True,True,2)
	vbox.show_all()
	
def on_checkbutton_toggled(widget, data=None):
	#data = (location,station,component)
	if widget.get_active():
		locations[data[0]][data[1]].append(data[2])
	else:
		locations[data[0]][data[1]].remove(data[2])
		
def on_treeviewLocations_select_all(widget):
	print 'on_treeviewLocations_select_all'
def on_notebook_switch_page(notebook, page, page_num):

	config.read(CONFIG_FILE)
	if page_num == 1:
		waveman2disk_init()
	if page_num == 2:
		read_config()		

def on_checkbuttonLogFile_toggled(widget):
	widget.set_label(("Disabled", "Enabled")[widget.get_active()])	


def get_SCNL():
	ret = []
	for name in locations:
		for station in locations[name]:
			for comp in locations[name][station]:
				#print "%s %s %s"%(name,station,comp)	
				ret.append("%s%s %s%s %s %s"%(station,comp,'BH',comp,'CY',name))
	return ret
def on_buttonExecute_clicked(widget):
			
	comboboxDataFormat = wTree.get_widget('comboboxDataFormat')
#	entryLocalDir = wTree.get_widget('entryLocalDir')
	filechooserbuttonLocalDir = wTree.get_widget('filechooserbuttonLocalDir')
	checkbuttonLogFile = wTree.get_widget('checkbuttonLogFile')
	
	entryInputMethod = wTree.get_widget('entryInputMethod')
	entryTrigFile = wTree.get_widget('entryTrigFile')
	entryWaveServer = wTree.get_widget('entryWaveServer')
	entryOutDir = wTree.get_widget('entryOutDir')

	spinbuttonMaxTraces = wTree.get_widget('spinbuttonMaxTraces')
	spinbuttonTraceBufferLen = wTree.get_widget('spinbuttonTraceBufferLen')
	spinbuttonGapThresh = wTree.get_widget('spinbuttonGapThresh')
	spinbuttonMinDuration = wTree.get_widget('spinbuttonMinDuration')
	spinbuttonTimeoutSeconds = wTree.get_widget('spinbuttonTimeoutSeconds')

	comboboxOutputFormat = wTree.get_widget('comboboxOutputFormat')
	
	fromDate = wTree.get_widget('dateeditFrom')
	toDate = wTree.get_widget('dateeditTo')

	output = 'waveman2disk2.d'
	file = open(output,'w')

	file.write('StartTime %s\n'%strftime("%Y%m%d%H%M%S", time.localtime(fromDate.get_time())) )
	file.write('Duration %d\n'% abs(fromDate.get_time() - toDate.get_time()) )
	file.write('DataFormat %s\n'% comboboxDataFormat.get_active_text())
	file.write('LogFile %s\n'% ('1', '0')[not checkbuttonLogFile.get_active()] )
	file.write('InputMethod %s\n'% entryInputMethod.get_text() )
	file.write('OutDir %s\n'% entryOutDir.get_text())
	file.write('OutputFormat %s\n'% comboboxOutputFormat.get_active_text())
	file.write('WaveServer %s\n'%entryWaveServer.get_text() )
	file.write('TimeoutSeconds %d\n'% spinbuttonTimeoutSeconds.get_value())
	file.write('MaxTraces %d\n'%spinbuttonMaxTraces.get_value() )
	file.write('TraceBufferLen %d\n'%spinbuttonTraceBufferLen.get_value())
	file.write('GapThresh %s\n'%spinbuttonGapThresh.get_value())
	file.write('MinDuration %d\n'%spinbuttonMinDuration.get_value())
	for scnl in get_SCNL():
		file.write('SaveSCNL %s\n'% scnl)
	file.close()

	
	config.read(CONFIG_FILE)
	cmd = 'scp waveman2disk2.d %s@%s:/usr/local/Earthworm/Run_OVC/Params'%(
                                config.get('WAVEMAN2DISK','user'),
                                config.get('WAVEMAN2DISK','server'))

	os.system(cmd)
	s = socket(AF_INET, SOCK_STREAM) 
	s.connect((config.get('WAVEMAN2DISK','server'), int(config.get('WAVEMAN2DISK','port'))))
	s.send('waveman2disk2')
	data = s.recv(1024)
	print '(%s)'%data

	date = strftime("%Y%m%d%H%M%S", time.localtime(fromDate.get_time())) 
	remoteFolder = "%s/%s/%s_%s_MAN"%(entryOutDir.get_text(),
	date[:6],
	date[:8],
	date[8:14],
	)
	
	time.sleep(5)	
	cmd = 'scp -r %s@%s:%s %s'%(
	config.get('WAVEMAN2DISK','user'),config.get('WAVEMAN2DISK','server'),	
	remoteFolder,filechooserbuttonLocalDir.get_current_folder())
	print cmd
	os.system(cmd)

wTree = gtk.glade.XML(GLADE_FILE)
config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)
print GLADE_FILE,CONFIG_FILE

sname = {}
for item in config.items('STATIONS'):
	sname.update({item[0].upper():item[1]})

dic = 	{ 
	'on_mainWindow_destroy' : quit,
	'on_notebook_switch_page':on_notebook_switch_page,
	'on_buttonExecute_clicked':on_buttonExecute_clicked,
	'on_checkbuttonLogFile_toggled':on_checkbuttonLogFile_toggled,
	'on_treeviewLocations_cursor_changed':on_treeviewLocations_cursor_changed,
	}
		
wTree.signal_autoconnect( dic )
gtk.main()
