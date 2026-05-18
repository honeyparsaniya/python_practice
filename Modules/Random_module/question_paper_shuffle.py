import random

total=int(input("Enter total number of question="))
questions=[]

for i in range(total):
    q=input(f"enter question {i+1}=")
    questions.append(q)

print("\nOriginal question paper:")
for q in questions:
    print(q)

random.shuffle(questions)
print("\nShuffled Question paper:")
for q in questions:
    print(q)