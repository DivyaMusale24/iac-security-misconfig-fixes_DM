resource "aws_security_group" "secure_sg" {
  name        = "secure_sg"
  description = "Restricted SSH access"

  ingress {
    description  = "Allow SSH from internal network"
    from_port    = 22
    to_port      = 22
    protocol     = "tcp"
    cidr_blocks  = ["10.0.0.0/16"]
  }

  egress {
    description  = "Allow HTTPS egress to internal network"
    from_port    = 443
    to_port      = 443
    protocol     = "tcp"
    cidr_blocks  = ["10.0.0.0/16"]
  }
}


