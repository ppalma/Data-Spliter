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
import sys

CONFIG_FILE = '/usr/src/git/dataSplitter/ds.cfg'
def quit(widget):
	gtk.main_quit()  
	sys.exit(0)

def read_config():
	vbox = wTree.get_widget('vbox')
	vbox.show()
	
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
	btnSave.show()
	btnRefresh.show()
	hbox = gtk.HBox(True,0)
	hbox.show()
	hbox.pack_start(btnSave,True,True,0)			
	hbox.pack_start(btnRefresh,True,True,0)			
	vbox.pack_start(hbox, True, True, 0)

def on_notebook_switch_page(notebook, page, page_num):

	if page_num == 2:
		config.read(CONFIG_FILE)
		read_config()		

wTree = gtk.glade.XML("ds.glade")
config = ConfigParser.ConfigParser()

dic = 	{ 
	'on_mainWindow_destroy' : quit,
	'on_notebook_switch_page':on_notebook_switch_page,
	}
		
wTree.signal_autoconnect( dic )
gtk.main()
