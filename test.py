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


# def example_function(numbers):
#     for x in numbers:
#         print(x)

# example_function(12, 45, 65, 78, 91)


# def multiply_list(numbers):
#     total = 1
#     for n in numbers:
#         total *= n
#     return total


# some_list =  [18, 0, 0] 
# magic = multiply_list(some_list) 
# print(magic) 


"""Enqueue"""

existing_queue = [1, 2, 3, "mom", 12]

MAX_SIZE = 6

class QueTask:
    try:
        if len(existing_queue) >= MAX_SIZE:
            raise Exception("My man, array is full")
        else:
            user_input = input("Enter anything: ")
            enque = existing_queue.insert(0, user_input)
            print(existing_queue)
    except Exception as e:
            print("Error caught:", e)


"""Dequeue"""

some_queue = [1]
class DeQUE:
    try:
        if len(some_queue) < 1:
            raise Exception("Ay Ay Ay, The Queue is empry")
        else:
            deque = some_queue.pop(0)
            print("Item deleted", some_queue)
    except Exception as sad:
        print("Error found: ", sad)