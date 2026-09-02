import subprocess

def is_up(exitCode):
    result = "down"
    if exitCode == 0:
        result = "up"
    return result

devices = {"sw0":"10.10.99.100","sw1":"10.10.99.101","sw3":"10.10.99.103"}

for device in devices:

    command = ["Ping","-n", "1", "-S", "10.10.99.6", devices[device]]
    output = subprocess.run(command, capture_output=True)

    exitCode = output.returncode

    print(is_up(exitCode))