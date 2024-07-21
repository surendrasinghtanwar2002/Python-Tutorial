                                        ## Joining the list in python ##

##Concatenating two list in python using + operator (It will only concatenate same type of datatype like list to list)

#Approach 1

list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = [110,120,130,140,150,160,170,180,190,200]
list3 = list1+list2
print(list3) #Adding or Concatenating two list using + operator

#Approach 2
list4 = [210,220,230,240,250,260,270,280,290,300]
list5 = [310,320,330,340,350,360,370,380,390,400]
list6 = list4+list5
print(len(list6))
list6[0:4] = [10]
print(f"This is length of the list {len(list6)} and this is original list",list6)

#Approach 3 
# list7 = [10,20,30,40,50,60,70,80,90,100]
# list8 = (110,120,130,140,150,160,170,180,190,200)
# list9 = list8+list7 ##give error because + operator can only Concatenate with same type of datatype
# print(list9)

##Extend() method is being used to add any list,tuple or set to list 

#Approach 1
list7 = [10,20,30,40,50,60,70,80,90,100]
list8 = [110,120,130,140,150,160,170,180,190,200]
list7.extend(list8)
list9 = list7
print(list9)

#Approach 2
list10 = [210,220,230,240,250,260,270,280,290,300]
list11 = [310,320,330,340,350,360,370,380,390,400] 
print(len(list10)) ##It is the previous length of the list 
print(len(list11)) ##It is previous length of the list 
list10.extend(list11)
print(f"This is the new list 10 size {len(list10)}, and this is real list {list10}")