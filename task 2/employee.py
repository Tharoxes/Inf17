from vehicle import *
from customer import *

class Employee(object):
    ######## CODE MISSING HERE

    def __init__(self, name):
        pass
    ######## CODE MISSING HERE

    def __str__(self):
        pass
    ######## CODE MISSING HERE

    def get_name(self):
        pass
    ######## CODE MISSING HERE
    
    def get_title(self):
        pass
    ######## CODE MISSING HERE
    
class Manager(Employee):

    def get_title(self):
        pass
    ######## CODE MISSING HERE

    def get_sales_report(self,salesman):
        pass
    ######## CODE MISSING HERE

class Salesman(Employee):

    ######## CODE MISSING HERE

    def sale(self,vehicle,sales_price,customer):
        pass
    ######## CODE MISSING HERE


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

# print(Eric) # expected output: Employee: Eric is of type Manager
# print(Kyle) # expected output: Employee: Kyle is of type Subordinate
# print(Stan) # expected output: Employee: Stan is of type Subordinate
# print(Kenny) # expected output: Employee: Kenny is of type Subordinate
# print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

# Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000
