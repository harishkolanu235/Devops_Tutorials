# Terraform Basics
---

### Components of Terraform
1. Provider
2. Resources
3. Variables
4. Statefile
5. Provisioners
6. Backends
7. Modules
8. Data Sources
9. Service Prinicipals

1. Providers
   
   - a provider is a plugin that allows Terraform to interact with external platforms, services, or APIs.
   - Providers are responsible for understanding API interactions and exposing resources that can be managed by Terraform.

1. **Init** - The terraform init command is used to initialize a working directory containing Terraform configuration files. 
This is the first command that should be run after writing a new Terraform configuration or cloning an existing one from version control. It is safe to run this command multiple times.
    ~~~
        $ terraform init
    ~~~

2. **Plan** - The terraform plan command creates an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure
    ~~~
        $ terraform plan
    ~~~

3. **Apply** - The terraform apply command executes the actions proposed in a Terraform plan.
    ~~~
        $ terraform apply
    ~~~

4. **Destry** - The terraform destroy command is a convenient way to destroy all remote objects managed by a particular Terraform configuration.
    ~~~
        $ terraform destroy
    ~~~
