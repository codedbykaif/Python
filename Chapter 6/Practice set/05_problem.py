username = input("Enter your username: ")
if(len(username)<10):
  print("Your username contains less than 10 characters: ", username)

else:
  print("All is well: ", username)