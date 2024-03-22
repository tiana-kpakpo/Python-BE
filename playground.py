## build an app that accepts a number of students scores and calculate the sum of it
# scores: str = input("Enter scores separated by a single space: ")
# scores_in_str: list[str] = (scores.split(" "))
# scores_in_int: list[int] = []
# for score in scores_in_str:
#     scores_in_int.append(int(score))
# print("Your scores: ", scores_in_int)
# print(" Total score is:", sum(scores_in_int))

# build a system that accepts the months in numbers and based on the input print the name of the month. 

months = {
    "1": "January", "2": "February", "3": "March",
    "4": "April", "5": "May", "6": "June",
    "7": "July", "8": "August", "9": "September",
    "10": "October", "11": "November", "12": "December"
}

answer = input("Enter the number of your preferred month (1-12): ")

# if answer in months:
if answer.isdigit() and 1 <= int(answer) <= 12:
    print("The month is:", months[answer])
else:
    print('Enter a valid number between 1-12')


# name = input("Name of Student: ")
# print(f"Your name is {name}")

# answer = input("What is the capital of Ghana?")

# if answer.upper() == "Accra".upper():
#     print("Good job ")
# else: 
#     print("Naaaahhhh, wrong answer")