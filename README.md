# CML Labs

Documentation | Automation | Rapid Iteration

Cisco Modeling Labs - using code to manage, build, and learn enterprise networking. 

Each topology folder contains compatible labs, device configs, and documentation desinged for rapid deployment and learning. 

## Labs

| Lab | Focus | Writeup |
|---|---|---|
| OSPF | adjacency creation | https://brandonscottlang.com/posts/ospf |
| L2 Triangle | L2 protocols | |

## Why

Rapid deployment means more time learning

## Stack

Cisco Modeling Labs · IOSv · Linux · Python · Netmiko

## Note:

IOSv devices don't boot intially with nvram - all devices will take a long time to load on first boot or after a wipe.

## Connections:

CML
external_connector - named "bridge 99" set to Bridge 99

sw0 always = x.x.x.100
sw1-10 always = x.x.x.101-110
r1-10 always = x.x.x.201-210

If more than 10 of either device or multiple labs are running concurrently special considerations need to be made regarding IP assignments.
