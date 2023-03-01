import random

# Generate 20 lists of 10 random IP addresses
for i in range(20):
    ip_list = []
    for j in range(10):
        octet1 = str(random.randint(0, 255))
        octet2 = str(random.randint(0, 255))
        octet3 = str(random.randint(0, 255))
        octet4 = str(random.randint(0, 255))
        ip_list.append(octet1 + "." + octet2 + "." + octet3 + "." + octet4)
    print(ip_list)
