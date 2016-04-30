#!/usr/bin/python
from MovieHandler import * #get classes from ClassOne file
movieHandler = MovieHandler()
print("Name of all movies in xml:")
movieHandler.findAllMovie("SampleXmlFile.xml")
print("\nYear of making of Movie 'Enemy Behind':")
movieHandler.findYearOfMake("SampleXmlFile.xml", "Enemy Behind")