import os

file_path="5/5.3/5.3.3/5.3.3.3/5.3.3.3.1/outcome"

if os.path.isfile(file_path):
	if os.stat(file_path).st_size ==0:
		print("5.3.3.3.1 | Ensure password history remember is configured | no")
	else:
		print("5.3.3.3.1 | Ensure password history remember is configured | yes")
