print("STUDENT MARKS AND GRADE CHECKER")

python = float(input("Enter Python marks: "))
maths = float(input("Enter Maths marks: "))
computer = float(input("Enter Computer Science marks: "))

if (0 <= python <= 100 and
    0 <= maths <= 100 and
    0 <= computer <= 100):

    total = python + maths + computer
    percentage = total / 3

    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    elif percentage >= 40:
        print("Grade: E")
    else:
        print("Grade: Fail")

else:
    print("Invalid marks! Enter marks between 0 and 100.")
