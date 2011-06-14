#!/usr/bin/python
# original file at http://sjbrown.geeky.net/metagame-sector/hw.py
# modified for gnome-python 1.99.16 by Jason Moiron
# http://nondeus.org


# import necessary modules (changed from libglade to gtk.glade)
import gtk
import gtk.glade
import gnome.ui

# this function is called when the window gets destroyed
def DestroyFunction(obj):
	gtk.main_quit() 		

widgetTree = gtk.glade.XML("project1.glade")	
					

dic = { "on_window1_destroy" : DestroyFunction }	#dler to function
					

widgetTree.signal_autoconnect (dic)			#rs defined in


gtk.main()

