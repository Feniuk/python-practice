# import random

# peeks = ["rock", "paper", "scissors"]
# rounds = 1
# max_rounds = 3

# while True:
#     try:
#         if rounds > max_rounds:
#             raise ValueError("You exceeded the round counts!")

#         print(f"Round {rounds}")

#         computer = random.choice(peeks)
#         me = random.choice(peeks)

#         print(f"Computer: {computer}")
#         print(f"Me: {me}")

#         if computer == me:
#             print("Draw")
#         elif (computer == "rock" and me == "paper") or \
#              (computer == "paper" and me == "scissors") or \
#              (computer == "scissors" and me == "rock"):
#             print("Me won")
#         else:
#             print("Me lose")

#         play_again = input("Would you like to play again? (yes/no): ").strip().lower()
#         if play_again != "yes":
#             print("Game finished hehe")
#             break

#         rounds += 1

#     except ValueError as e:
#         print(e)
#         print("Game over!")
#         break


def example_function(numbers):
    for x in numbers:
        print(x)

example_function(12, 45, 65, 78, 91)



