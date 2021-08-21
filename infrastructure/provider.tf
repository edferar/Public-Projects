provider "aws" {
    region = var.aws_region
}

#centralizando arquivo de estado do terraform
terraform{
    backend "s3" {
      bucket = "terraform-state-igti-edney"
      key = "state/igti/edv/mod1/terraform.tfstate"
      region = "us-east-1"
    }
}