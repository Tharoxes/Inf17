from moduleElement import *

class Module(object):

    counter = 0
    # I'm a bit confused, for my comprehension in task 1a) is to create a class withing a
    # class and by creating Module, the counter of the module_count increase, right?
    # It was clear when I saw the test case, but I prefer to ask for safety
    # I don't know how to count by a class variable, my solution for counting modules
    # is not a real solution. I use a method instead a class variable
    # I may work with "if __name__ == __main__"-statements or the solution is so simple
    # I haven't seen it
    def module_count(self):
        Module.counter += 1


    def __init__(self,ects,title,semester,grade=None):
        "constructor for class module"

        self.ects = ects
        self.grade = grade
        self.title = title
        self.semester = semester

        self.dates = []

        self.elements = []

        ######## CODE MISSING HERE


    def get_important_dates_overview(self):
        "prints all the important dates for a module"

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind,date))


    def set_grade(self,grade):
        "set the grade to a given value"

        self.grade = grade


    def add_module_element(self,other_class,date):
        "add a new module element to the elements list"

        obj = other_class(self)
        obj.add_important_date(date)
        self.elements.append((obj))

    def get_title(self):
        return self.title


    def get_grade(self):
        return self.grade


#########################################################################

class Course(Module):

    def __str__(self):
        return "Course: " + Course.get_title(self)

#########################################################################

class Seminar(Module):

    # for the classes "Seminar" and "Thesis" I've got the dubiety, what does the unfilled
    # parameters mean, because, if I try to fix it and insert ",ects,title,semester," in
    # parent class parameters, it's fixed, BUT there's a conflict with the arguments section
    # below in the test cases
    # thank you for response
    def __init__(self,ects,title,semester, topic):
        Module.__init__(self,grade)
        self.ects = ects
        self.title = title
        self.semester = semester
        self.topic = topic
    
    def __str__(self):
        return "Seminar in " + Seminar.get_title(self) + "under the topic:" + Seminar.get_topic(self)

    def get_topic(self):
        return self.topic

#########################################################################


class Thesis(Module):

    def __init__(self, ects, title, semester,  topic, research_group):
        Module.__init__(self,grade)
        self.ects = ects
        self.title = title
        self.semester = semester
        self.topic = topic
        self.research_group = research_group
    
    def __str__(self):
        return Thesis.get_title(self) + " on the topic " + Thesis.get_topic(self) + "in the Research Group " + \
               Thesis.get_research_group(self)

    def get_topic(self):
        return self.topic

    def get_research_group(self):
        return self.research_group


#########################################################################

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grade = {}

    def add_module(self, Module):
        self.modules.append(Module)
        self.grade[Module] = Module.get_grade()

    def get_list_modules(self):
        for module, grade in self.modules:
            print(module)

    def get_grades(self):
        for module, grade in self.modules:
            print(modules + ": " + grade)


Student = Student(Erik)

### test cases ###

info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()
# print(info1)
# expected output:
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
math1.get_important_dates_overview()
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


# print(Module.module_count)
# expected output: 2

thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
# print(thesis)
# expected output:
# Bachelor Thesis on the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
# print(sem)
# print(thesis)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)
