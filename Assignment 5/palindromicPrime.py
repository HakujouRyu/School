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


def is_prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True


i = 0
j = 1
counter = 0

while i < 50:
    if  reverse(j) is True and is_prime(j) is True:
        print(j, end='\t')
        i += 1
        counter += 1
        if counter % 10 == 0:
            print()
    j += 1
