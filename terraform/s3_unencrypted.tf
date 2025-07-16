resource "aws_s3_bucket" "public_bucket" {
  bucket = "my-insecure-bucket"
  acl    = "public-read"
}

