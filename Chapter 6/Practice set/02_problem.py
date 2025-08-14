# take input of marks from user
marks1 = int(input("Enter marks of sub1: "))
marks2 = int(input("Enter marks of sub2: "))
marks3 = int(input("Enter marks of sub3: "))

# check for total percentage
total_percentage =(100)*(marks1 + marks2 + marks3)/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
  print("You have passed the exam, and your total percentage is: ", total_percentage)

else:
  print("You have failed the exam, try again and you total percentage is: ", total_percentage)  