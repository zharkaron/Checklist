import os

outcome = "5/5.3/5.3.3/5.3.3.2/5.3.3.2.6/outcome"

with open (outcome, 'r') as file:
	content = file.read().strip()
if content:
	last_word = content.split()[-1]
	if last_word == '1':
		print("5.3.3.2.6 | Ensure password dictionary check is enabled | yes")
	else:
		print("5.3.3.2.6 | Ensure password dictionary check is enabled | no")
else:
	print("5.3.3.2.6 | Ensure password dictionary check is enabled | no")
