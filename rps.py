import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game = [rock, paper, scissors]
user_choice = input("Type: 0 - Rock, 1 - Paper or 2 - Scissors: ")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
computer_choice = random.choice(game)
print(f"computer choose:\n {computer_choice}")
if computer_choice == rock and user_choice == "2":
    print(" computer won ")
elif computer_choice == scissors and user_choice == "1":
    print(" computer won ")
elif computer_choice == paper and user_choice == "0":
    print(" computer won ")
elif user_choice == "2" and computer_choice == rock:
    print(" you won ")
elif user_choice == "1" and computer_choice == scissors:
    print(" you won ")
elif user_choice == "0" and computer_choice == paper:
    print(" you won ")
else:
    print("It's a draw")
