print("Welcome to my quiz game!")

playing = input("Do you want to play?\nAnswer Yes or No: ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's play:)\n")

score = 0

answer = input("What does the CPU stand for?\nWrite your answer: ")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n") 

answer = input("What does the GPU stand for?\nWrite your answer: ")
if answer.lower() == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")   

answer = input("What does the RAM stand for?\nWrite your answer: ")
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")   

answer = input("What does the PSU stand for?\nWrite your answer: ")
if answer.lower() == "power supply unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

print("You got " + str(score) + " questions correct!") 
print("You got " + str((score/4) * 100) + "%.\n")

if score < 2:
    print("You are fucked up!!!")
else:
    print("Ok, you pass")