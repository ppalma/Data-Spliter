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


p = Picker()


config = ConfigParser.ConfigParser()
config.read('ds.cfg')

ADDR = config.get('FTP', 'address')
USER = config.get('FTP', 'user')
PASSWD = config.get('FTP', 'passwd')

def DestroyFunction(obj):
        gtk.main_quit()  

def FromDaySelected(cal):
	year, month, day = cal.get_date()
	p.SetFromDate(year, month+1 ,day,0,00,0)
	print p.fromDate
def ConnectClicked(widget,data=None):
	print "%s" % (("Desconnecting", "Try to connect")[widget.get_active()])
	
	if widget.get_active():
		p.Connect(ADDR,USER,PASSWD)
	else:
		p.Disconnect()
#	if widget.get_active():
#		ftp = FTP("192.168.0.103", "user", "coy")
#		ftp.cwd('/home/user/Descargas')
#		ftp.retrlines('LIST')	
		
#		print ftp.nlst("*g");

#		filelist = ftp.nlst("*g")
		
#		for hostfile in filelist:
#			lines = []
#			ftp.retrlines("RETR "+hostfile, lines.append)
#			pcfile = open("%s/%s"% ('./',hostfile), 'w')
#			for line in lines:
#                        	pcfile.write(line+"\n")
#	                pcfile.close()
#			print ("Done : %s")%hostfile
#		print "Connected"
#		widget.set_label("Connected")
#	else:
	#	ftp.quit()
#		widget.set_label("Disconected")

	

widgetTree = gtk.glade.XML("ds.glade")
dic = { 
	"FromDaySelected" : FromDaySelected,
	"ConnectClicked" : ConnectClicked,
	"on_window1_destroy" : DestroyFunction
}	
widgetTree.signal_autoconnect (dic)   
gtk.main()
