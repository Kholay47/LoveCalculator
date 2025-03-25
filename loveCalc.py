from simple_colors import*

print("\nWelcome to Kholay Maharaj's LOVE CALCULATOR");
print("\n");
name_1=input("Please enter your name: ");
print("\n");
name_2=input("Please enter your partner's name: ");
print("\n");

combined_names= name_1+name_2;
lower_names=combined_names.lower();

t=lower_names.count("t");
r=lower_names.count("r");
u=lower_names.count("u");
e=lower_names.count("e");

first_digit= t+r+u+e;

l=lower_names.count("l");
o=lower_names.count("o");
v=lower_names.count("v");
e=lower_names.count("e");

second_digit= l+o+v+e;

score=int(str(first_digit)+str(second_digit));
# score=str(first_digit)+str(second_digit);
# check=int(score);

if score<10 or score>90:
    print(f"Your score is {score}% and You both are like coke and mentos!!\n");
elif score>=40 and score<=50:
    print(f"Your score is {score}% and You both are alright together\n");
else: print(f"Your score is {score}%\n");