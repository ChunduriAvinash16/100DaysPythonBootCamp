
student_heights = input("Input s list of student heights ").split()
print(student_heights)
for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)

sum_of_heights = 0
count = 0
for height in student_heights :
    sum_of_heights += height
    count += 1
# print(sum_of_heights)
# print(count)
# print(sum_of_heights / count)
average = round(sum_of_heights / count)
print(average)