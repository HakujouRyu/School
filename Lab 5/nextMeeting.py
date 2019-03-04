todaysInt = 8
while todaysInt < 0 or todaysInt > 7:
    try:
        todaysDay = input("Assuming Sunday = 0, and Saturday = 6, please enter the day of the week: ")
        todaysInt = int(todaysDay)
    except ValueError:
        if todaysDay == "help":
            print("Monday 0")
            print("Tuesday 1")
            print("Wednesday 3")
            print("Thursday 4")
            print("Friday 5")
            print("Saturday 6")
            todaysInt = 8
        else:
            print("Error: Please enter valid day code.")
            print("Type 'help' to see day codes.")
            todaysInt = 8
daysLeft = int(input("How many more days until your next meeting? "))
meetingDay = ((todaysInt + daysLeft) % 7)
dict = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
todaysInt = dict[todaysInt]
meetingDay = dict[meetingDay]
print("Today is ", todaysInt, ".", sep='')
print("You have ", daysLeft, " until your next meeting. ", sep= '')
print("Meeting Day is ", meetingDay, ".", sep='')
