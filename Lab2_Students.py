from dataclasses import dataclass ## as it's clear using dataclass makes the app much simpler and requires less codes and confisuon x
@dataclass
class Students:
   # def __init__(self, name, school_id, gpa): # __init__ is special name and it diesn't change
      #  self.name = name
       # self.school_id = school_id
        #self.gpa = gpa
    name:str
    school_id:str
    gpa: float    

    def __str__(self):
         return f'Student name : {self.name}, ID: {self.school_id}, GPA: {self.gpa} '

def main():
        sam = Students('Sam','bbvfd32', '4.0') #this is just like the constracotr  that we did in JAVA
        print(sam.name)
        print(sam)
        alex = Students('Alex','bbvfd32', '3.5') 
        print(alex.name) #Alex
        print(alex.gpa) #3.5
        print(alex)

if __name__ == '__main__':
    main()
        