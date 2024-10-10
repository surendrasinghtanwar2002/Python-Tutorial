                                                ## In this section we will practise some concepts used by programmer in classes ##

class Employee:
    def setname(self,nm):                    ##Setter Method
        self.name = nm
    
    def getname(self):
        return f"Hello Mr {self.name}"
    
##creating the first instance
e1 = Employee()
e1.setname(nm="Surendra")
print(e1.getname())

print(e1.__dict__)

##creating the second instance
e2 = Employee()
e2.setname(nm="Lokendar")
print(e2.getname())

print(e2.__dict__)

