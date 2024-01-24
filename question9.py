import random
array=[]
sum=0
for x in range(1,76):
    random_Num=random.randint(1,100)
    array.append(random_Num)
    sum=sum+random_Num

average=sum/75

print("array is:",array)
print("sum of elements if array is:",sum)
print("average of array is:",average)
