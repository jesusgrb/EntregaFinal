import os, sys
from shotgun_api3 import Shotgun 
import os.path
import time
from pprint import pprint

sg = Shotgun('http://upgdl.shotgunstudio.com', 'JGR', 'f5f9235e5ff91e4add702747098b9586a3dd06f1d23620c46c19c2177560dc8e')
global inputType, goodID, projectID, goodProjectID, savedVersions
codeToUpload = None

def validateType(userInputType):
	validationType = False
	while (validationType == False):
		if (userInputType == 'asset' or userInputType == 'a'):
			return 'Asset'
		elif (userInputType == 'shot' or userInputType == 's'):
			return 'Shot'
		else:
			userInputType = raw_input("ERROR - Invalid input. Try again\nWhat do you want to upload?\n-> Asset\n-> Shot\n").lower()

def validateID(userInputID):
	validationNum = False
	while (validationNum == False):
		try:
			userInputID = int(userInputID)
			return userInputID
		except:
			userInputID = raw_input("ERROR - ID must be a number.\nType in the correct ID:\n")
