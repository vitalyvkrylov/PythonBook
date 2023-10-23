def zeros(ip):
    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    return new_ip
print(zeros("255.036.02.07"))
