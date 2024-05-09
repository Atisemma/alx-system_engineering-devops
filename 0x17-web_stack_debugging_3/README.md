# 0x17. Web stack debugging #3

## Description
This project focuses on debugging a Wordpress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. It is designed to provide hands-on experience in troubleshooting and resolving issues that may arise in a web server environment.

## Requirements
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Puppet manifests must run without error
- The first line of Puppet manifests must be a comment explaining the purpose of the manifest
- Puppet manifest files must have the `.pp` extension
- Files will be checked with Puppet v3.4

## Setup
1. Install `puppet-lint` version 2.1.1:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
