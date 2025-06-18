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

  - **Why Use terraform import?**
    - Resources already exist (manually created or via other tools) and you want Terraform to manage them.
    - You want to avoid re-creating existing infrastructure by Terraform.
    - You are migrating old infrastructure to Infrastructure-as-Code (IaC) via Terraform.

#### 9. What are Modules in Terraform?

  - Modules are reusable Terraform configurations. They enable code reusability, maintainability, and scalability.
    ~~~
      module "vpc" {
        source = "./modules/vpc"
      }
    ~~~

#### 10. Difference between count and for_each in Terraform?

  - *count:* Used to create multiple resources based on a number.
  - *for_each:* Used to create resources based on a map or set of strings.

#### 11. Can you explain depends_on in Terraform?

  - depends_on is used to specify explicit dependencies between resources when implicit dependency cannot be derived by Terraform.

#### 12. How does Terraform handle drift?

  - Terraform detects drift when you run terraform plan. If any resource has been changed outside of Terraform, it will show the differences and optionally correct them.
    
#### 13. What is a Data Source in Terraform?

  - Data sources allow Terraform to fetch data from external resources or APIs for use in the configuration without managing them.
    ~~~
      provider "azurerm" {
        features {}
      }
      
      data "azurerm_key_vault" "example" {
        name = "myKeyVault"
        resource_group_name = "myResourceGroup"
      }
      
      data "azurerm_key_vault_secret" "client_id" {
        name  = "Terraform-Client-Id"
        key_vault_id = data.azurerm_key_vault.example.id
      }
      
      data "azurerm_key_vault_secret" "client_secret" {
        name  = "Terraform-Client-Secret"
        key_vault_id = data.azurerm_key_vault.example.id
      }
      
      data "azurerm_key_vault_secret" "tenant_id" {
        name = "Terraform-Tenant-Id"
        key_vault_id = data.azurerm_key_vault.example.id
      }
      
      data "azurerm_key_vault_secret" "subscription_id" {
        name = "Terraform-Subscription-Id"
        key_vault_id = data.azurerm_key_vault.example.id
      }
      
      provider "azurerm" {
        features {}
        client_id       = data.azurerm_key_vault_secret.client_id.value
        client_secret   = data.azurerm_key_vault_secret.client_secret.value
        tenant_id       = data.azurerm_key_vault_secret.tenant_id.value
        subscription_id = data.azurerm_key_vault_secret.subscription_id.value
      }
    ~~~
    
#### 14. What happens if your terraform apply fails in the middle?

  - Partial changes may occur. Terraform records what was successfully applied and what failed. On the next run, Terraform will attempt to continue or correct based on the state file.

#### 15. How do you upgrade Terraform providers?

  - Update the required_providers block and run:
    ~~~
      $ terraform init -upgrade
    ~~~

#### 16. What is the difference between local-exec and remote-exec provisioners?
  
  - **local-exec:** Runs commands on the machine running Terraform.
  - **remote-exec:** Runs commands on the target remote resource.

#### 17. Explain the concept of workspaces in Terraform.
  
  - Workspaces allow you to manage multiple state files for the same configuration, useful for managing environments like dev, staging, and prod.

#### 18. What is the use of the terraform validate command?

  - It validates the configuration files for syntax errors and correctness.

#### 19. Can you explain backend in Terraform?

  - Backend defines where Terraform state is stored (local, S3, Terraform Cloud, etc.)
  ~~~
  Example for s3
    terraform {
      backend "s3" {
        bucket = "mybucket"
        key    = "state.tfstate"
        region = "us-east-1"
      }
    }

  Example of Azure Storage
   terraform {
    backend "azurerm" {
      resource_group_name  = "terraform-rg"
      storage_account_name = "tfstatestorage123"
      container_name       = "tfstate"
      key                  = "terraform.tfstate"
    }
  }

  ~~~
