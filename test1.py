class MyClass :
    def __init__(self,name,age):
        self.name=name
        self.age=age
     
    def clas(self, skills):
        print(self.name,"and", self.age)
        self.skills=skills
    def getclass(self):
        print("skill",self.skills)
p1=MyClass("Huynh",18)
p1.clas("Good Teamwork")
p1.getclass()            

