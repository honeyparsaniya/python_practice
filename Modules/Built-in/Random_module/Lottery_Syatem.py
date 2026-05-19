import random

participants=[]
num=int(input("Enter total number of participants="))

for i in range(num):
    name=input(f"Enter {i+1} name=")
    participants.append(name)

winner=random.choice(participants)
print("\nparticipants list:\n")
print(participants)
print("\nWinner participant=",winner)