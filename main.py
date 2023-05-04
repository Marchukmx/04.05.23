#Класи

class student:
    print("Hi!")
    count = 0
    def __init__(self, height = 150):
        self.heigth = height
oleg = student()   # Олег відноситься до Student
print(oleg.heigth)
masha = student(height = 200)
print(masha.heigth)