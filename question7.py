import array as arr

array1=arr.array('i')
for x in range(1,31):
    if x%3==0:
        array1.append(x)

print(array1)
