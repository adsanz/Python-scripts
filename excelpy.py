# Points of participation
# dependencies = pandas, openpyxl, xlrd, colorama
# Made by @AdSanz_IT
# version V.2

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import load_workbook
import xlrd
import datetime
from colors import *
from colorama import init
init()

#Define los atributos de los alumnos
class alumno():
	name_alu = ""
	points = 0
	estado = ""
	def __init__(self):
		self.points = 0

	def name(self,nombre):
		self.name_alu = nombre

	def increase(self,user_increase_points):
		self.points += user_increase_points

	"""
	Future use to see the "state" of the student points
	def status(self):
		if self.points < 10:
			self.estado = "Bad"
		elif self.points < 20 and self.points > 10:
			self.estado = "Good"
		elif self.points <  40 and self.points > 20:
			self.estado = "Excelent"
		else:
			print("You cannot have more points than that")
	"""
#Define students
ASM = alumno()
DSC = alumno()
#Define the name of the student
ASM.name("Adrian Sanz Melchor")
DSC.name("David Saldaña Castaño")

#date
now = datetime.datetime.now()
date = str(now.strftime("%Y-%m-%d %H:%M"))

#List of the students to iterate later on "increase_points"
alu_list = [ASM,DSC]

#Save to excel
def Excel():
	#Define the DataFrame which will be used in excel
	df1 = pd.read_excel('prueba.xlsx')
	df = pd.DataFrame({'Alumno':[ASM.name_alu,DSC.name_alu],
		'Puntos':[ASM.points,DSC.points],
		'Fecha': date})
	#Saves the data
	writer = ExcelWriter('prueba.xlsx', engine='openpyxl')
	df1.to_excel(writer,'Sheet1',index=False, startrow=0,)
	df.to_excel(writer,startrow=len(df1)+1,index=False,)
	writer.save()

#Iterates through alu_list and adds points
def increase_points():
	for x in alu_list:
		print("Increasing points to: " + CBEIGE + "{}".format(x.name_alu) + CEND)
		user_increase_points = int(input("Number of points: "))
		x.increase(user_increase_points)
		print(CGREEN + "{} points added".format(x.points) + CEND)

#Read the data on the excel to show it on the terminal
def read_ex():
	df1 = pd.read_excel('prueba.xlsx')
	df = pd.DataFrame({'Alumno':[ASM.name_alu,DSC.name_alu],
		'Puntos':[ASM.points,DSC.points]})
	df2 = pd.read_excel('prueba.xlsx',sheet_name='Sheet1')
	print(df2)


#Main
print(CRED2 + "Welcome!\nPoint Increaser v2.0\nMade my @AdSanz_IT\n" + CEND)
increase_points()
Excel()
print(CVIOLET2 + "Done!" + CEND)
read_ex()
