import subprocess

devices = {"sw0":"192.168.40.100","r1":"192.168.40.101","r2":"192.168.40.102","r3":"192.168.40.103"}

for device in devices:
    command = ["ping", "-n", "1", devices[device]]
    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode()

    if "Received = 1" in output:
        status = "up"
    else:
        status = "down"

    print(device, " = ", devices[device], " - ", status)