class TestQuestion():
    def __init__(self, Q = "What is 2 + 2?", A = "4"):
        self.question = Q
        self.answer = A

    def __str__(self):
        print(self.question)
        print(self.answer)


    def CheckAnswer(self):
        if input(self.question) == self.answer:
            return True
        else:
            return False

checking = TestQuestion()
# checking.__init__()
# checking.__str__()
# checking.CheckAnswer()
Q = input('Please enter a test question (or just hit enter to skip):')
A = input('Please enter the answer to that question (or just hit enter to skip):')
while True:
    if Q != '' and A != '':
        checking.__init__(Q, A)
    else:
        checking.__init__()

    key = checking.CheckAnswer()
    if key is True:
        Q = input('You are the new champion. Claim your prize by setting a new more difficult question: ')
        if Q == 'quit':
            break
        A = input('And the answer to that question: ')
        checking.__init__(Q, A)
    if key is False:
        print("Sorry Try Again.")

