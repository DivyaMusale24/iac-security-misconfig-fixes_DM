resource "aws_iam_policy" "overprivileged" {
  name   = "wildcard-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = "*"
      Effect   = "Allow"
      Resource = "*"
    }]
  })
}

