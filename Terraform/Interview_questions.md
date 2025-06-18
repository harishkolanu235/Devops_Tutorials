#### 1. What is Terraform?

  Terraform is an open-source Infrastructure as Code (IaC) tool created by HashiCorp. It allows you to define and provision data center infrastructure using a declarative configuration language (HCL - HashiCorp Configuration Language).

#### 2. What are the key features of Terraform?

  - Infrastructure as Code (IaC)
  - Execution Plan (terraform plan)
  - Resource Graph (terraform graph)
  - Change Automation (terraform apply)
  - Provider support (AWS, Azure, GCP, etc.)

#### 3. Explain the Terraform workflow?
  
  - **Write:** Define infrastructure in .tf files.
  - **Initialize:** Run terraform init to initialize configuration.
  - **Plan:** Run terraform plan to preview changes.
  - **Apply:** Run terraform apply to make actual changes.
  - **Destroy:** Run terraform destroy to remove infrastructure.

#### 4. What are Providers in Terraform?
  - Providers are plugins in Terraform that interact with cloud providers (like AWS, Azure, GCP) or other APIs.
    ~~~
      provider "aws" {
        region = "us-east-1"
      }
    ~~~

#### 5. What is the difference between terraform plan and terraform apply?

  - **terraform plan:** Shows what changes Terraform will make.
  - **terraform apply:** Actually performs those changes on the infrastructure.

#### 6. What is a Terraform state file?

  - Terraform stores the infrastructure's current state in a file called terraform.tfstate. This file is crucial for tracking resources and managing dependencies.

#### 7. How do you manage Terraform state in a team?
  - Using Remote State (e.g., Azuere storage blob, AWS S3 with DynamoDB locking, Terraform Cloud) to avoid conflicts and ensure consistency when multiple people work on the same infrastructure.

#### 8. What is the purpose of terraform import?

  - terraform import allows existing infrastructure to be brought under Terraform management without recreating resources.
    ~~~
      $ terraform import aws_instance.example i-abcd1234
    ~~~

#### 9. What are Modules in Terraform?

  - Modules are reusable Terraform configurations. They enable code reusability, maintainability, and scalability.
    ~~~
      module "vpc" {
        source = "./modules/vpc"
      }

    ~~~
    
