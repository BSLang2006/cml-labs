import subprocess

devices = {"sw0": "10.10.99.100", "sw1": "10.10.99.101", "sw2": "10.10.99.102"}

for device in devices:

    command = ["ping", "-n", "1", "-S", "10.10.99.6", devices[device]]
    output = subprocess.run(command, capture_output=True)
    display = output.stdout.decode()

    status = "down"

    for line in display.splitlines():
        if "bytes=32" in line: 
            status = "up"

    print (device, devices[device], status)