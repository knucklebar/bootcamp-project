
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
name3 = name1 + name2 

t1 = name3.count("t")
r1 = name3.count("r")
u1 = name3.count("u")
e1 = name3.count("e")

l1 = name3.count("l")
o1 = name3.count("o")
v1 = name3.count("v")
e2 = name3.count("e")

left_final = t1+r1+u1+e1
right_final = l1+o1+v1+e2

final_score = f"{left_final}{right_final}"
final_score = int(final_score)

if final_score <10 and final_score>90:
  print(f"Your score is {final_score}, you go together like coke and mentos")
elif 40<final_score>50:
  print(f"Your score is {final_score}, you are alright together")
else:
  print(f"Your score is {final_score}")