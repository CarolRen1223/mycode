# This is a game anout a man/woman how to escape the desert island#
print "You wake up, and find yourself in a desert island.No human is here"
print "you can't remember why you came here,even who you are."
print '"What happend to me?",you think.'
print "you look up yourself,try to find out your gender."
print "Check what gender are you, female or male?\n"


#users will enter his/her gender, 
#this is related to later scene.
gender=raw_input("Plese enter your gender (Female or Male):")
print "\nAlright, so you figure out your gender , you are a "+str(gender)



print "\nYou look aroud, and find a bag!!"
print "Do you want to pick up the bag and examin it?\n"

#let user choose yes or no
pick=raw_input("Please enter your choice(Yes or No):")



#This is your Id card info
if pick=="Yes":
    print "\nWow, you find a lot of items," 
    print "and there even are two ID card, maybe you can know your identity!!"
    print "there are 2 ID cards here, which one is yours?"
    print "\n"
    print "\n"
    print "----------------------           ----------------------"
    print "|Name: Jack          |           |Name: Rose          |"
    print "|Gender: Male        |           |Gender: Female      |"
    print "|Birthday: 1986/11/21|           |Birthday: 1990/12/15|"
    print "|Job: Explorer       |           |Job: Dancer         |"
    print "----------------------           ----------------------"
    print "\n"
    print "\n"
    print "Now think about your gender, which one is yours?"
    ID=raw_input("(Jack or Rose):")#if USER choose male ,she must choose "Jack"
    if gender=="Male": 
        if ID=="Jack":#User is male,and he choose "jeck", he is right!
            print str(ID)+", You find your ID!! "
            print "And you fins tools in this bag. Using the tool, you can make a boat and escape!!"
            print "Congratulations!! you did it!! you pass the game"
        else:
            print "Sorry, you are a %r, but you choose%r."%(gender,ID)
            print "The gender dosen't match, you lose the game"   
            
    else:
        if ID=="Rose":#if USER choose female ,she must choose "Rose"
            print str(ID)+", You find your ID!! "
            print "And you fins tools in this bag. Using the tool, you can make a boat and escape!!"
            print "Congratulations!! you did it!! you pass the game"
        else:
            print "Sorry, you are a %r, but you choose%r."%(gender,ID)
            print "The gender dosen't match, you lose the game"          

else:
    print "Sorry, you don't know who you are and you don't have tools to help you out" 
    print "you lose the game!"    
    
    
 




