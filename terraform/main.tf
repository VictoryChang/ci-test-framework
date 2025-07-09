provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-05ee755be0cd7555c"
  instance_type = "t3.micro"
}
