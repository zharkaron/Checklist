#!/bin/bash

cat /etc/security/pwquality.conf | grep enforcing > 5/5.3/5.3.3/5.3.3.2/5.3.3.2.7/outcome

python3 "5/5.3/5.3.3/5.3.3.2/5.3.3.2.7/audit.py"
