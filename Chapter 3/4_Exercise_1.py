#Nested if else
win_number=27
user_input=input("Guess a number between 1 to 100")
user_input=int(user_input)
if user_input==win_number:
    print("YOu WIN !!!")
else:
    if user_input < win_number:
        print("Too Low")
    else:
        print("Too High")