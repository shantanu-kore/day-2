def reverse(str):
    ans=''
    for x in str:
        ans=x + ans
    print(ans)
str=input("Enter a string:")
reverse(str)