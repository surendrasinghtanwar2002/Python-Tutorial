                                        ## In this section we will practise the multilevel inheritance in python ##


##This is the base class or Parent Class
class Grandparent:
    def __init__(self) -> None:
        self.grandparent_attr= "I am grandparent"
        print("Calling the Grandparent class constructor")
    
    def showgrandparent(self):
        print(self.grandparent_attr)
    
##This is child class
class Parents(Grandparent):
    def __init__(self) -> None:
        super().__init__()          ##It will call the grand parent constructor
        self.parrent_attr= "I am parrent"
        print("Calling the parrent class constructor")
    
    def showparent(self):
        print(self.parrent_attr)

##This is another child class
class Child(Parents):
    def __init__(self) -> None:
        super().__init__()              ##Call the parrent constructor
        self.child_attr = "I am Child"
        print("Calling the child class constructor")
    
    def showchild(self):
        print(self.child_attr)


###Creating the instance
child_instance = Child()

print(child_instance.child_attr)
print(child_instance.parrent_attr)
print(child_instance.grandparent_attr)