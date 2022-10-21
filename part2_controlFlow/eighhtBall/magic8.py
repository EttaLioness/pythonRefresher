import random

name = "Nicole"
#store the question
question = "Will I win the lottery?"
#store your answers
answer = ""
#store random number generated
random_number = random.randint(1, 9)
#generate a random number between 1 (inclusive) and 9 (inclusive). 
#Note In Python, we can use the .randint() function from the random module to generate a random number from a range. But first, import this module so we can use its functions. Add this line of code to the top of your file: import random. 

#here checking if random value is being generated
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
#=========================================

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)
  
print("Magic 8 Ball's answer: " + answer)
