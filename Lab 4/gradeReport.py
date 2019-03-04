grade = int(input("Please enter your grade: "))

if grade >= 100:
    print("That grade is a perfect score. Well done.")
elif grade < 100 and grade >= 90:
    print("That grade is well above average. Excellent work.")
elif grade < 90 and grade >= 80:
    print("That grade is above average. Nice job.")
elif grade < 80 and grade >= 70:
    print("That grade is average work.")
elif grade < 70 and grade >= 60:
    print("That grade is not good, you should seek help!")
elif grade < 60:
    print("That grade is not passing.")
