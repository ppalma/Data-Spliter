#!/usr/bin/python
#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
#----------------------------------------------------------------------------

from ftplib import FTP
import datetime

class Picker:
	def __init__(self):
		self.ftp = None
		self.fromDate = datetime.datetime.now()
		self.toDate = datetime.datetime.now()
		self.stations = None
		self.connected = False
		self.format = "%a %b %d %H:%M:%S %Y"
		print "init Picker"

	def Connect(self,addr='',user='',passwd=''):
		if self.ftp == None:
			ftp = FTP(addr,user,passwd)
			connected = True
			print "Connected"

	def Disconnect(self):
		if self.ftp <> None:
			ftp.quit()
			connected = False	
			print "Disconnected"

	def SetFromDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):
		self.fromDate = datetime.datetime(yy,mm,dd,h,m,s);
		print self.fromDate

	def SetToDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):

		self.toDate = datetime.datetime(yy,mm,dd,h,m,s);

		
