#!/usr/bin/env python3

import random
import sys
import time

responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Hazy', 'Yes definitely', 'You may rely on it',
'As I see it, yes',  'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it',
'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print("What is your question, peasant?")

user_input = input()

while user_input != "quit":

                print("Thinking ", end="")
                sys.stdout.flush()
                time.sleep(1)                           #adding time delay between dots to simulate loading for aesthetic effect
                print(".", end="")
                sys.stdout.flush()
                time.sleep(1)
                print(".", end="")
                sys.stdout.flush()
                time.sleep(1)
                print(".", end="")
                sys.stdout.flush()
                time.sleep(1)
                print()                                         #double print() simply to create spacing between lines
                print()

                print(random.choice(responses))
                print()

                print("Ask another question, or type 'quit' to exit")

                user_input = input()

else:
        sys.exit()
