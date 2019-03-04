import random
randomThing = []
for counter in range(10):
    randomThing.append(random.randint(1, 50))

randomPrint = '' .join(str(randomThing))
print("random numbers between 50 and 100: ", randomPrint)
