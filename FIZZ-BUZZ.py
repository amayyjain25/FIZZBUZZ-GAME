#fizz buzz
n= int(input("ENTER A NO."))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"is","FIZZBUZZ")
    elif i % 3 == 0:
        print(i,"is","FIZZ")
    elif i % 5 == 0:
        print(i,"is ",'BUZZ')
    else:
        print(i)