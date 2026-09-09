score = int(input("Enter a score between 0 and 100: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100.")
else:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"A score of {score} earns grade: {grade}")
