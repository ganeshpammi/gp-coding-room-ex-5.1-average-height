# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height = 0
student_count = 0
for each_height in student_heights:
    height += each_height
    student_count += 1

avg_height = round(height / student_count)

print(avg_height)
