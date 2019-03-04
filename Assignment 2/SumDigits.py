userInput = int(input("Please enter a number between 0 and 1000: "))
if userInput > 1000:
    print("Please Try again")
total = 0
while userInput > 0:
    total = total + (userInput % 10)
    userInput = userInput // 10
print(total)