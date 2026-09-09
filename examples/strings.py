my_name_lower = "cole mathis"
my_name_upper = my_name_lower.upper()
# print(my_name_upper)

university = "     Arizona State University     "

split_uni = university.split()
# print(split_uni)


# f strings
month = 10
day = 1
year = 2026
# Format variables
date = f"{month}-{day}-{year}"
# print(date)

# Control the number of decimal points
pi = 3.14159
str_pi = f"{pi:.4f}"
# print(str_pi)

# Convert to a percentage
score = 7.5
max_score = 10
grade = score/max_score
str_grade = f"{grade:.1%}"
print(str_grade)
