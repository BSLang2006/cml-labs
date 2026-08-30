# CML Labs

Documentation | Automation | Rapid Iteration

Cisco Modeling Labs - using code to manage, build, and learn enterprise networking. 

Each topology folder contains compatible labs, device configs, and documentation desinged for rapid deployment and learning. 

## Labs

| Lab | Focus | Writeup |
|---|---|---|
| _in progress_ | | |

## Why

Rapid deployment means more time learning

## Stack

Cisco Modeling Labs · IOS-XE · Linux · Python · Netmiko

## Note:

IOSv devices don't boot intially with nvram - all devices must run <reload> to get the static IP address from the baked config.

## Connections:

CML
external_connector - named "bridge" set to Bridge 1

sw0 always = x.x.x.100
r1-10 always = x.x.x.101-110
sw1-10 always = x.x.x.111-120

If more than 10 of either device or multiple labs are running concurrently special ip address considerations need to be made.
