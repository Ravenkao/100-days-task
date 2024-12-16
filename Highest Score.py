student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# Option 1
total_exam_score = sum(student_scores)
print(total_exam_score)

# Option 2
sum = 0
for score in student_scores:
    sum += score

print(sum)

# MAX Option 1
total_exam_score = max(student_scores)
print(max(student_scores))

# MAX Option 2
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)