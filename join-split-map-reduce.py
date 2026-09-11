#split
# data="I am well developer"
# words=data.split()
# print(words)


#joins - opposite to split

# data=["I","am","well","developer"]
# delimiter=" "
# sentence=delimiter.join(data)
# print(sentence)


#filter
# a=[1,2,3,4,5,6,7,8,9]
# b=[1,2,4,5,3,2,5,6,6]
# result=list(filter((lambda x:x not in b),a))
# print(result)


#map

# numbers=[1,2,3,4,5]
# res=list(map((lambda x:x**3),numbers))
# print(res)

from functools import reduce
x=[1,2,3,4,5,6]

result=reduce((lambda x,y:x*y),x)
print(result)