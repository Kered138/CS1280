import random
import os

print("Hello World")
deck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J']
for i in range(1,11):
    for j in range(4):    
        deck.append(i)

def DrawCard():
    chosenNum = random.randint(0,52)
    chosenCard = deck[chosenNum]
    
    print()
    return chosenCard
def ShuffleDeck():
    global deck
    deck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J']
    for i in range(1,11):
        for j in range(4):    
            deck.append(i)
def clear():
    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def aging(self, years):
        self.age +=  years

class Student(Person):
    pass

p1 = Person("John", 36)
p2 = Student("Jeff", 17)
print(p1.age)
print(p1.name)
p1.aging(6)
print(p1.age)
print(p2.age)

#print(random.randint(0,6))
print(DrawCard(),DrawCard())




