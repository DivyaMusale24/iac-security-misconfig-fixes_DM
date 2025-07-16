# IaC Security Misconfiguration Fixes

This project highlights common security misconfigurations in Terraform infrastructure and how to detect and fix them using open-source tools.

The goal: build secure cloud infrastructure by design—not as an afterthought.

##  What This Project Covers

- Security misconfigurations in:
  - AWS Security Groups
  - IAM Policies
  - S3 Buckets
- Detection using:
  - Checkov
  - tfsec
  - KICS
- Remediation using Terraform best practices

##  Project Structure

├── terraform/ # Insecure IaC examples
├── terraform/secure_versions/ # Hardened versions after remediation
├── scans/ # Static analysis output
└── README.md

##  Examples of What Was Fixed

| Resource           | Misconfiguration                     | Fix Applied                     |
|-------------------|----------------------------------------|----------------------------------|
| Security Group     | SSH open to 0.0.0.0/0                 | Restricted to internal CIDR     |
| S3 Bucket          | No encryption, public access         | Enforced AES256 + private ACL   |
| IAM Policy         | Wildcard `"*"` on Action + Resource  | Scoped to `s3:GetObject` only   |

##  Tools Used

- [Checkov](https://github.com/bridgecrewio/checkov)
- [tfsec](https://github.com/aquasecurity/tfsec)
- [KICS](https://github.com/Checkmarx/kics)
- GitHub Actions (planned)

## Why I Built This

Most cloud breaches start with misconfigured infrastructure. I wanted to gain hands-on experience not just in identifying those misconfigs—but actually fixing them.

This project simulates real-world issues and shows how they can be remediated in a structured, automated, and version-controlled way.

## Key Learnings

- Scanning tools are only useful if you take action on the results
- Secure defaults matter, especially with IAM and networking
- Documentation and automation go hand-in-hand for scalable remediation

##  Live Repo

> https://github.com/DivyaMusale24/iac-security-misconfig-fixes_DM


