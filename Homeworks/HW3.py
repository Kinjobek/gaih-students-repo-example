print("\nCourse Grade Application\n")

name = input("Enter Name and Surname of student: ")
print("Enter 2 Midterms and Final marks: ")
Midterm1 = float(input("Midterm1" ": "))
Midterm2 = float(input("Midterm2"  ": "))    
Final = float(input("Final" ": "))

Total = Midterm1*0.30 + Midterm2*0.30 + Final*0.40

print("Total Grade:", Total)     

if Total >= 93:
    mark = "A+"
elif Total >= 86:
    mark = "A"
elif Total >= 76:
    mark = "B"
elif Total >= 56:
    mark = "C"
else:
    mark = "F"

if Total >= 86:
    Total = "GREAT"
elif Total >= 76:
    Total = "GOOD"
elif Total >= 56:
    Total = "PASS"
else:
    Total = "FAIL"

print("\nName: ", name, "\nMidterm 1: ", Midterm1, "\nMidterm 2: ", Midterm2, "\nFinal: ", Final, "\nMark: ", mark, "\nTotal: ", Total)
