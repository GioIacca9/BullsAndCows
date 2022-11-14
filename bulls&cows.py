from random import randint
import timeit
class Number:
    # generate random number
    def __init__(self, length):
        self.__number = []
        self.__number.append(randint(0, 9))
        while True:
            if self.getLength() != int(length):
                self.a = randint(0, 9)
                if self.a not in self.__number:
                    self.__number.append(self.a)
                else:
                    continue
            else:
                break

    # return the lenght of the number
    def getLength(self):
        return len(self.__number)

    # print the number
    def __str__(self):
        return f"{self.__number}"

    def __getitem__(self, index):
        return self.__number[index]

    # a number of correct numbers in the right place
    # b number of correct numbers in the wrong place
    def ceckMyNumber(self, myNumberInt):
        myNumber = []
        for i in range(self.getLength()):
            myNumber.append(int(myNumberInt[i]))
        a = 0
        b = 0
        for i in range(len(self.__number)):
            if self.__number[i] == myNumber[i]:
                a += 1
            elif self.__number[i] in myNumber:
                b += 1
        return a, b

class game:

    while True:
        # generete random number length = 4
        number = Number(4)
        #set the counter to 0
        counter = 0
        # ask the user to guess the number
        print("Number has been generated u can try to guess it")
        # start the timer, check the user's number
        start = timeit.default_timer()
        while True:
            myNumber = input("Enter your number: ")
            # check if the nuber is a number and if it is the right lenght
            if len(myNumber) != number.getLength():
                print("Your number is not the right lenght")
                continue
            elif not myNumber.isdigit():
                print("Your number is not an integer")
                continue
            else:
                counter += 1
                a, b = number.ceckMyNumber(myNumber)
                if a == number.getLength():
                    stop = timeit.default_timer()
                    print("You won in", counter, "tries" + " in " + str(round(stop-start, 2)) + " seconds")
                    break
                else:
                    print(f"You have {a} bulls and {b} cows")

