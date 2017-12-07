from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        pass
        ######## CODE MISSING HERE

    def add_module(self,title):
        pass
        ######## CODE MISSING HERE

    def get_list_modules(self):
        pass
        ######## CODE MISSING HERE

    def get_grades(self):
        pass
        ######## CODE MISSING HERE


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
