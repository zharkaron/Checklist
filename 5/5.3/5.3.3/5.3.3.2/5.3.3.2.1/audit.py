import os

outcome = "5/5.3/5.3.3/5.3.3.2/5.3.3.2.1/outcome"

with open (outcome, 'r') as file:
	content = file.read().strip()
if content:
	last_word = content.split()[-1]
	if last_word == '3':
		print("5.3.3.2.1 | Ensure password number of changed characters is configured | yes")
	else:
		print("5.3.3.2.1 | Ensure password number of changed characters is configured | no")
else:
	print("The file is empty")
