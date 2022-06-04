# Terraform Variables
---


### Variables Types
The Terraform language uses the following types for its values

- string: a sequence of Unicode characters representing some text, like "hello".
    ~~~
        variable "region" {
            type    = string
            default = "us-east-2"
        }
        
        Example:
            provider "aws" {
            region = var.region
            access_key = var.access_key
            secret_key = var.secret_key
}


    ~~~

- number: a numeric value. The number type can represent both whole numbers like 15 and fractional values like 6.283185.
    ~~~
        variable "ssh_port" {
            type    = number
            default = 22
        }
    ~~~

- bool: a boolean value, either true or false. bool values can be used in conditional logic.
    ~~~
        variable "enabled" {
            default = true|false
        }
    ~~~

- list : a sequence of values, like ["us-west-1a", "us-west-1c"]. Elements in a list.
    ~~~
        variable "mylist" {
            type    = list(string)
            default = ["value1","value2","value3"]
        }
    ~~~

- tuple : a sequence of values, like ("us-west-1a", "us-west-1c"). Elements in a tuple are identified by consecutive whole numbers, starting with zero.
    ~~~
        variable "mytuple" {
            type    = tuple([string, number, string])
            default = ["value1", 2, "value2"]
        }
    ~~~

- map : a group of values identified by named labels, like {name = "siva", age = 52}.
    ~~~
        variable "mymap" {
            type    = map
            default = {
                key1 = "value1"
                key2 = "value2"
            }
        }
    ~~~

- object : a group of values identified by named labels, like {name = "vishnu", age = 52}.
    ~~~
        variable "subnet_cidr" {
            type    = object({ private = string, public = list(string)})
            default = {
                private = "10.0.0.0/16"
                public = ["10.0.99.0/24", "10.0.100.0/24", "10.0.101.0/24"]
            }
        }
    ~~~

Strings, numbers, and bools are sometimes called primitive types. Lists/tuples and maps/objects are sometimes called complex types, structural types, or collection types.
