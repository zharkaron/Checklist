#!/bin/bash

cat /etc/security/pwquality.conf | grep dictcheck > 5/5.3/5.3.3/5.3.3.2/5.3.3.2.6/outcome

python3 "5/5.3/5.3.3/5.3.3.2/5.3.3.2.6/audit.py"
