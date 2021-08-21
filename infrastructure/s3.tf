resource "aws_s3_bucket" "dl" {
  bucket = "datalake-edney-igti-tf"
  acl = "private"

    tags={
        IES = "IGTI"
        CURSO = "EDC"

    }

    server_side_encryption_configuration {
      rule{
          apply_server_side_enryption_by_default{
              sse_algorithm = "AES256"
          }
      }
      
    }
}
