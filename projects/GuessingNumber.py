
#Guessing number through user input 



while True: # it is used to stop the excetion when it is guessed correct number
 
 import random # import random module

 #Input the lower_limit and upper_limit
 lower_limit=int(input("Enter the lower limit:"))
 upper_limit=int(input("Enter the upper limit:"))


 #randint method generates a random integer number
 #it requries two parameters to determine the range
 random_number=random.randint(lower_limit,upper_limit)

 print(random_number)
 chances=0 # it is used to calculate the no of chances
 print(f"You have to guess between {lower_limit}and {upper_limit} ")
 while chances<=8:
   #guess is write
   guess_number=int(input("Enter the guess:"))
   if random_number==guess_number:
      print("Congratulations!!!! You have guessed the number")
      break #break statement is used stop the statement when it is true
   elif random_number>guess_number:
       print("You are guessed smaller number")
   else:
       print("You are guessed large number")
   if chances==8:
       print("Sorry you are out of chances ")
       print("The numberis",random_number)
       print("Better luck next time ")
       break
   
 
 break