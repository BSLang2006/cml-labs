import yaml

from netmiko import ConnectHandler

with open("../devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

with open("../secrets.yaml") as f:
    creds = yaml.safe_load(f)





r3 = next(d for d in devices if d["name"] == "r3")

conn = ConnectHandler(
    device_type="cisco_ios",
    host=r3["ip"],
    username=creds["username"],
    password=creds["password"],
)

conn.send_config_set([
    "interface g0/2",
    "ip address 10.10.10.6 255.255.255.252",
    "no shutdown",

    "interface g0/3",
    "ip address 10.10.10.10 255.255.255.252",
    "no shutdown",  
])

output = conn.send_command("show ip int b")
print(output)

conn.disconnect()