"""
Decision Pipeline Engine

Determines application outcome using
function delegation and early returns
"""

def check_age(age):
    if age < 18:
        return "Rejected: Underage"
    return None

def check_discipline(flag):
    if flag == "yes":
        return "Rejected: Disciplinary Record"
    return None

def check_score(score):
    if score <= 60:
        return "Rejected: Low Score"
    if score >= 85:
        return "Accepted with Scholarship"
    return "Accepted"

def decision_pipeline(age, score, flag):

    result = check_age(age)
    if result:
        return result
    result = check_discipline(flag)
    if result:
        return result
    
    return check_score(score)

age = int(input("Enter age: "))
score = int(input("Enter score: "))
flag = input("Disciplinary record? (yes/no): ").lower()
result = decision_pipeline(age, score, flag)
print(f"Final Decision: {result}")