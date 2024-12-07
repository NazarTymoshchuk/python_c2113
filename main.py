class Student:
    def __init__(self, name):
      self.name = name
      self.progress = 0
      self.energy = 50

    def show_info(self):
       print(f"Name: {self.name}, progress: {self.progress}, energy: {self.energy}")
      


student = Student("Nikita")

student.show_info()