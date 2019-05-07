class student:

    def __init__(self, name,branch,id):
        self.name = name
        self.branch = branch
        self.id = id
    def __repr__(self):
        return self.name + ',' + self.id + ',' + self.branch
    def isstudent_wise(self):
        return False
class student_wise(student):
    def isstudent_wise(self):
        return True
x = student_wise("Soumya","EEE","18B01A0234")
y = student('Anusha','EEE','18B01A0246')
'''
print(y.__repr__(),y.isstudent_wise())
print(x.__repr__(),x.isstudent_wise())'''

