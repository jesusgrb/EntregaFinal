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
		if (userInputType == 'asset'):
			return 'Asset'
		elif (userInputType == 'shot'):
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

def validateIDShotgun(validatedID):
	shotgunVal = False
	while (shotgunVal == False):
		shotgunFile = sg.find_one(inputType, [["id", "is", validatedID]], ["id", "code", "sg_status_list"])
		if (shotgunFile == None):
			newID = raw_input("ERROR - No %s with ID %s found on the project.\nType in the correct ID:\n" % (inputType, validatedID))
			validatedID = validateID(newID)
		else:
			print "The founded %s's name is: %s" %(inputType, shotgunFile['code'])
			shotgunVal = True
			return shotgunFile

def checkVersionsSG():
	global savedVersions, codeToUpload
	fields = ['id', 'code']
	filters = [['entity', 'is', {'type': inputType, 'id': goodID}]]
	versions = sg.find("Version", filters, fields)
	savedVersions = versions
	print "The versions in this %s are:" %inputType
	for v in versions:
		print 'VERSION: %s and his ID is: %d' % (v['code'], v['id'])

def asignName(inputName):
	global savedVersions
	global codeToUpload
	for v in savedVersions:
		if(inputName.lower() in v['code'].lower()):
			codeToUpload = v['code']
	if (codeToUpload == None):
		codeToUpload = inputName + "_v001"
		updateContent(goodID, codeToUpload, inputType)
	else:
		codeToUpload = codeToUpload[:len(codeToUpload) - 4] + ('_v%03d' %(int(codeToUpload[len(codeToUpload) - 3:])+ 1))
		updateContent(goodID, codeToUpload, inputType)

def createContent(id, code, taskType):
    data = {
        'project': {"type": "Project","id": id},
        'code': code,
        'description': 'Open on a beautiful field with fuzzy bunnies',
        'sg_status_list': 'ip'
    }
    result = sg.create(taskType, data)
    pprint(result)
    print "The ID of the %s is %d." % (result['type'], result['id'])

def createVersion(inType, ID, code, actionID, mediaPath, description):
	data = { 'project': {'type': 'Project','id': ID},
         'code': code,
         'description': description,
         'sg_status_list': 'rev',
         'entity': {'type': inType, 'id': actionID}
         }
	result = sg.create('Version', data)
	uploadContent(result['id'], mediaPath)

def deleteContent(inpType, inputID):
	result = sg.delete(inpType, inputID)
	print 'The %s has been deleted succesfully' %inpType

def updateContent(contentID, code, inputType):
	data = {
		'code': code,
		'description': 'Updating',
        'sg_status_list': 'ip'
	}
	result = sg.update(inputType, contentID, data)

def uploadContent(ID, mediaPath):
	result = sg.upload("Version", ID, mediaPath, field_name = "sg_uploaded_movie", display_name="Latest QT")
	print 'Uploaded succesfully'


'''
{
user_action = raw_input("Where do you want to upload your video?\n-> Asset\n-> Shot\n").lower()
inputType = validateType(user_action)
ID = raw_input("Type in the %s's VERSION ID:\n" %inputType)
goodID = validateID(ID)
mediaFile = '/Users/anapau/Desktop/Leak.mov'
checkVersionsSG()
versionID = raw_input("Type in the ID of the version where you want to upload your video:\n")
goodVersionID = validateID(versionID)
uploadContent(goodVersionID, mediaFile)
}
'''


'''
{
user_action} = raw_input("What do you want to delete?\n-> Asset\n-> Shot\n").lower()
inputType = validateType(user_action)
ID = raw_input("Type in the %s's ID:\n" %inputType)
goodID = validateID(ID)

deleteContent(inputType, goodID)
}
'''


'''
{
projectName = raw_input('Type in the name of the project you want to create a shot in:\n')
projectID = raw_input("Type in %s's ID:\n" %projectName)
goodProjectID = validateID(projectID)
user_action = raw_input("Where do you wanna create a new version?\n-> Asset\n-> Shot\n").lower()
inputType = validateType(user_action)
ID = raw_input("Type in the %s's ID:\n" %inputType)
goodID = validateID(ID)
#shotgunInfo = validateIDShotgun(goodID)
code = raw_input("Type in %s's version name:\n" %inputType)
mediaFile = '/Users/anapau/Desktop/Leak.mov'
desc = raw_input("Type in %s's description:\n" %inputType)
#uploadContent(goodVersionID, mediaFile)
createVersion(inputType, goodProjectID, code, goodID, mediaFile, desc)
}
'''

'''
{
user_action = raw_input("Type what you want to upload?\n-> Asset\n-> Shot\n").lower()
inputType = validateType(user_action)
ID = raw_input("Type in the %s's ID:\n" %inputType)
goodID = validateID(ID)
shotgunInfo = validateIDShotgun(goodID)
}
'''


'''{
projectName = raw_input('Type in the name of the project you want to create a shot in:\n')
projectID = raw_input("Type in %s's ID:\n" %projectName)
goodID = validateID(projectID)
user_action = raw_input("Type what you want to create?\n-> Asset\n-> Shot\n").lower()
inputType = validateType(user_action)
code = raw_input("Type in %s's name:\n" %inputType)

createContent(goodID, code, inputType)
}'''


print 'Data correct'
time.sleep(5)





