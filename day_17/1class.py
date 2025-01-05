class User:    #(in class name we use first letter of its every word capital eg: class MyNanmeIsShyam)
    def __init__(self,user_id,username) : #(with the help of init we can add parameters in class, but then whenever we get new user of class we also have to pass those parameters there also)
        self.id=user_id    
        self.username = username
        self.followers = 0 #(we didnt mentioned followers in init as  it has a constant value which will e common value for all objects created from this class)
        self.following = 0

    def follow(self, user): #it is defined as a method when self follows user
        user.followers +=1
        self.following +=1

user0 = User("000","ramesh")
user_2=User("002","raju")
user_1=User("001","angela")


user_1.follow(user_2)
print(user0.id)
print(user0.username)
user0.followers+=1
print(user0.followers)
print(user_1.id,user_1.username)  #(this are the attributes)
print(user_1.followers,user_1.following)
print(user_2.id,user_2.username)
print(user_2.followers,user_2.following)





# if we leave our class empty we can give attributes during naming of our variables(attribute:the things that an object has)

class Fruit:
    pass  #this will make an empty class

mango = Fruit()
mango.price = "20"
mango.season = "summer"

apple = Fruit()
apple.price = "25"
apple.season = "winter"

print(apple.price)
print(mango.season)
