#Lucy Murphy ft. Bubbles the Duck
#01-26-22
#Song of the day: The Logical Song (Supertramp)
#Source of problem: https://edabit.com/challenge/kpPkYohYvGJWWEb6Q

#####################
#                   #
# STRINGS AND FRETS #
#                   #
#####################

##############
#INSTRUCTIONS#
##############

#Write a function that gets a string number and a fret of a 6-string guitar in 'standard tuning'
#and return the corresponding note.
#For this challenge we use a 24 fret model.
#Try not to use a 2 dimensional list.
#View this image for guitar infromation: https://edabit-challenges.s3.amazonaws.com/24-frets.png

######################
#SPOILERS/MY SOLUTION#
######################


def isInputValid(givinInfo):   #Tests the user input for valid string and fret num
    #wont let me use whitespace the way I want... hmm could be another error
    #I know there is a way to separate the or statements just for better whitespace, but its been a while since I used python
    if (givinInfo[0] > 6) or (givinInfo[0] < 1) or (givinInfo[1] > 24) or (givenInfo[1] < 0):   #I like to separate bc I think it adds read ability, but this could all be one line 
        return(False)   #Invalid input
    else:
        return(True)   #Dont think i need this try without it

def GetAndCheckInput():   #obtain input from the user and call the isInputValid(() function
    givinInfo= []   #list that will hold fret and string numbers
    print("SMTH CUTE here idk guitar word art \n Howdy there! Welcome to the guitar shop! \n I hear you want to learn to play.")
    name = input("THAT IS WONDERFUL!! What did you say your name was?")   #just making it a little for fun for me personally
    print(name + " is a pretty cool name, alright so lets go over some different notes." +   #sry if the splitting bothers you, I dont like long lines
          "Why dont you place your finger anywhere and Ill tell you the note")   #thats a flimsy story line, maybe ill fix it.
    fret = int(input("what fret is your finger on?"))   #IK all the dialauge is unnessasary but I think it makes the code more fun, and thats the point
    stringNum = int(input("what string is your finger on?")) #ugh this dialauge is rly stilted, maybe a UI would be alot better. I just have alot of work today.
    givinInfo.append(stringNum) #I feel like I could make this one line...
    givinInfo.append(fret)
    #print(givinInfo) Passed test
    if isInputValid(givinInfo) == False:
        print ("Invalid input") #Make this an input loop later...
    


#OK So at this point in the process I am looking for patterns in the note stuff.
#Repeates every 5 frets

def fretCombos(fret): #get input from GetAndCheckInput
    if fret % 5 == 0:  #every 5 frets repeats
        print (fret) #Test to be commented out 
    

def _main():
    GetAndCheckInput()
    return
    
    
_main()
        
    
