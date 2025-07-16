# 🛡️ IaC Misconfiguration Fix: EC2 Security Group

##  What I Did
- Simulated a real-world misconfiguration: SSH (port 22) was open to the internet
- Detected the issue using Checkov
- Remediated by restricting access to internal CIDR blocks
- Validated the fix with zero failed checks

##  Problem

cidr_blocks = ["0.0.0.0/0"] # ❌ anyone on the internet can SSH in

##  Fix

cidr_blocks = ["10.0.0.0/16"] # ✅ only internal IPs allowed

