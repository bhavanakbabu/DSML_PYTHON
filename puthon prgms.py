#1.Write a script to get the largest number from a list
list1 =[10,15,20,56,84]
list1.sort()
print ("largest element is:",list1[-1])

#2.Write a program to remove duplicates from a list.
input_list =[1,1,4,5,5,6,7]
unique_list=[]
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

#3.Write a script to convert a tuple to a dictionary.
tuple_data = (('name','devu'),('age',23),('city','kkm'))
dict_data = dict(tuple_data)
print(dict_data)


#4.Write a script to merge two python dictionaries
d1={1:2,4:3,5:6}
d2={"a":"b","c":"b"}
d1.update(d2)
print(d1)


#5.Write a function that takes two lists and returns true if they have at least one common member
def common(11,12):
    for i in range(len(11)):
        for j in range(len(12)):
            if 11[i]==12[j]:
                return True

        
