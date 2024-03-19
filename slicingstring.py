cidr_notation = "172.168.1.1/24"
ip_address = cidr_notation .split('/')[0]
print(ip_address)

first_octet = ip_address[:ip_address .index('.')]
print(first_octet)

second_octed_start = ip_address .index('.') + 1
second_octed_end = ip_address .index('.' , second_octed_start)
second_octed = ip_address[second_octed_start:second_octed_end]
print(second_octed)

subnet_mask = cidr_notation .split('/')[1]
print(subnet_mask)



