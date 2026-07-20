name=input("student name:")
sub1=int(input("subject1 marks:"))
sub2=int(input("subject2 marks:"))
sub3=int(input("subject3 marks:"))
total=sub1+sub2+sub3
average=total/3
percentage=(total/300)*100
print("student name:",name)
print("Total:",total)
print("Average:",average)
print("Percentage:",percentage)
if percentage>=35:
    print("pass")
else:
    print("fail")    