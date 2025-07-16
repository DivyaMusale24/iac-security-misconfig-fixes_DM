# IaC Security Misconfiguration Fixes

This project highlights common security misconfigurations in Terraform infrastructure and how to detect and fix them using open-source tools.

The goal: build secure cloud infrastructure by design, not as an afterthought.

##  What This Project Covers

- Security misconfigurations in:
  - AWS Security Groups
  - IAM Policies
  - S3 Buckets
- Detection using:
  - Checkov
  - tfsec
  - KICS
- Remediation using:
  - Terraform best practices
  - A custom-built Python auto-remediation script

##  Project Structure

iac-security-misconfig-fixes/
├── terraform/
│ ├── ec2_public.tf
│ ├── s3_unencrypted.tf
│ ├── iam_overprivileged.tf
│ └── secure_versions/
│ ├── ec2_secure.tf
│ ├── s3_secure.tf
│ └── iam_secure.tf
├── scans/
│ └── checkov_results.txt
├── auto_fix.py
└── README.md

##  Examples of What Was Fixed

| Resource           | Misconfiguration                     | Fix Applied                     |
|-------------------|----------------------------------------|----------------------------------|
| Security Group     | SSH open to 0.0.0.0/0                 | Restricted to internal CIDR     |
| S3 Bucket          | No encryption, public access         | Enforced AES256 + private ACL   |
| IAM Policy         | Wildcard "*" on Action + Resource  | Scoped to 's3:GetObject' only   |

##  Automation with Python

To go beyond detection, I created a Python script ('auto_fix_misconfig') that identifies common insecure patterns and rewrites hardened Terraform configurations automatically. This simulates a real-world auto-remediation pipeline.
''' python3 auto_fix_misconfig.py

Output files are saved in terraform/secure_versions/

##  Tools Used

- [Checkov](https://github.com/bridgecrewio/checkov)
- [tfsec](https://github.com/aquasecurity/tfsec)
- [KICS](https://github.com/Checkmarx/kics)

## Why I Built This

Misconfigurations are one of the leading causes of cloud breaches. I wanted to go beyond theory, by replicating the mistakes that actually happen in production and practicing how to fix them with repeatability, documentation, and automation.

This hands-on project allowed me to combine scanning tools, remediation strategies, and scripting to simulate real-world incident handling from start to resolution.

## Key Learnings

- Scans are just the beginning, fixing the root issue is the real value
- IAM and Security Group defaults should be secure, not permissive
- Automation scales, codifying fixes helps teams enforce policies efficiently

##  Live Repo

> https://github.com/DivyaMusale24/iac-security-misconfig-fixes_DM


