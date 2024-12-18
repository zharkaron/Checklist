#!/bin/bash

cat /etc/security/pwquality.conf | grep enforce_for_root > 5/5.3/5.3.3/5.3.3.2/5.3.3.2.8/outcome

python3 "5/5.3/5.3.3/5.3.3.2/5.3.3.2.8/audit.py"
