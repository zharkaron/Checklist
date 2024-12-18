#!/bin/bash

cat /etc/security/pwquality.conf | grep difok > 5/5.3/5.3.3/5.3.3.2/5.3.3.2.1/outcome

python3 "5/5.3/5.3.3/5.3.3.2/5.3.3.2.1/audit.py"
