import os

file_path="5/5.3/5.3.3/5.3.3.3/5.3.3.3.3/outcome"

if os.path.isfile(file_path):
	if os.stat(file_path).st_size ==0:
		print("5.3.3.3.3 |Ensure pam_pwhistory includes use_authtok | no")
	else:
		print("5.3.3.3.3 | Ensure pam_pwhistory includes use_authtok | yes")
