#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import time

def homeTeamGiants(regex):
	data = re.findall(r'homeTeamAbbr\"\:"(.*?)\"', str(regex))
	if str(data[0]) == "NYG":
		return True
	else:
		return False

def homeTeamJets(regex):
	data = re.findall(r'homeTeamAbbr\"\:"(.*?)\"', str(regex))
	if str(data[0]) == "NYJ":
		return True
	else:
		return False


try:
	url = 'http://www.giants.com/games-and-schedules/schedule.html'

	resp = urllib.request.urlopen(url)
	respData = resp.read()


except Exception as e:
	print(str(e))
	print("Error finding the page, check the URl")
	exit()

VAR = time.strftime("%Y%m%d") #Contains the date which is the ID to determine whether they won or lose

data = re.findall(r'%s(.*?)ameStatus' % VAR, str(respData))

for eachD in data:


	temp = re.findall(r'homeTeamScore\":(.*?)g', str(eachD))
	temp = re.findall(r'\d+', temp[0])

	b = homeTeamGiants(eachD)
	if b == True:
		if(int(temp[0]) > int(temp[1])): #comparing numbers that are strings
			print("The Giants won, get your $1 coffee!")
		else:
			print("The Giants lost, I'm sorry.")
	else:
		if(int(temp[0]) < int(temp[1])): #comparing numbers that are strings
			print("The Giants won, get your $1 coffee!")
		else:
			print("The Giants lost, I'm sorry.")
	break;


try:
	url = 'http://www.newyorkjets.com/schedule/season-schedule.html?campaign=clock'

	resp = urllib.request.urlopen(url)
	respData = resp.read()


except Exception as e:
	print(str(e))
	print("Error finding the page, check the URl")
	exit()


data = re.findall(r'%s(.*?)ameStatus' % VAR, str(respData))

for eachD in data:


	temp = re.findall(r'homeTeamScore\":(.*?)g', str(eachD))
	temp = re.findall(r'\d+', temp[0])

	b = homeTeamJets(eachD)
	if b == True:
		if(int(temp[0]) > int(temp[1])): #comparing numbers that are strings
			print("The Jets won, get your $1 coffee!")
		else:
			print("The Jets lost, I'm sorry.")
	else:
		if(int(temp[0]) < int(temp[1])): #comparing numbers that are strings
			print("The Jets won, get your $1 coffee!")
		else:
			print("The Jets lost, I'm sorry.")
	exit()


