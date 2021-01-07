import datetime 

today = datetime.date.today()

dob = input("Enter your dob> ")
d,m,y = dob.split(" ")

dob_date = datetime.date(int(y), int(m), int(d))
diff =  today - dob_date
print(diff.days)


