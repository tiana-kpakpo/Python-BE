# build a system that accepts the months in numbers and based on the input print the name of the month. 


months = {
    "1": "January", "2": "February", "3": "March",
    "4": "April", "5": "May", "6": "June",
    "7": "July", "8": "August", "9": "September",
    "10": "October", "11": "November", "12": "December"
}

while True:
    answer = input("Enter the number of your preferred month (1-12): ")
    
    if answer.isdigit() and 1 <= int(answer) <= 12:
        print("The month is:", months[answer])
        break
    else:
        print('Enter a valid number between 1-12')
