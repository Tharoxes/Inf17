from vehicle import *


class Customer(object):
    
    def __init__(self,name):
        pass
    ######## CODE MISSING HERE

    def __str__(self):
        pass
    ######## CODE MISSING HERE

    def credit_score(self):
        pass
    ######## CODE MISSING HERE

    def get_score(self):
        pass
    ######## CODE MISSING HERE


class VIP_Customer(Customer):

    def credit_score(self):
        pass
    ######## CODE MISSING HERE


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

# print(Wendy) # expected output: Customer: Wendy
# print(Heidi) # expected output: Customer: Heidi

# print(Wendy.get_score()) # expected output: True
# print(Heidi.get_score()) # expected output: True
