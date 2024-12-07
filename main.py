import random

class Student:
    def __init__(self, name):
      self.name = name
      self.progress = 0
      self.energy = 50
      self.alive = True

    def show_info(self):
      print(f"Name: {self.name}, progress: {round(self.progress, 2)}, energy: {self.energy}")

    def sleep(self):
      print("Sleeping")
      self.energy += 15

    def study(self):
      print("Studing")
      self.progress += 0.5
      self.energy -= 8

    def chill(self):
      print("chilling")
      self.energy += 10
      self.progress -= 0.3

    def is_alive(self):
      if self.energy <= 0:
        print("Overworked")
        self.alive = False

      if self.progress < -1:
        print("Cast out")
        self.alive = False

    def live(self, day):
      print(f"Day {day} of {self.name} life")

      student_choice = random.randint(1, 3)

      if student_choice == 1:
        self.study()
      
      elif student_choice == 2:
        self.chill()

      elif student_choice == 3:
        self.sleep()

      self.is_alive()
      self.show_info()

   
student = Student("Nikita")

for day in range(365):
  if student.alive == False:
    break
  student.live(day)