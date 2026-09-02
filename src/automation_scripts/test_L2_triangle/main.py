import subprocess

dev = {"sw0":"10.10.99.100", "sw1":"10.10.99.101", "sw2":"10.10.99.102", "sw3":"10.10.99.103"}


for device in dev:
        
        command = ["ping", "-n", "1", "-S", "10.10.99.6", dev[device]]
        result = subprocess.run(command, capture_output=True)
        output = result.stdout.decode()

        print(type(result), type(result.stdout), type(output))
