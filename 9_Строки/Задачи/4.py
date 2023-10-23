def zeros(ip):
    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    return new_ip
print(zeros("192.280.03.04"))
