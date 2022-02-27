list1 = []
myfile = open(file="nginx_logs.txt",mode="r",encoding="utf-8")
for line in myfile:
    remote_addr = line.split(" - - ")[0]
    request = line.split('"')[1]
    request_type = request.split()[0]
    requested_resource = request.split()[1]
    list1.append((remote_addr, request_type, requested_resource))
myfile.close()

#print(list1)

for x in list1:
    print(x)