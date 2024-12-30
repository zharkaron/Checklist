#!/bin/bash
grep -Psi -- '^\h*password\h+[^#\n\r]+\h+pam_pwhistory\.so\h+([^#\n\r]+\h+)?enforce_for_root\b' /etc/pam.d/common-password > 5/5.3/5.3.3/5.3.3.3/5.3.3.3.2/outcome

python3 5/5.3/5.3.3/5.3.3.3/5.3.3.3.2/audit.py
