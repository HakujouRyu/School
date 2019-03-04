def reverse(x):
    reverseNum = 0
    original = x
    while x > 0:
        y = x % 10
        reverseNum = (reverseNum * 10) + y
        x = x // 10
    answer = is_palindrome(reverseNum, original)
    return answer


def is_palindrome(x, y):
    if x == y:
        return True
    else:
        return False


try:
    userIn = int(input("Please enter a number: "))
except ValueError:
    print("Please Try again!")
final = reverse(userIn)
print("Entered Value:", userIn)
print(final)
if final == True:
    print("Judgement: Palindrome")
else:
    print("Judgement: Not palindrome")