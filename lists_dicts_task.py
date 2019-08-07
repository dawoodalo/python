print("Welcome to AC Milan FC")

skills = ["attack", "defense", "goalkeeper"]
cv = {}

name = input("Please insert your name: ")
cv['name'] = name

age = int(input("Please insert age: "))
cv['age'] = age

experience = int(input("Please insert years of experience "))
cv['experience'] = experience
cv['skills'] = ''

skill_amount = 1
for skill in skills:
	print("{}. {}".format(skill_amount, skill))
	skill_amount += 1

skill_1 = input("Choose one of the skills above: ")
cv['skills'] = skill_1


skill_2 = input("Choose another skill from above: ")
cv['skills2'] = skill_2

if age >= 16 and age <= 21 and experience >= 2 and (skill_1 == "attack" or skill_2 == "goalkeeper"):
	print("Congrats, you have been accepted")
else:
	print("Sorry, you do not meet the requirements")