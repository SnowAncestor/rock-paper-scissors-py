import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# طلب الاختيار من المستخدم
x = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# عرض اختيار المستخدم
if x == 0:
    print(rock)
elif x == 1:
    print(paper)
elif x == 2:
    print(scissors)
else:
    print("Wrong input")
    exit()

# اختيار الكمبيوتر عشوائيًا
print("Computer chose: ")
computer = random.randint(0, 2)

# عرض اختيار الكمبيوتر
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

# تحديد الفائز
if x == computer:
    print("It's a tie!")
elif (x == 0 and computer == 2) or (x == 1 and computer == 0) or (x == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")












