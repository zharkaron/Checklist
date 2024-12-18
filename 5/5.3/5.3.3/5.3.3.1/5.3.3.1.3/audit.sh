#!/bin/bash

grep -Pi -- '^\h*(even_deny_root|root_unlock_time\h*=\h*\d+)\b' /etc/security/faillock.conf > 5/5.3/5.3.3/5.3.3.1/5.3.3.1.3/outcome

python3 5/5.3/5.3.3/5.3.3.1/5.3.3.1.3/audit.py
