print("Welcome to Love Calculator!")
fname = input("What is your name ?\n ")
lname = input("What is their name?\n ")
name = fname+lname;
name_lower = name.lower();
true_count = name_lower.count('t')+name_lower.count('r')+name_lower.count('u')+name_lower.count('e')
love_count = name_lower.count('l')+name_lower.count('o')+name_lower.count('v')+name_lower.count('e')
fscore = true_count * 10 + love_count
if fscore<10 or fscore>90:
    print(f"Your score is {fscore}, you go together like coke and mentos.")
elif 40 < fscore < 50:
    print(f"Your score is {fscore}, you are alright together.")
else:
    print(f"Your score is {fscore}.")

print(fname)