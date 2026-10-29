name=input("Enter student name: ")
n=int(input("Enter number of subjects: "))
total=0
for i in range(1,n+1):
    mark=int(input(f"Enter marks for subject {i}: "))
    total=total+mark
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="outstanding"
elif percentage>=80:
    grade="A"
    performance="excellent"
elif percentage>=70:
    grade="b"
    performance="very good"
elif percentage>=60:
    grade="c"
    performance="good"
elif percentage>=50:
    grade="D"
    performance="average"
print("name:",name)
print("marks:",total)
print("percentage:",percentage)
print("grade:",grade)
print("performance:",performance)


