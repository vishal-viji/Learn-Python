'''
mystr="GUVI is an IIT-M & IIM-A incubated Ed-tech company"
# positive slicing
print(mystr[25:34])
#negative slicing
mystr="GUVI is an IIT-M & IIM-A incubated Ed-tech company"
print(mystr[-25:-16])
#negative slicing
mystr="GUVI is an IIT-M & IIM-A incubated Ed-tech company"
print(mystr[-7:])

mystr="GUVI is an IIT-M & IIM-A incubated Ed-tech company "
print(mystr[0:27:26])
print(mystr[0:50:49])

# a) Take the student's name
name = input("Enter student's name: ")

# b) Take marks
english = float(input("Enter English marks: "))
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
social = float(input("Enter Social marks: "))
kannada = float(input("Enter Kannada marks: "))
hindi = float(input("Enter Hindi marks: "))

# c) Add total marks
total = english + maths + science + social + kannada + hindi
print("Total marks:", total)

# d) Print average
average = total / 6
print("Average:", average)

# e) Add language marks and print average
language_total = english + kannada + hindi
language_average = language_total / 3
print("Languages average:", language_average)

# f) Add core subject marks and print average
core_total = maths + science + social
core_average = core_total / 3
print("Core subjects average:", core_average)
'''

# problem 2


# mynum=[1,2,3,4,5]
# total=0
# for i in mynum:
#     total = total + i
# print(total)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# mylist = [1, 2, 2, 3, 4, 2, 5, 2]

# reverse_list = []

# for i in range(len(mylist) - 1, -1, -1):
#     reverse_list.append(mylist[i])

# print(reverse_list)



# # string slicing positive
# mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# # print(mylist[6:9])
# # print(mylist[9:15])
# # print(mylist[5:])
# # print(mylist[12:])
# # print(mylist[12::2])
# # print(mylist[3:10:2])
# # print(mylist[6::4])
# # negative string slicing
# print(mylist[-7::2])
# print(mylist[-16:-9:2])
# print(mylist[-13::4])
# print(mylist[-13:-7])






# meghna=input()
# if(meghna=="died"):
#     print("RIP")
# else:
#     print("alive")




