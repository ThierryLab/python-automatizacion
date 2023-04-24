from netmiko import ConnectHandler

switch1 = "198.18.190.94"

dev1 = {
    "device_type": "cisco_ios",
    "host": switch1,
    "username": "cisco",
    "password": "cisco",
}

with ConnectHandler(**dev1) as dev_connect:
    result = dev_connect.send_command("show vlan brief")
    print(result)
