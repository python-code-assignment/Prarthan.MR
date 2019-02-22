def Grade(score):
    grades = [(90, 'Distinction'), (80, 'First Class'), (60, 'Second Class'), (40, 'Third Class'), (0, 'Fail')]
    for i in range(len(grades)):
        if score >= grades[i][0]:
            return grades[i][1]
        
score=input("enter the grade")
score=int(score)
print(Grade(score))
