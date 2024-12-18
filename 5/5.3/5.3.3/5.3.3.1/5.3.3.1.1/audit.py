import os

outcome = "5/5.3/5.3.3/5.3.3.1/5.3.3.1.1/outcome"

with open (outcome, 'r') as file:
	content = file.read().strip()
if content:
	last_word = content.split()[-1]
	if last_word == '3':
		print("5.3.3.1.1 | Ensure password failed attempts lockout is configured | yes")
	else:
		print("5.3.3.1.1 | Ensure password failed attempts lockout is configured | no")
else:
	print("5.3.3.1.1 | Ensure password failed attempts lockout is configured| no")
