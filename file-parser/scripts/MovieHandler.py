#!/usr/bin/python
import xml.etree.ElementTree as ET
class MovieHandler():
	def _init_(self):
		print("Hello")
	
	#Define function to accept xml
	def findAllMovie(self, file):
		tree = ET.parse(file)
		root = tree.getroot()
		for movie in root.findall('movie'):
			print(movie.get('title'))
			
	#Define function to accept xml
	def findYearOfMake(self, file, movieName):
		tree = ET.parse(file)
		root = tree.getroot()
		for movie in root.findall('movie'):
			if movieName == movie.get('title'):
				print(movie.find('year').text)

		
		
	
