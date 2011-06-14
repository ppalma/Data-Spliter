#!/usr/bin/python
#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
#----------------------------------------------------------------------------

from ftplib import FTP


class Picker:
	def __init__(self):
		self.ftp = None
		self.fromDate = None
		self.toDate = None
		self.stations = None
		self.connected = False

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

	def SetFromDate(self,yy='',mm='',dd='',h='',m='',s=''):
		self.fromDate = "%s/%s/%s %s:%s:%s"%(yy,mm,dd,h,m,s)

	def SetToDate(self,yy='',mm='',dd='',h='',m='',s=''):
		self.toDate = "%s/%s/%s %s:%s:%s"%(yy,mm,dd,h,m,s)

		
