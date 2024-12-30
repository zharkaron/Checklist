#!/bin/bash
grep -Psi -- '^\h*password\h+[^#\n\r]+\h+pam_pwhistory\.so\h+([^#\n\r]+\h+)?use_authtok\b' /etc/pam.d/common-password > 5/5.3/5.3.3/5.3.3.3/5.3.3.3.3/outcome

python3 5/5.3/5.3.3/5.3.3.3/5.3.3.3.3/audit.py
