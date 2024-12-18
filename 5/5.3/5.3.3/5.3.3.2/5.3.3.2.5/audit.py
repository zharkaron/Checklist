import os

outcome = "5/5.3/5.3.3/5.3.3.2/5.3.3.2.5/outcome"

with open (outcome, 'r') as file:
	content = file.read().strip()
if content:
	last_word = content.split()[-1]
	if last_word == '2':
		print("5.3.3.2.5 | Ensure password maximum sequential characters is configured | yes")
	else:
		print("5.3.3.2.5 | Ensure password maximum sequential characters is configured | no")
else:
	print("5.3.3.2.5 | Ensure password maximum sequential characters is configured | no")
