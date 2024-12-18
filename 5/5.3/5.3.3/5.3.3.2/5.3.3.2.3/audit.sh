#!/bin/bash

grep -E 'minclass|ucredit|lcredit|dcredit|ocredit' /etc/security/pwquality.conf > 5/5.3/5.3.3/5.3.3.2/5.3.3.2.3/outcome

python3 "5/5.3/5.3.3/5.3.3.2/5.3.3.2.3/audit.py"
