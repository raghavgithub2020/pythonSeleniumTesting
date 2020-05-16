# To inherit the chile class, we just need to call the parent class name into child class braces
from OopsDemo import Calculator

class ChildOops(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 10, 20)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildOops()
print(obj.getCompleteData())

