import os

file_path="5/5.3/5.3.3/5.3.3.3/5.3.3.3.2/outcome"

if os.path.isfile(file_path):
	if os.stat(file_path).st_size ==0:
		print("5.3.3.3.2 | Ensure password history is enforced for the root user | no")
	else:
		print("5.3.3.3.2 | Ensure password history is enforced for the root user | yes")
