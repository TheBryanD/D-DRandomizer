#
#                   TODO
#
#  Work on GUI
#       Work on scaling Fonts
#       On hover change mouse pointer
#  Finish Classes, Artifact, and Magic items
#       Seperate Artifacts from magic items
#  Add elf subraces
#  Add/Finish Encounter DB
#
#
#########################################################################################

##################################   Imports   ##########################################

#webbrowser to open url
import webbrowser
#for random numbers
import random
#import tkinter for GUI
import tkinter as tk
from tkinter import font

##################################   /Imports   ##########################################


##############################################################   Classes   ############################################################################

#Object class for items that are added from database
class obj:
    #vars
    name = ''
    url = ''

    #constructor
    def __init__(self, name, url):
        self.name = name
        self.url = url

##############################################################   /Classes   ############################################################################


##############################################################   GUI   ############################################################################

    #FontSize
    global fontSize
    fontSize = 10

#initialize window of GUI
def initializeWindow():

    #Create RootWindow
    global rootWindow
    rootWindow = tk.Tk()
    rootWindow.title("D&D Randomizer")
    rootWindow.geometry("800x500")
    rootWindow.bind("<Configure>", resizeWindow)

    #Button Frame to hold all of the buttons
    global buttonFrame
    buttonFrame = tk.Frame(rootWindow, background="#620004", borderwidth=5, relief="ridge")
    buttonFrame.place(relheight=1, relwidth=0.25, relx=0.75, rely=0)

    #Info Frame to hold what the buttons update
    global infoFrame
    infoFrame = tk.Frame(rootWindow, background="#0e0005")
    infoFrame.place(relheight=1, relwidth=0.75)

    ### LABELS ####

    #vars
    labelRelHeight = 0.09
    labelRelWidth = 0.3
    global labelFont
    labelFont = font.Font(family="Calibri", size=fontSize, weight="bold")
    labelBGColor = "#7e000f"
    labelFontColor = "white"

    #Label in info Frame to hold the name string of item
    global encounterLabel
    encounterLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont, justify="left", wraplength=150, relief="ridge", borderwidth=5)
    encounterLabel.place(relheight=1, relwidth=0.25, relx=0, rely=0)
    global animalLabel
    animalLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    animalLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.11)
    global armorLabel
    armorLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    armorLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.21)
    global artifactLabel
    artifactLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    artifactLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.31)
    global classLabel
    classLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    classLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.41)
    global magicItemLabel
    magicItemLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    magicItemLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.51)
    global monsterLabel
    monsterLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    monsterLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.61)
    global mundaneItemLabel
    mundaneItemLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    mundaneItemLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.71)
    global raceLabel
    raceLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    raceLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.81)
    global weaponLabel
    weaponLabel = tk.Label(infoFrame, text='', background=labelBGColor, foreground=labelFontColor, font=labelFont)
    weaponLabel.place(relheight=labelRelHeight, relwidth=labelRelWidth, relx=0.3, rely=0.91)


    global labelArray
    labelArray = [encounterLabel, animalLabel, artifactLabel, classLabel, magicItemLabel, monsterLabel, mundaneItemLabel, raceLabel, weaponLabel]

    ### /LABELS ####

    makeButtons()


#make buttons for GUI
def makeButtons():

    #Vars
    buttonHeight = 0.05
    buttonWidth = 0.5
    global buttonFont
    buttonFont = font.Font(family="Calibri", size=10, weight="bold")
    buttonColor = "#1e000a"
    buttonFontColor = "white"

    #Encounter button
    getRandomEncounterButton = tk.Button(buttonFrame, text="Encounter", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=encounterArray,file="../D&DRandomizer/DB/EncounterDB.txt",label=encounterLabel:getRandomObj(array, file, label))
    getRandomEncounterButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.01)

    #Animal button
    getRandomAnimalButton = tk.Button(buttonFrame, text="Animal", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=animalArray,file="../D&DRandomizer/DB/AnimalDB.txt",label=animalLabel:getRandomObj(array, file, label))
    getRandomAnimalButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.11)

    #Armor Button
    getRandomArmorButton = tk.Button(buttonFrame, text="Armor", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=armorArray,file="../D&DRandomizer/DB/ArmorDB.txt",label=armorLabel:getRandomObj(array, file, label))
    getRandomArmorButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.21)

    #Artifact button
    getRandomArtifactButton = tk.Button(buttonFrame, text="Artifact", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=artifactArray,file="../D&DRandomizer/DB/ArtifactDB.txt",label=artifactLabel:getRandomObj(array, file, label))
    getRandomArtifactButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.31)

    #Classes button
    getRandomClassButton = tk.Button(buttonFrame, text="Class", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=classArray,file="../D&DRandomizer/DB/ClassesDB.txt",label=classLabel:getRandomObj(array, file, label))
    getRandomClassButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.41)

    #Magic-Item Button
    getRandomMagicItemButton = tk.Button(buttonFrame, text="Magic Item", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=magicItemsArray,file="../D&DRandomizer/DB/Magic-itemsDB.txt",label=magicItemLabel:getRandomObj(array, file, label))
    getRandomMagicItemButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.51)

    #Monster button
    getRandomMonsterButton = tk.Button(buttonFrame, text="Monster", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=monsterArray,file="../D&DRandomizer/DB/MonsterDB.txt",label=monsterLabel:getRandomObj(array, file, label))
    getRandomMonsterButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.61)

    #Mundane Item Button
    getRandomMundaneItemButton = tk.Button(buttonFrame, text="Mundane Item", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=mundaneItemsArray,file="../D&DRandomizer/DB/MundaneItemsDB.txt",label=mundaneItemLabel:getRandomObj(array, file, label))
    getRandomMundaneItemButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.71)

    #Race Button
    getRandomRaceButton = tk.Button(buttonFrame, text="Race", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=raceArray,file="../D&DRandomizer/DB/RaceDB.txt",label=raceLabel:getRandomObj(array, file, label))
    getRandomRaceButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.81)

    #Weapon Button
    getRandomWeaponButton = tk.Button(buttonFrame, text="Weapon", font=buttonFont, foreground=buttonFontColor, background=buttonColor, relief="flat", command=lambda array=weaponArray,file="../D&DRandomizer/DB/WeaponDB.txt",label=weaponLabel:getRandomObj(array, file, label))
    getRandomWeaponButton.place(relheight=buttonHeight, relwidth=buttonWidth, relx=0.25, rely=0.91)

    #Main loop for GUI
    rootWindow.mainloop()

