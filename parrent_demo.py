class Calculator:
    num = 100 #class varible

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b

        print("I am called automatically when object is created")

    def get_data(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.first_number + self.second_number + Calculator.num


obj = Calculator(2, 3)
obj.get_data()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.get_data()
print(obj1.summation())
