import random
import time

print("Welcome to my random # guesser!")
print("After you type in your awnser, press ENTER to submit it.")
time.sleep(1)

top_range = input("Please choose the number you want the game to go up to: ")
time.sleep(1)
print(".")
time.sleep(1)
print("loading...")
time.sleep(1)
print(".")

if top_range.isdigit: 
    top_range = int(top_range) 
  
elif top_range <= 0:
      print("Please type a number larger than 0 next time.")
      quit() 
else:
    print('Please type a number next time')
    quit()
    
random_number = random.randint(0, top_range)
  
while True:
  user_guess = input('Now take a guess!: ')
  time.sleep(1)
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('please type a number next time.')
    continue
  
  if user_guess == random_number:
    print("You got it!")
    break
  else:
    print("You got it wrong!")
