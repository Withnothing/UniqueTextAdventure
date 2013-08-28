from time import sleep
import random 

HP = ""
Strength = ""
Intelligence = ""


def welcomeMessage():
    name = input("what's your name?")

    if name == "" or name == int:
       print ("You did not enter your name!")

    else:
        print ("So, your name is %s?" % (name))
        print
        print("You're a very brave hero!")
        print
        print ("If you see words capitalized, then it means you can choose between these answers, you should type in these answers AS WRITTEN!")


def equipmentStart():
    equipment1 = ["Pistol", "Sniper", "Amulet", "Gold"]
    equipment2 = ["Health kit", "Knife", "Ninja sword", "Silver"]
    print ("Welcome hero, choose your equipment: ")
    print
    print (equipment1)
    print (equipment2)
    print ("#1 for inventory1 and #2 for inventory2")
    equipment = input('> ')

    if equipment == "1":
        print("You've chosen the following items:")
        print
        print(equipment1)
        print
        print("An excellent choice for long-range combat!")
        print
        print

    elif equipment == "2":
        print("You've chosen the following items:")
        print
        print(equipment2)
        print
        print("Perfect equipment for an assasin!")
        print
        print

    else:
        print("Please type 1 or 2!")
        print(equipmentStart())


def equipmentPotions():
    potions = {"1 potion of regenerate HP": "gives you 25 HP when used", "1 potion of strength": "gives you temporary 25 points of strength" }
    print ("And these are the potions you have in your bag:")
    print
    print
    print
    print (potions)
    print
    print

def playerStats(HP,Strength,Intelligence):
    HP = " HP :500"
    Strength = " Strength: 150"
    Intelligence = "Intelligence: 200"
    print("And last but not least, your stats:")
    print
    print(HP)
    print(Strength)
    print(Intelligence)
    

def playAgain():
            againAnswer = input("Would you like to play again? YES OR NO?")
            if againAnswer == 'YES':
                print ("You won't give up, uh?")
                print (prologue())
            

            elif againAnswer == 'NO':
                print ("See ya next time!")

            else:
                print("YES or NO only, please!")
                print(playAgain())
def prologue():
    print("PROLOGUE")
    print ("You have been hunting in the forest for a while and decided to go back to your hometown Sumonia.")  
    print
    print
    print ("The way back is long and dark, you feel a little psychopatic... You've heard from a shortcut nearby, but it's dangerous there.")
    print
    print
    firstChoice = input ("Do you wanna TAKE THE RISK or STAY ON TRACK?")
    if firstChoice == "TAKE THE RISK":
        print ("You walk down a hill...")
        sleep(2.5)
        print
        print ("And fall into a giant ravin!")
        print (playAgain())        

    elif firstChoice == "STAY ON TRACK":
        print ("You continue you journey to your hometown, you chose wisely!")

    else:
        print("You can't choose that!")
        print(prologue())



def chapter1():
    print("CHAPTER 1")
    print
    print ("You continue walking, glad that you've taken the right way.")
    print
    print ("After a while, you get very thirsty.")
    print
    print ("You see a little lake and you're tempting to drink from it...")
    print
    DrinkOrContinue = input ("Do you DRINK or CONTINUE?")
    if DrinkOrContinue == 'DRINK':
        print ("You drink for a while and...")
        sleep(2.5)
        print
        print ("feel great and refreshed!")
        print(chapter2())

    elif DrinkOrContinue == 'CONTINUE':
        print("After you start running again you slowly dry out and drop unconscious to the ground!")
        print (playAgain())

    else:
         print("Please choose between the give options, please!")
         print(chapter1())

def chapter2():
    print("CHAPTER 2")
    print
    print("")
    
     

print (welcomeMessage())
print (equipmentStart())
print (equipmentPotions())
print (playerStats("HP","Strength","Intelligence"))
print (prologue())
print (chapter1())


                
        





    

    


    

    

