# pyneng-workout
https://pyneng.readthedocs.io/ru/latest/contents.html
Курс Натальи Самойленко.


## Creating virtual environment of Python 3.8.5
- python.3.8.install.sh: installs python 3.8.5
- venv-3.8.make.sh: creates virtual environment of Python 3.8.5 in venv-3.8 directory
- venv-3.8.modules.sh: updates pip, installs modules from requirements.txt

## Activating virtual environment

    . venv-3.8/bin/activate

## Deactivating virtial environment

    deactivate


## Exercise desriptions

[06_control_structures](06_control_structures) - Parsing ip addresses. Checking the correct address.

[09_functions](09_functions) - Generating configs by templates. Parsing configs. 
  - 9.3 parsing config
  - 9.4 converting config into dictionary

[11_modules](11_modules) - Parsing command "show cdp neighbors". Device map creation. Graphviz.
  - 11.1 cdp neighbors
  - 11.2 network map creation by cdp neighbors, map drawing, graphviz
  
[12_useful_modules](12_useful_modules) - Subprocess. Pinging. Decorated output.
  - 12.1 module subprocess, pinging ip address
  - 12.2 module subprocess, pinging ip address ranges
  - 12.3 module tabulate, print result in columns

[15_module_re](15_module_re) - Regular expressions. Parsing configs.
  - 15.1  simple regex search in config file, re.search
  - 15.1a regex search in config file, search ip of interfaces, re.search, match.group, match.groups
  - 15.1b regex search in config file, search multiple ip of interfaces, re.search, match.group, match.groups
  - 15.2  parsing of output of command "show ip int br" from file, re.search, match.groups
  - 15.2a convertning list of headers and list of values into list of dictionaries with headers as keys, zip(), comprehension
  - 15.3  converting file with IOS NAT rules to file with ASA NAT rule, regex with groups, str.format of match.groupdict()
  - 15.4  looks for interfaces without a description in the config file, regex with multiple conditions, matchgroups, match.lastgroup
  - 15.5  parsing command show cdp neighbors from file, regex with groups, str.format of match.groupdict() 

[17_serialization](17_serialization) - Work with csv, json, yaml files. Parsing multiple files. Graphviz.
  - 17.1 writing to csv, parsing "show dhcp snooping binding" with regex "ip,mac,vlan,port"
  - 17.2 writing to csv, parsing "show versions" with regex "ios, image, uptime", using flag re.DOTALL
  - 17.3 reading csv, parsing "show cdp neighbors" with regex
  - 17.3a writing to yaml, parsing multiple output "show cdp neighbors" with regex
  - 17.3b reading yaml, topology creation, graphviz
  - 17.4 reading/writing csv as dict, comparing dates
[18_ssh_telnet](18_ssh_telnet) - Connection to equipment. Modules netmiko.
  - 18.1 netmiko

[19_concurrent_connections](19_concurrent_connections) - Concurrent connections to multiple devices.
modules: logging, concurrent.futures, subprocess, platform
  - 19.1 ping a range of IP addresses using multithreading

[20_jinja2](20_jinja2) - Jinja2 configuration templates. Modules jinja2, yaml, sys, os.
  - 20.1 load jinja template and yaml config. print rendered config 

[OOP basics](22_oop_basics) - OOP
  - 22.1 Class creation. __init__.
