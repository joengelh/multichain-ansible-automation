import mcrpc

client = mcrpc.RpcClient('192.168.2.11','7755','multichainrpc','CbBLBkWNvtJtesiixQkGfBsMQQKhEe78vtRpzm7wyPnq')

#print(client.getinfo())
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"hpeserver",1)
#print(client.listaddresses())
print(client.listassets())
client.send("1XXXXXXWrHXXXXXXQtXXXXXXYcXXXXXXZaY3hj","60-265-64467","1")





