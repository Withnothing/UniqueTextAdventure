
def shopPurchase(): 
   inventory = []
   shop = ["Sword","Dagger","HP potion"]

   print("This is what we've got in store today:")
   print(shop, '\n')
   print("And this is your inventory:")
   print(inventory)
   buyItem = input("What would you like to buy? Type #1, #2 or #3")

   if buyItem == "1":
       inventory.append("Sword")
       print(inventory)
       buyMore = input("Would you like to buy more? YES or NO?")
       if buyMore == "YES":
           print (buyItem)

       else:
            print("Thanks for visiting!")
           
           
           

   buyItem = input("What would you like to buy? Type #1, #2 or #3")

   if buyItem == "2":
       inventory.append("Dagger")
       print(inventory)
       buyMore = input("Would you like to buy more? YES or NO?")
       if buyMore == "YES":
           print (buyItem)

       else:
           print("Thanks for visiting!")
         
        

   buyItem = input("What would you like to buy? Type #1, #2 or #3")

   if buyItem == "3":
        inventory.append("HP potion")
        print (inventory)
        buyMore = input("Would you like to buy more? YES or NO?")
        if buyMore == "YES":
           print (buyItem)

        else:
             print("Thanks for visiting!")
            
            


shopPurchase()
