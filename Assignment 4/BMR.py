# Set variables to force loops.
sentinel = True
height = "loop"
weight = "loop"
age = "loop"
gender = "loop"
exercise = "loop"
exArray= [0, 1.2, 1.375, 1.55, 1.725, 1.9]
print("Welcome! Type \"exit\" anytime to terminate program!")
# Encapsulate script in while, so that we can terminate anytime.
while sentinel is True:
    # separate loops for each input. All with an escape word.
    while height == "loop" and sentinel is True:
        height = input("Please enter your height in inches: ")
        try:
            height = int(height)
        except ValueError:
            if height == "exit":
                sentinel = False
            else:
                print("Please enter a numerical value!")
                height = "loop"
    while weight == "loop" and sentinel is True:
        weight = input("Please enter your weight in pounds: ")
        try:
            weight = int(weight)
        except ValueError:
            if weight == "exit":
                sentinel = False
            else:
                print("Please enter a numerical value!")
                weight = "loop"
    while age == "loop" and sentinel is True:
        age = input("Please enter your age: ")
        try:
            age = int(age)
        except ValueError:
            if age == "exit":
                sentinel = False
            else:
                print("Please enter a numerical value!")
                age = "loop"
    while gender == "loop" and sentinel is True:
        gender = input("Please enter your gender [M/F]")
        if gender == "M" or gender == "m" or gender == "F" or gender == "f":
            continue
        elif gender == "exit":
            sentinel = False
        else:
            print("Please enter only \"M\" or \"F\" ")
            gender = "loop"
    while exercise == "loop" and sentinel is True:
        print("Please select an option below: \n"
              "1.   You don't exercise.\n"
              "2.   You engage in light exercise one to three days a week.\n"
              "3.	You exercise moderately three to five times a week.\n"
              "4.	You exercise intensely six to seven days a week.\n"
              "5.	You exercise intensely six to seven days a week and have a physically active job.")
        exercise = input("Your selection: ")
        print()
        try:
            exercise = int(exercise)
            if exercise < 1 or exercise > 5:
                print("Please enter a number 1-5!")
                print()
                exercise = "loop"
            else:
                continue
        except ValueError:
            if exercise == "exit":
                sentinel = False
            else:
                print("Please enter a number 1-5!")
                exercise = "loop"
    # start calculations and print results
    if gender == "m" or gender == "M" and sentinel is True:
        BMR = 66+(6.23 * weight) + (12.7 * height) - (6.8 * age)
        DCA = BMR * exArray[exercise]
        print("Your Results:\n"
              "Male, ", height, "\", ", weight, "lbs, ", age, "years old, BMR = ", BMR,
              ", Exercise: ", exercise, ", DCA:", DCA, sep='')
        print(exArray[exercise])
    elif gender == "f" or gender == "F" and sentinel is True:
        BMR = float(655+(4.35 * weight) + (4.7 * height) - (4.7 * age ))
        DCA = float(BMR * exArray[exercise])
        print("Your Results:\n"
              "Female, ", height, "\", ", weight, "lbs, ", age, "years old, BMR = ", BMR,
              ", Exercise: ", exercise, ", DCA:", DCA, sep='')
        print(exArray[exercise], height, weight, age)
    # prepwork for next iteration
    if sentinel is True:
        print()
        print()
        print("Next user:")
        print()
        print()
        height = "loop"
        weight = "loop"
        age = "loop"
        gender = "loop"
        exercise = "loop"
else:
    print()
    print("Thanks for using this program, Goodbye!")
