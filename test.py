import mcrpc

client = c = mcrpc.RpcClient('192.168.2.8','7755','multichainrpc', 'HQYxx31kGsdUsV5Q2THPkpbzUyBaNe5i2Xv6ZW7MiMLe')

print(client.listaddresses())
