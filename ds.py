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
FOLDER = config.get('FTP', 'folder')
def DestroyFunction(obj):
        gtk.main_quit()  

def ConnectClicked(widget,data=None):
	print "%s" % (("Desconnecting", "Try to connect")[widget.get_active()])
	
	if widget.get_active():
		p.Connect(ADDR,USER,PASSWD,FOLDER)
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

def on_notebook1_change_current_page(nbook,offset):
	print offset


def on_buttonSetupRefresh_clicked(btn):
	config.read('ds.cfg')

	entryFtpAddr.set_text(config.get('FTP', 'address'))
	entryFtpUser.set_text(config.get('FTP', 'user'))
	entryFtpPwd.set_text(config.get('FTP', 'passwd'))
	entryFtpFolder.set_text(config.get('FTP', 'folder'))
	filechooserbutton.set_filename((config.get('FOLDER', 'output')))
	ADDR = config.get('FTP', 'address')
	USER = config.get('FTP', 'user')
	PASSWD = config.get('FTP', 'passwd')
	FOLDER = config.get('FTP', 'folder')

def on_filechooserbutton_file_set(fbtn):
	print fbtn.get_filename()
def on_buttonSetupSave_clicked(btn):
#	config.add_section('FTP')
	config.set('FTP','address', entryFtpAddr.get_text())
	config.set('FTP','user', entryFtpUser.get_text())
	config.set('FTP','passwd', entryFtpPwd.get_text())
	config.set('FTP','folder', entryFtpFolder.get_text())
	
#	config.add_section('FOLDER')
	config.set('FOLDER','output', filechooserbutton.get_filename())



	with open('ds.cfg', 'wb') as configfile:
    		config.write(configfile)
def on_notebook1_switch_page(notebook, page, page_num):
	if page_num == 1:
		on_buttonSetupRefresh_clicked(None)
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

	"on_buttonSetupRefresh_clicked" :on_buttonSetupRefresh_clicked,
	"on_buttonSetupSave_clicked" :on_buttonSetupSave_clicked,
	"on_filechooserbutton_file_set": on_filechooserbutton_file_set,
	"on_notebook1_switch_page": on_notebook1_switch_page
##	"":,
}	
spinbuttonToTimeh = widgetTree.get_widget('spinbuttonToTimeh')
spinbuttonToTimem = widgetTree.get_widget('spinbuttonToTimem')
entryFtpAddr = widgetTree.get_widget('entryFtpAddr')
entryFtpUser = widgetTree.get_widget('entryFtpUser')
entryFtpPwd = widgetTree.get_widget('entryFtpPwd')
entryFtpFolder = widgetTree.get_widget('entryFtpFolder')

filechooserbutton = widgetTree.get_widget('filechooserbutton')
widgetTree.signal_autoconnect (dic)  

p.GetFiles() 
gtk.main()
