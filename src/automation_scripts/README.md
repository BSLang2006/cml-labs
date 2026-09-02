# Network Automation

Python tooling for managing network devices as code rather than by hand.

## Tools

| Tool | What it does |
|---|---|
| _health check_ | pings devices and reports status |

## Approach

Device configuration lives in YAML as a source of truth. Scripts render, push, and validate against it — so a change is reviewable in git before it touches a device, and verifiable after.

## Stack

Python · Netmiko · YAML · Jinja2 · Linux · Cisco IOS-XE
