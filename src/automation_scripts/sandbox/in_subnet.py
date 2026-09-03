devices = [
    {"name": "sw0", "ip": "10.10.99.100", "role": "access"},
    {"name": "sw1", "ip": "10.10.99.101", "role": "access"},
    {"name": "core0", "ip": "10.10.99.1", "role": "core"},
]

matches = []
for d in devices:
     if d["role"] == role:
        matches.append(d["name"])