## In this section we will practise nested dictionaries in which we will create nested dictionaries 
## where we will create dictionary inside the dictionaries


# "First Method" basic dictionary methods to print specific dictionary object
student_information = {
    "student_1":{
        "Full_Name":"Surendra Singh Tanwar",
        "Father_Name":"Vikram Singh Tanwar",
        "Contact_No": 9460824001,
        "Email_Address": "surendrasinghtanwar667@gmail.com",
        "Current_Student": False
    },
    "student_2":{
        "Full_Name":"Krishna Tanwar",
        "Father_Name":"Vikram Singh Tanwar",
        "Contact_No": 9414911678,
        "Email_Address": "krishnatanwar2000@gmail.com",
        "Current_Student": False
    },
    "student_3":{
        "Full_Name":"Yogita Kanwar",
        "Father_Name":"Vikram Singh Tanwar",
        "Contact_No": 9057214045,
        "Email_Address": "vsntweb@gmail.com",
        "Current_Student": True
    },
    "student_4":{
        "Full_Name":"Kuldeep Singh Tanwar",
        "Father_Name":"Prem Singh Tanwar",
        "Contact_No": 8209269438,
        "Email_Address": "kuldeepsinghtanwar2005@gmail.com",
        "Current_Student": True
    },
    "student_5":{
        "Full_Name":"Ronak Kanwar",
        "Father_Name":"Prem Singh Tanwar",
        "Contact_No": 7727911260,
        "Email_Address": "ronakkanwar667@gmail.com",
        "Current_Student": True
    },
}
print(student_information["student_1"]["Full_Name"])
print(student_information["student_2"]["Full_Name"])
print(student_information["student_3"]["Full_Name"])
print(student_information["student_4"]["Full_Name"])
print(student_information["student_5"]["Full_Name"])


# "Second Method" which allow to create multiple dictionary and merge in single dictionary
student1 = {
    "Full_Name":"Surendra Singh Tanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com",
    "Course": "BCA",
    "Passout": 2024,
    "Current_Student_Status": False
},
student2 = {
    "Full_Name":"Kuldeep Singh Tanwar",
    "Father_Name": "Prem Singh Tanwar",
    "Mobile_no": 8209269438,
    "Email_Address": "kuldeepsinghtanwar667@gmail.com",
    "Course": "BA(Law)",
    "Passout": 2027,
    "Current_Student_Status": True
},
student3 = {
    "Full_Name":"Krishna Tanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Mobile_no": 9414384439,
    "Email_Address": "krishnatanwar2000@gmail.com",
    "Course": "MCOM",
    "Passout": 2024,
    "Current_Student_Status": False
},
student4 = {
    "Full_Name":"Ronak Kanwar",
    "Father_Name": "Prem Singh Tanwar",
    "Mobile_no": 8209214264,
    "Email_Address": "premsinghtanwar1975@gmail.com",
    "Course": "9th",
    "Passout": "On-goin",
    "Current_Student_Status":  True
},
student5 = {
    "Full_Name":"Yogita Kanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Mobile_no": 9057214045,
    "Email_Address": "vstnweb@yahoo.com",
    "Course": "6th",
    "Passout": "On-goin",
    "Current_Student_Status":  True
}
myfamilyeducation = {
    "child1": student1,
    "child2": student2,
    "child3": student3,
    "child4": student4,
    "child5": student5
}
print(myfamilyeducation["child1"])


