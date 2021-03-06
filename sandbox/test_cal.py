from tkinter import *
import tkinter as tk
import calendar as cal
from datetime import datetime
import time
from functools import partial

def currMonth(current, display):
	display['year'] = current['year']
	display['month'] = current['month']
	drawMonth()
	return

def nextMonth(current, display):
	if display['month'] == 12:
		display['year'] += 1
		display['month'] = 1
	else:
		display['month'] += 1
	drawMonth()
	return

def prevMonth(current, display):
	if display['month'] == 1:
		display['year'] -= 1
		display['month'] = 12
	else:
		display['month'] -= 1
	drawMonth()
	return

def drawMonth():
	# Get Number of Days and Numbers of Full or Partial Weeks in This Month
	#		Note on line 16: calendar's monthrange(year,month) function returns
	#		a tuple like (2, 29). See documentation for more info
	monthRange = cal.monthrange(display['year'], display['month'])
	numDays = monthRange[1]
	if numDays % 7 != 0: # if days don't divide evenly into 7, need extra week row to display month
		rowsForWeeks = int(numDays / 7) + 1
	else:
		rowsForWeeks = int(numDays / 7)

	showMonth = tk.LabelFrame(app, font = 'Verdana 13 bold', fg='#CFD0C2', bg='#272822', labelanchor='n')
	showMonth['text']=(cal.month_name[display['month']], str(display['year']))
	showMonth.grid(row=1, columnspan=7, padx=30, pady=30, ipadx=0, ipady=0)
	# Display Day of Week Headers
	for x in range(7):
		tk.Label(showMonth, text=cal.day_abbr[x], # Can also use day_name[x] for full name
			 borderwidth=1, padx=5, pady=5, fg='#CFD0C2', bg='#272822', font='Verdana 11 bold').grid(row=1,column=x)

	# Determine What Day of the Week the First Day Falls On (0 for Monday, etc.)
	firstDayOffset = cal.weekday(display['year'], display['month'], 1)
	# Display Month as a Grid of Days

	daysShown = 0 # Counter starts at zero
	dayBlock = [] # Empty list for tkinter labels, each containing one calendar day
	for wk in range(rowsForWeeks):
		for day in range(7):
			if firstDayOffset != 0:
				nullDay = tk.LabelFrame(showMonth)
				nullDay.configure(border=0)
				nullDay.grid(row=wk+2,column=day)
				firstDayOffset = firstDayOffset - 1
			else:
				# If number of days printed to grid so far is less than the days in
				# a given month, add another day
				if daysShown < numDays:
					dayBlock.append(tk.LabelFrame(showMonth, text=daysShown, fg='#CFD0C2'))
					dayBlock[daysShown].configure(text='%s'%(daysShown + 1), borderwidth=1, padx=0, pady=15, width=100, height=90, fg='#CFD0C2', bg='#272822')
					dayBlock[daysShown].grid(row=wk+2,column=day)
					#tk.Label(showMonth, text='%s'%(daysShown + 1), borderwidth=1, padx=5, pady=5, width=10, height=5, fg='#CFD0C2', bg='red', takefocus=1).grid(row=wk+2,column=day)
					daysShown = daysShown + 1

def nada():
	return

app = tk.Tk() # Create App Object in Tkinter

menuBar = Menu(app)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=nada)
fileMenu.add_command(label="Open", command=nada)
fileMenu.add_command(label="Save", command=nada)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=app.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help", command=nada)
helpMenu.add_command(label="About", command=nada)
menuBar.add_cascade(label="Info", menu=helpMenu)

app.configure(background='#272822', width=500, menu=menuBar) # Paint it Dark Theme
app.wm_title('Calendar App') # Anyone good at coming up with names?

# CALCULATE CURRENT DATE (& store this info for when user jumps back to current month)
current = {'day'	: datetime.now().day,
		   'month'	: datetime.now().month,
		   'year'	: datetime.now().year}

# MONTH TO DISPLAY IN CALENDAR (starts as current date by default)
display = {'month'	: current['month'],
		   'year'	: current['year']}

# Buttons
calNav = tk.LabelFrame(app, font='Verdana 8', text='Calendar Navigation', fg='#CFD0C2', bg='#272822', labelanchor='n')
calNav.grid(row=0, columnspan=7, padx=5, pady=5, ipadx=5, ipady=5)
prevMonthBtn = tk.Button(calNav, text=' <= Prev ', bg='#CFD0C2', command=partial(prevMonth, current, display)).grid(row=1,column=1,padx=5, pady=5, sticky='w')
currMonthBtn = tk.Button(calNav, text=' Current ', bg='#CFD0C2', command=partial(currMonth, current, display)).grid(row=1,column=2,padx=5, pady=5, sticky='n')
nxtMonthBtn = tk.Button(calNav, text=' Next => ', bg='#CFD0C2', command=partial(nextMonth, current, display)).grid(row=1,column=3,padx=5, pady=5, sticky='e',)

drawMonth()

# Task list
taskFrame = tk.LabelFrame(app, text='            Task List            ', bg='#272822',fg='#CFD0C2')
taskFrame.grid(row=1, column=8, rowspan=5,sticky='NS', padx=25, pady=30)
taskContent = tk.Label(taskFrame, text="-", bg='#272822',fg='#CFD0C2')
taskContent.grid(row=0)

app.mainloop()
