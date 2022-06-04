# Terraform Output
---


**Output** - Output values make information about your infrastructure available on the command line, and can expose information for other Terraform configurations to use. Output values are similar to return values in programming languages

## Declaring an Output Value
    Example-1
        output "instance_ip_addr" {
            value = aws_instance.server.private_ip
        }

    Example-2
        output "vpc_id" {
            value = aws_vpc.myvpc.id
        }
    