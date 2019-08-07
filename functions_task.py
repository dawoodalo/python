def check_birthdate(y,m,d):
	import datetime
	date_object = datetime.date.today()
	past_check = date_object > check_birthdate
	return past_check

def calculate_age(y,m,d):
	from datetime import date
	calc_year = date.today().y - y
	calc_month = date.today().m - m
	calc_day = date.today().d - d
	print("You are %s year(s), %s month(s), and %s day(s) old" % (calc_year, calc_month, calc_day))

y = int(input("Enter year of birth:  "))
m = int(input("Enter month of birth:  "))
d = int(input("Enter day of birth:  "))

if check_birthdate(y, m, d) == True:
	calculate_age(y, m, d)
else:
	print("Invalid birthday")
