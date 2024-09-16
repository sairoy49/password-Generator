import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Num = [0,1,2,3,4,5,6,7,8,9,]
symbols = ['!','@','$','%','^','#','&','+','-','*','(',')']
print("GET YOUR PASSWORD:")
password=[]  # list is taken to use3 shuffle fun in line 19
num_chosen=int(input("How Many Numbers Do You Need In Your Password?"))
for i in range(1,num_chosen+1):
    char = random.choice(Num)
    password += str(char) #the num converts to string as it not converted intially
letters_chosen=int(input("How Many Letters Do You Need In Your Password?")) 
for i in range(1,letters_chosen+1):
    char = random.choice(letters)
    password += char
symbol_chosen=int(input("How Many Symbols Do You Need In Your Password?")) 
for i in range(symbol_chosen+1):
    char = random.choice(symbols)
    password += char
random.shuffle(password)
password="".join(password) #join() fun used to concatenate elements of iterable.
print(password)
  