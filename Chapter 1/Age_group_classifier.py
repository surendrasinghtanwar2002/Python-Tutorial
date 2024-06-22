#In this section we will create a age group classifier to find the student age
a= int(input("Enter your age please= "))
if (a>=0 and a<=12):
    print("You are a child")
elif (a>=13 and a<=19):
    print("You are a teenager")
elif (a>=20 and a<=64):
    print("You are adult")
elif (a>=65 and a<=120):
    print("You are a senior citizen of our country")
elif (a<=0):
    print("You have given a negative which is not valid")
else:
    print("You have not given a valid number")