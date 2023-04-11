
print("Welcome to the True Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_name1 = name1.lower()
lower_name2 = name2.lower()

true_count1 = lower_name1.count("t")+lower_name1.count("r")+lower_name1.count("u")+lower_name1.count("e")
true_count2 = lower_name2.count("t")+lower_name2.count("r")+lower_name2.count("u")+lower_name2.count("e")
true_sum = true_count1 + true_count2
love_count1 = lower_name1.count("l")+lower_name1.count("o")+lower_name1.count("v")+lower_name1.count("e")
love_count2 = lower_name2.count("l")+lower_name2.count("o")+lower_name2.count("v")+lower_name2.count("e")
love_sum = love_count1 + love_count2
score = int(str(true_sum)+str(love_sum))
if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score<= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")