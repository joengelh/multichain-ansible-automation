import mcrpc

client = mcrpc.RpcClient('192.168.2.8','7755','multichainrpc','HQYxx31kGsdUsV5Q2THPkpbzUyBaNe5i2Xv6ZW7MiMLe')

client.grant("1XXXXXXWrHXXXXXXQtXXXXXXYcXXXXXXZaY3hj","receive")
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"dellserver",600,1)
print(client.listassets())
print(client.sendasset("1XXXXXXWrHXXXXXXQtXXXXXXYcXXXXXXZaY3hj","65-266-2074",1))

