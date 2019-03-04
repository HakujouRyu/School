lgWeight = int(input("How many pounds does the big one weigh? "))
smWeight = int(input("How many pounds does the small one weigh? "))
lgPrice = int(input("How much does the big one cost? "))
smPrice = int(input("How much does the small one cost? "))
if (lgPrice / lgWeight) < (smPrice / smWeight):
     print("Large box is better deal.")
elif (lgPrice / lgWeight) > (smPrice / smWeight):
     print("Small box is better deal.")
elif (lgPrice / lgWeight) == (smPrice / smWeight):
     print("Both are the same value!")
