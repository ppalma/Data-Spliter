#!/usr/bin/python

#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
# Copyright:    
#----------------------------------------------------------------------------

import gtk
import gtk.glade
import gnome.ui
from Picker import Picker
import ConfigParser
import sys

def quit(widget):
	gtk.main_quit()  
	sys.exit(0)

wTree = gtk.glade.XML("ds.glade")
dic = 	{ 
	'on_mainWindow_destroy' : quit,
	}
		
wTree.signal_autoconnect( dic )
gtk.main()
