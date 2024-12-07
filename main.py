class Student:
    def __init__(self, name):
      self.name = name
      self.progress = 0
      self.energy = 50

    def show_info(self):
       print(f"Name: {self.name}, progress: {self.progress}, energy: {self.energy}")

    def sleep(self):
       print("Sleeping")
       self.energy += 15

    def study(self):
       print("Studing")
       self.progress += 0.5
       self.energy -= 5

    def chill(self):
       print("chilling")
       self.energy += 10
       self.progress -= 0.2

    


      


student = Student("Nikita")

student.show_info()

student.study()
student.chill()
student.sleep()

student.show_info()