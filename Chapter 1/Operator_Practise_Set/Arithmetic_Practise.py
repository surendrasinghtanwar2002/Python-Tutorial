# Operator precedence with associativity (PEMDAS)

#(1) Basic Arithmetic operation:

#First question 3+5×2
first_Value = 3
second_value = 5
third_Value = 2
print(first_Value+second_value*third_Value) #Output will be 13

#Second Question 8/4*2
first_no = 8
second_no = 4
third_no = 2
print(first_no/second_no * third_no) #Output will be 4.0

#Third Question 5+4-3*2
first_a = 5
second_a = 4
third_a = 3
fourth_a = 2
print(first_a+second_a-third_a*fourth_a) #output will be 3

#Fourth Question 10-3+2*2
first_b = 10
second_b = 3
third_b = 2
fourth_b = 2
print(first_b-second_b+third_b*fourth_b) #output will be 11

#(2) Mixed Arithmetic Operation:

#First Question 4+3×2−1
first_c = 4
second_c = 3
third_c = 2
fourth_c = 1
print(first_c+second_c*third_c-fourth_c) #output will be 9

#Second Question 7+3*(6/2)
first_d = 7
second_d = 3
third_d = 6
fourth_d = 2
print(first_d+second_d*(third_d/fourth_d))

#Third Question 7+3/(6*2)
first_e = 7
second_e = 3
third_e = 6
fourth_e = 2
print(first_e+second_e/(third_e*fourth_e))

#Fourth Question (8+2)*5 - 3
first_f = 8
second_f = 2
third_f = 5
fourth_f = 3
print(first_f+second_f*third_f-fourth_f)

#Fifth Question 6/3+4*2
first_g = 6
second_g = 3
third_g = 4
fourth_g = 2
print(first_g/second_g+third_g*fourth_g)

#(3) Parenthesis and Nesting

#First Question (3+5)*2
first_h = 3
second_h = 5
third_h = 2
print((first_h+second_h)* third_h)

#Second Question (4+2)*(3-1)
first_i = 4
second_i = 2
third_i = 3
fourth_i = 1
print((first_i+second_i)*(third_i-fourth_i))

#Third Question 5*(3+(2-1))
first_j = 5
second_j = 3
third_j = 2
fourth_j = 1
print(first_j*(second_j+(third_j-fourth_j)))

#Fourth Question (7+3)*(6/2)
first_k = 7
second_k = 3
third_k = 6
fourth_k = 2
print((first_k+second_k)*(third_k/fourth_k))

