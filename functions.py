# custom-functions/my_functions.py

def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp*9/5) + 32
    



# TODO: define gradebook function here

def numeric_to_letter_grade (i):
    if i >= 93:
        return "A"
    elif i >= 90:
        return "A-"
    elif i >= 87.5:
        return "B+" 
    elif i >= 84:
        return "B"
    elif i >= 80:
        return "B-"
    else:
        return "C"

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = float(input("Enter Numeric Grade (from 0 to 100):"))
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)