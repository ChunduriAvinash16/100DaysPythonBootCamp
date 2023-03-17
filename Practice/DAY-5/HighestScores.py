
student_scores = input("Input a list of student's score").split()
print(student_scores)
for i in range(0,len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)
#print(max(student_scores))
highest_score = student_scores[0]
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print(f"The heighest score in the class is: {highest_score}")