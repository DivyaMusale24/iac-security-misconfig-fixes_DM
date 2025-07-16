import os
import re

INPUT_DIR = "terraform"
OUTPUT_DIR = os.path.join(INPUT_DIR, "secure_versions")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def harden_ec2(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Fix SSH ingress from 0.0.0.0/0 to internal CIDR
    content = re.sub(r'cidr_blocks\s*=\s*\["0\.0\.0\.0/0"\]', 'cidr_blocks = ["10.0.0.0/16"]', content)

    # Limit egress to HTTPS and internal CIDR
    content = re.sub(r'egress\s*{[^}]*}', '''egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
}''', content, flags=re.DOTALL)

    output_path = os.path.join(OUTPUT_DIR, "ec2_secure.tf")
    with open(output_path, "w") as f:
        f.write(content)
    print(f"[+] Hardened EC2 config written to {output_path}")

def harden_s3(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Make S3 bucket private
    content = re.sub(r'acl\s*=\s*"public-read"', 'acl = "private"', content)

    # Add encryption block if not present
    if "server_side_encryption_configuration" not in content:
        encryption_block = '''
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
'''
        content = content.replace('}', encryption_block + '\n}', 1)

    output_path = os.path.join(OUTPUT_DIR, "s3_secure.tf")
    with open(output_path, "w") as f:
        f.write(content)
    print(f"[+] Hardened S3 config written to {output_path}")

def harden_iam(file_path):
    hardened_policy = '''resource "aws_iam_policy" "secure_policy" {
  name   = "read-only-s3"
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": "arn:aws:s3:::my-secure-bucket/*"
    }]
  })
}'''
    output_path = os.path.join(OUTPUT_DIR, "iam_secure.tf")
    with open(output_path, "w") as f:
        f.write(hardened_policy)
    print(f"[+] Hardened IAM policy written to {output_path}")

print("Starting auto-remediation...")

for filename in os.listdir(INPUT_DIR):
    path = os.path.join(INPUT_DIR, filename)
    if filename.startswith("ec2") and filename.endswith(".tf"):
        harden_ec2(path)
    elif filename.startswith("s3") and filename.endswith(".tf"):
        harden_s3(path)
    elif filename.startswith("iam") and filename.endswith(".tf"):
        harden_iam(path)

print("Auto-remediation complete.")

