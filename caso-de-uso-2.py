from netmiko import ConnectHandler

switch1 = "198.18.190.94"
switch2 = "198.18.190.93"
switch3 = "198.18.190.92"

dev1 = {
    "device_type": "cisco_ios",
    "host": switch1,
    "username": "cisco",
    "password": "cisco",
}
dev2 = {
    "device_type": "cisco_ios",
    "host": switch2,
    "username": "cisco",
    "password": "cisco",
}
dev3 = {
    "device_type": "cisco_ios",
    "host": switch3,
    "username": "cisco",
    "password": "cisco",
}
dev_list = [dev1, dev2, dev3]

for dev in dev_list:
    with ConnectHandler(**dev) as dev_connect:
        result = dev_connect.send_command("show version | in uptime")
        print(result)


