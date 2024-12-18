import os

outcome = "5/5.3/5.3.3/5.3.3.2/5.3.3.2.8/outcome"

with open (outcome, 'r') as file:
	content = file.read().strip()
if content:
	last_word = content.split()[-1]
	if last_word == 'enforce_for_root':
		print("5.3.3.2.8 | Ensure password quality is enforced for the root user | yes")
	else:
		print("5.3.3.2.8 | Ensure password quality is enforced for the root user | no")
else:
	print("5.3.3.2.8 | Ensure password quality is enforced for the root user | no")
