from netmiko import ConnectHandler

device = {
     "device_type": "cisco_ios",
        "ip": "50.50.50.11",
        "username": "admin",
        "password": "Test123",
        "secret": "Test123",
}

 
net_connect = ConnectHandler(**device)
output = net_connect.send_command('enable')   


interface = 'interface Ethernet0/0'  
port_security_commands = [
    'switchport mode access',
    'switchport port-security',
    'switchport port-security maximum 1',
    'switchport port-security mac-address sticky',
    'switchport port-security violation Shutdown',
]
config_commands = [interface] + port_security_commands
output = net_connect.send_config_set(config_commands)

output = net_connect.send_command('show run ' + interface)


net_connect.disconnect()


print(output)