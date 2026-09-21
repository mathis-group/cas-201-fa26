
def score_to_percent(score):
    total_points = 10
    return 100*(score/10)

def score_to_grade(score):
    # Take a score and return a letter grade
    grade = ""
    if score >= 9:
        grade = "A"
    elif score >=8:
        grade = "B"
    elif score >= 7:
        grade = "C"
    elif score >= 6:
        grade = "D"
    else:
        grade = "F"
    return grade

my_score = 9
#print(score_to_grade(my_score))


# While loops
a = 1

# while a < 5:
#     # print(a)
#     a += 1
    
    
# Savings account example
balance = 100
interest = 0.14 # high yield rate 5%
year = 0 

# When while the balance double? That happens while the balance is double
while balance <= 200:
    # print(year)
    year += 1
    balance = balance * (1.0 + interest)
    print(f"In year {year}, the balance will be {balance}")
    
