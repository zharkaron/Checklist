#!/bin/bash
grep -Pi -- '^\h*unlock_time\h*=\h*(0|9[0-9][0-9]|[1-9][0-9]{3,})\b' /etc/security/faillock.conf > 5/5.3/5.3.3/5.3.3.1/5.3.3.1.2/outcome

python3 5/5.3/5.3.3/5.3.3.1/5.3.3.1.2/audit.py
