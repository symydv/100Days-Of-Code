# print num from 1 to 100 but num div by 3 will be called fizz ,num div but 5 called buzz, num div by both 5 and 3 called fizzbuzz


for num in range(1,101):

    if num%3 == 0 and num%5 == 0 :
        print("fizzbuzz")

    elif num%3 == 0 and num%5 != 0 :
        print("fizz")

    elif num%5 == 0 and num%3 != 0 :
        print("buzz")    

    else:
        print(num)   