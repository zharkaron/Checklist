#!/bin/bash
grep -Pi -- '^\h*deny\h*=\h*[1-5]\b' /etc/security/faillock.conf > 5/5.3/5.3.3/5.3.3.1/5.3.3.1.1/outcome

python3 5/5.3/5.3.3/5.3.3.1/5.3.3.1.1/audit.py
