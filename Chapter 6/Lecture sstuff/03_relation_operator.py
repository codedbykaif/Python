a = int(input("Enter your age: "))
# if statement no 1: 
if(a%2 ==0 ):
  print("a is even")
  # end of statement no 1:


# if statement no 2:
if(a>18):
  print("you are above the age of conscent")
  print("Good for you")
  
elif(a<0):
  print("You are enterning an invalid age ")

elif(a==0):
  print("You are entering 0 which is a invalid age")
  
else:
  print("you are below the age of conscent")
  # end of statement no 2:
  
print("End of program")