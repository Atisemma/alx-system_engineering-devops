# 0x16. API advanced

## Description
This project focuses on advanced API usage and scripting in Python for back-end development. It covers topics such as reading API documentation, pagination, parsing JSON results, making recursive API calls, and sorting dictionaries.

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Resources
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## General Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- All files end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A `README.md` file at the root of the project folder is mandatory
- Code should adhere to PEP 8 style
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Requests module must be used for sending HTTP requests to the Reddit API
