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

def on_calendarFrom_day_selected(cal):
	year, month, day = cal.get_date()
	p.SetFromDate(
		year,
		month+1,
		day,
		p.fromDate.hour  ,
		p.fromDate.minute,
		p.fromDate.second
	)
def on_calendarTo_day_selected(cal):
	year, month, day = cal.get_date()
        p.SetToDate(
                year,
                month+1,
                day,
                p.fromDate.hour  ,
                p.fromDate.minute,
                p.fromDate.second
        )
	
def on_spinbuttonFromTimeh_value_changed(spin): 
	p.SetFromDate(
		p.fromDate.year,
		p.fromDate.month,
		p.fromDate.day,
		spin.get_value(),
		p.fromDate.minute,
		p.fromDate.second
	)
	spinbuttonToTimeh.set_range(spin.get_value(),23)
def on_spinbuttonFromTimem_value_changed(spin):
	p.SetFromDate(
		p.fromDate.year,
		p.fromDate.month,
		p.fromDate.day,
		p.fromDate.hour,
		spin.get_value(),
		p.fromDate.second
	)
	spinbuttonToTimem.set_range(spin.get_value(),59)
def on_spinbuttonToTimeh_value_changed(spin): 
	p.SetToDate(
	p.toDate.year,
	p.toDate.month,
	p.toDate.day,
	spin.get_value(),
	p.toDate.minute,
	p.toDate.second
	)

def on_spinbuttonToTimem_value_changed(spin):
	p.SetToDate(
	p.toDate.year,
	p.toDate.month,
	p.toDate.day,
	p.toDate.hour,
	spin.get_value(),
	p.toDate.second
	)


widgetTree = gtk.glade.XML("ds.glade")
dic = { 
	"ConnectClicked" : ConnectClicked,
	"on_window1_destroy" : DestroyFunction,

	"on_calendarFrom_day_selected" : on_calendarFrom_day_selected,
	"on_spinbuttonFromTimeh_value_changed" : on_spinbuttonFromTimeh_value_changed,
	"on_spinbuttonFromTimem_value_changed" : on_spinbuttonFromTimem_value_changed,

	"on_calendarTo_day_selected" : on_calendarTo_day_selected,
	"on_spinbuttonToTimeh_value_changed" : on_spinbuttonToTimeh_value_changed,
	"on_spinbuttonToTimem_value_changed" : on_spinbuttonToTimem_value_changed,
##	"":,
}	
spinbuttonToTimeh = widgetTree.get_widget('spinbuttonToTimeh')
spinbuttonToTimem = widgetTree.get_widget('spinbuttonToTimem')
widgetTree.signal_autoconnect (dic)   
gtk.main()
