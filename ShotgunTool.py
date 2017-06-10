import os, sys
from shotgun_api3 import Shotgun
import os.path
import time

sg = Shotgun("https://upgdl.shotgunstudio.com", "Tests", "4c1d11a4bfe1c118176a092c8155a022453a658e16618765668ddb9cfff6e254")

def validateType (userInputType):
	validationType = False
	while validationType == False:
		if userInputType == 'asset':
			return "Asset"
		elif userInputType == 'shot':
			return "Shot"
		else:
			userInputType = raw_input("ERROR, invalid data. Try again\nWhat do you want to upload?\n->Asset\n->Shot\n").lower()

def validateID(userInputID):
	validationNumber = False
	while validationNumber == False:
		try:
			userInputID = int(userInputID)
			validationNumber = True
		except:
			userInputID = raw_input("ERROR! The ID must be a number\nType the ID of the %s:"%inputType)

def validateIDShotgun (validatedID):
	try:
			shotgunValidation = False
			print inputType
			shotgunFile = sg.find_one(inputType, [["id", "is", validatedID]], ["id", "code"])
		print shotgunFile
	except Exception as e:
		print e
		#while shotgunValidation == False:
		#if shotgunFile == None:



option = raw_input("What do you want to upload?\n->Asset\n->Shot\n").lower()
inputType = validateType(option)
ID = raw_input("Type the ID of the %s:"%inputType)
inputID = validateID(ID)

print "Data correct"
time.sleep (5)


