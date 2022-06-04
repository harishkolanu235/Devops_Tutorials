# Terraform State
---

**State**
- Terraform must store state about your managed infrastructure and configuration. This state is used by Terraform to map real world resources to your configuration, keep track of metadata, and to improve performance for large infrastructures. 

- This state is stored by default in a local file named "terraform.tfstate", but it can also be stored remotely, which works better in a team environment.

- Terraform uses this local state to create plans and make changes to your infrastructure. Prior to any operation, Terraform does a refresh to update the state with the real infrastructure.

