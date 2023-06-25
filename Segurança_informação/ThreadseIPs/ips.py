import ipaddress

ip = '192.168.0.1'

address = ipaddress.ip_address(ip)

print(address)
print(type(address))
print(ip)
print(type(ip))

# rede

ip = '192.168.0.0/24'

net = ipaddress.ip_network(ip)
# net = ipaddress.ip_network(ip, strict=False)

print(net)
print(type(net))

for ip in net:
    print(ip)
