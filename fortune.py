import random

print("Python Fortune Teller")
print("---------------------")

greetings = ['yes', 'no', 'maybe', 'try again later']

while True:
    question = input("Ask me a question and I'll predict your future: \n")
    rand = random.choice(greetings)
    print(rand)