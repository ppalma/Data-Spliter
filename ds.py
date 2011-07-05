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




CONFIG_FILE = '/usr/src/git/dataSplitter/ds.cfg'
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

def on_notebook_switch_page(notebook, page, page_num):

	if page_num == 1:
		entryStartTime.set_text(strftime("%Y%m%d%H%M%S", gmtime()))
		comboboxDataFormat = wTree.get_widget('comboboxDataFormat')
		comboboxOutputFormat = wTree.get_widget('comboboxOutputFormat')
		comboboxDataFormat.set_active(0)
		comboboxOutputFormat.set_active(0)

	if page_num == 2:
		config.read(CONFIG_FILE)
		read_config()		

def on_checkbuttonLogFile_toggled(widget):
	widget.set_label(("Disabled", "Enabled")[widget.get_active()])	

#print "%s"%(('Enable','Disable')[widget.toggled()])
def on_buttonExecute_clicked(widget):
			
	entryStartTime = wTree.get_widget('entryStartTime')
	spinbuttonDuration = wTree.get_widget('spinbuttonDuration')
	comboboxDataFormat = wTree.get_widget('comboboxDataFormat')
	entryLocalDir = wTree.get_widget('entryLocalDir')
	
	checkbuttonLogFile = wTree.get_widget('checkbuttonLogFile')
	
	entryInputMethod = wTree.get_widget('entryInputMethod')
	entryTrigFile = wTree.get_widget('entryTrigFile')
	entryWaveServer = wTree.get_widget('entryWaveServer')
	entryOutDir = wTree.get_widget('entryOutDir')
	entrySaveSCNL = wTree.get_widget('entrySaveSCNL')

	spinbuttonMaxTraces = wTree.get_widget('spinbuttonMaxTraces')
	spinbuttonTraceBufferLen = wTree.get_widget('spinbuttonTraceBufferLen')
	spinbuttonGapThresh = wTree.get_widget('spinbuttonGapThresh')
	spinbuttonMinDuration = wTree.get_widget('spinbuttonMinDuration')
	spinbuttonTimeoutSeconds = wTree.get_widget('spinbuttonTimeoutSeconds')

	comboboxOutputFormat = wTree.get_widget('comboboxOutputFormat')

	output = 'waveman2disk.d'
	file = open(output,'w')
	
	file.write('StartTime %s\n'%entryStartTime.get_text())
	file.write('Duration %d\n'% spinbuttonDuration.get_value() )
	file.write('DataFormat %s\n'% comboboxDataFormat.get_active_text())
	
	
	file.write('LogFile %s\n'% ('1', '0')[not checkbuttonLogFile.get_active()] )
	file.write('InputMethod %s\n'% entryInputMethod.get_text() )
	file.write('SaveSCNL %s\n'% entrySaveSCNL.get_text())
	file.write('OutDir %s\n'% entryOutDir.get_text())
	file.write('OutputFormat %s\n'% comboboxOutputFormat.get_active_text())
	file.write('WaveServer %s\n'%entryWaveServer.get_text() )
	file.write('TimeoutSeconds %d\n'% spinbuttonTimeoutSeconds.get_value())
	file.write('MaxTraces %d\n'%spinbuttonMaxTraces.get_value() )
	file.write('TraceBufferLen %d\n'%spinbuttonTraceBufferLen.get_value())
	file.write('GapThresh %s\n'%spinbuttonGapThresh.get_value())
	file.write('MinDuration %d\n'%spinbuttonMinDuration.get_value())
	file.close()
	os.system('scp waveman2disk.d user@172.16.5.51:/usr/local/Earthworm/Run_OVC/Params')
	
	config.read(CONFIG_FILE)
	s = socket(AF_INET, SOCK_STREAM) 
	s.connect((config.get('WAVEMAN2DISK','server'), int(config.get('WAVEMAN2DISK','port'))))
	s.send('waveman2disk')
	data = s.recv(1024)
	print '(%s)'%data
wTree = gtk.glade.XML("ds.glade")
config = ConfigParser.ConfigParser()

dic = 	{ 
	'on_mainWindow_destroy' : quit,
	'on_notebook_switch_page':on_notebook_switch_page,
	'on_buttonExecute_clicked':on_buttonExecute_clicked,
	'on_checkbuttonLogFile_toggled':on_checkbuttonLogFile_toggled,
	}
		
entryStartTime = wTree.get_widget('entryStartTime')
spinbuttonDuration = wTree.get_widget('spinbuttonDuration')
comboboxDataFormat = wTree.get_widget('comboboxDataFormat')
entryLocalDir = wTree.get_widget('entryLocalDir')
 #= wTree.get_widget('')



wTree.signal_autoconnect( dic )
gtk.main()
