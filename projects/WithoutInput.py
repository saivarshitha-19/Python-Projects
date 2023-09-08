
#Guessing an number without user input 

number=46
chances=0
while chances<=8:
  guessed_number=int(input("enter the number:"))
  chances+=1
  if number== guessed_number:
     print("Congratulations!!! you have guessed right!")
     break
  elif number>guessed_number:
     print("you are guessed smaller number")
  else:
     print("you are guessed larger number")
  if chances==7:
    print(" you are ran out the chance")
    print(" The number is",number)
    print("Better luck next time!!")