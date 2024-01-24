import random
import sys
size=int(input("enter a size between 1 to 10:"))
list=[]
def random_generator(size):
    for x in range(size):
            rn=random.randint(100,500)
            list.append(rn)
    print(list)  
       
if size>0 and size<=10:
     random_generator(size)
     print("array created") 
  
else:
    i=1
    while i < 3:
        size=int(input("enter a size between 1 to 10 again:"))
        i=i+1
        if size>0 and size<=10:
            random_generator(size)
            
    else:
        sys.exit("enter a corrct value")        
        
    

             
        

            
              


    


    