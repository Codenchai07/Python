# create a program capable of displaying to the user like KBC

questions = [
    """1. Which keyword is used to define a function in Python?
A. func
B. define
C. def
D. function""",

    """2. What is the output of len("Python")?
A. 5
B. 6
C. 7
D. 8""",

    """3. Which data type is immutable?
A. List
B. Dictionary
C. Tuple
D. Set""",

    """4. Which loop is used when the number of iterations is known?
A. while
B. do-while
C. for
D. repeat""",

    """5. Which operator is used for exponentiation?
A. ^
B. **
C. //
D. %""",

    """6. Which function is used to take input from the user?
A. scan()
B. read()
C. input()
D. gets()""",

    """7. What is the extension of a Python file?
A. .java
B. .cpp
C. .py
D. .html""",

    """8. Which keyword exits a loop immediately?
A. continue
B. stop
C. break
D. return""",

    """9. Which data structure stores key-value pairs?
A. List
B. Tuple
C. Dictionary
D. Set""",

    """10. Which function displays output?
A. output()
B. display()
C. print()
D. show()"""
]

answers = [
    "C",
    "B",
    "C",
    "C",
    "B",
    "C",
    "C",
    "C",
    "C",
    "C"
]
amount = 0
winningAmount = 200000

print("Welcome to KBC of tech Game")
print("---------------------------")
print("please provide some details about you")
username = input("enter your name: ")
age = int(input("enter your age: "))

if age >= 18:
    print("You're eligible for this game", username)
    print("Read our Rules carefully")
    print("----------------------------------------------------------------")
    print("1. We have 10 question to ask you.")
    print("2. Each question has four options.")
    print("3. Questions will be asked one at a time.")
    print("4. If you provide the correct answer, you win ₹5,000.")
    print("5. If you answer incorrectly, the game ends.")
    print("6. If you answer all 10 questions correctly, you win ₹2,50,000.")
    print("7. After answering 6 questions correctly, you may either continue or quit with your winnings.")
    print("----------------------------------------------------------------")
    print("lets get start")

    correctQuestion = 0

    for i in range(len(questions)):
        print("------------------------------------------------------------")
        print(questions[i])
        ans = input("Enter option (A/B/C/D): ").upper()
        if ans == answers[i]:
            print("Correct")
            amount += 5000
            print(f"the current win amount is ₹{amount}")
            correctQuestion += 1

            if correctQuestion == 6:
                usercomment = input("""You have crossed the safe level.\n

Do you want to continue?\n

Type YES to continue\n
Type NO to quit\n""")
                if usercomment.lower() == "yes":
                    continue
                else:
                    print(f"You won the total amount of ₹{amount}")
                    print("Thank you for choosing us")
                    break

        else:
            print("Wrong answer!")
            print("Better luck next Time")
            print("Thank you for choosing us")
            break
    if correctQuestion == 10:
        print("--------------------------------------------------")
        print(f"Hey {username} Congrats! You are the winner of this KBC Game")
        print(f"You won the total amount of ₹{amount+winningAmount}")

else:
    print("You're not eligible! Thank you for choosing us", username)