#Changes font based on window size (doesnt work correctly)
def resizeWindow(event):
    #if x <= 500: set fontSize to 10
    if(rootWindow.winfo_width() in range(0,500)):
        fontSize = 10
        #go through array of labels and resize them
        for item in labelArray:
            #Change button fontSize since the amount of buttons are same or less than labels
            buttonFont.config(size=fontSize)
            #change label fontSize
            labelFont.config(size=fontSize)
            item.config(font=buttonFont)
            #Change length of word wrap for the encounter label on left side
            encounterLabel.config(wraplength=100)
    #if 500 < x > 1200:
    elif rootWindow.winfo_width() in range(500, 1200):
        fontSize = 15
        for item in labelArray:
            buttonFont.config(size=fontSize)
            labelFont.config(size=fontSize)
            item.config(font=buttonFont)
            encounterLabel.config(wraplength=150)
    #if x > 1200
    else:
        fontSize = 20
        for item in labelArray:
            buttonFont.config(size=fontSize)
            labelFont.config(size=fontSize)
            item.config(font=buttonFont)
            encounterLabel.config(wraplength=200)
    #encounterLabel.config(text="Size:" + str(rootWindow.winfo_height()) + " x " + str(rootWindow.winfo_width()))


##############################################################   /GUI   ############################################################################

############################  Vars  ####################################
#Url for API
#baseURL = "https://www.dnd5eapi.co"

#Arrays
encounterArray = []
animalArray = []
armorArray = []
artifactArray = []
classArray = []
magicItemsArray = []
monsterArray = []
mundaneItemsArray = []
raceArray = []
weaponArray = []

############################  /Vars  ####################################

##############################################################   Functions  ############################################################################
#Gets a random number between n and m
def Roll(n, m):
    num = 0
    if(m > 0):
        num = random.randint(n, m)
    return num

#Open URL into browser
def openURL(url):
    try:
        webbrowser.open(url)
    except:
        print("Error Opening URL...")

#New Load Array Fun:
def loadArray(DBFile, arrayToLoad):

    #vars
    a = True
    #open the file passed to the function
    f = open(DBFile, 'rb')

    #start looping through items
    while a:
        #get the data
        name = f.readline()
        #check if EOF, if so then quit loop
        if name == ''.encode('utf-8'):
            a = False
            break
        url = f.readline()
        arrayToLoad.append(obj(name, url))

        print(name)
        print(url)

    #close the file
    f.close()

#Get a random object and change the text on the label, bind button 1 to array[random Num] to open obj url
def getRandomObj(array, file, label):
    #if array is empty, then load array, otherwise skip
    if(len(array) == 0):
        loadArray(file, array)
    #get random number from 0 to arrayHi-1
    rNum = (Roll(0, len(array)-1))
    #change text on label to array[rNum].name
    try:
        label.config(text=array[rNum].name)
        #bind mouse 1 to openURL(urlToOpen)
        label.bind('<Button-1>', lambda e,url=array[rNum].url:openURL(url))
    except:
        print('ERROR in getRANDOMObj')

##############################################################   /Functions  ############################################################################

##############################################################   Main  ############################################################################

#Create GUI window
initializeWindow()

##############################################################   /Main  ############################################################################
