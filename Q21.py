### Q21 write a user defined function in python named showGrades which takes the dictionary S as an arguement conatains Name:[Eng,Math,Science] as key value pair . The fn dispalys the corresponding result >=90 grade A , <90 but >= 60 grade B , <60 grade C



def showGrades(S):
    for name, scores in S.items():
        print(f"Grades for {name}:")
        for subject, score in zip(['English', 'Math', 'Science'], scores):
            if score >= 90:
                grade = 'A'
            elif score >= 60:
                grade = 'B'
            else:
                grade = 'C'
            print(f"{subject}: {grade}")
        print()  

# Example usage:
S = {
    "Rudhra": [95, 85, 92],
    "Shadab": [58, 77, 65],   
}

showGrades(S)
