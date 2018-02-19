import random
def talk():
	print "What would you like to talk about Amir?Choose a number"
	print "1.Do you think your going to make another club?"
	print "2.How's it like being in a phone?"
	print "3.Whats going on?"
def poem():
  ranom = ['roses are red,voilets are blue,you are dead and I am to',
            'Everyone can go through a door but many,instead hit the floor',
            "When you think,that what matters is a lawn,you end up becoming it's pawn",          
           "The hardest part " 
           "to any journey "
           "you embark " 
           "is the start. ",
           "The dogs are barking at the stillness, the stillness is still.",
           "Do not dream too loudly.You may awaken your conscience",
           "Come sit with me my dear,Even the Stars need the Darkness to shine.",
           "disappear for a bit, those who look for you, keep them.",
           "Only those  you trust can betray you",
           "As time trickle down the stream,we bow down to fate, saluting the years",
           "We can never go back,but we can go on!"
           "Don't loose the battle" 
            "Within yourself "
            "Only to take it out" 
            "On the rest of the world" 
            "  In the end" 
            "  We call it "
            "  A"
             " Bully"
           ]
  print random.choice(ranom)
  whattodo()
def whattodo():
	print "what would you like to do with me",text,"today?(play,talk,advice)"
	command = raw_input("")
	if command == "advice":
          poem()
        if command == "talk":
    	  talk()

def greeter():		
	greetings = ["Hello","Whats going on!","Nice to see you","hi,nice to see you.","Hey,feeling lonely?","Have you had a good day?yes or no"]
	greeting = random.choice(greetings)
	print "Hi,welcome to my text world,in case you want to hang out in your phone."
	print greeting
	if greeting == "Have you had a good day?yes or no":
		    response = raw_input("")
		    if response == "yes":
				print "Thats Fantasic to hear"
				whattodo()
		    if response == "no":
		    		print "Oh...well I hope I can make that day better"
		    		whattodo()
	else:
		    whattodo()
		
fw = open('name.txt','r')
text = fw.read()
if text == "" :
	fw.close()
	print "What is your name?"
	global name
	name = raw_input("")
	fr = open('name.txt','w')
	fr.write(name)
    	fr.close()
else:
	greeter()
