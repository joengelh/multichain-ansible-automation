import mcrpc

client = mcrpc.RpcClient('192.168.2.8','7755','multichainrpc','CbBLBkWNvtJtesiixQkGfBsMQQKhEe78vtRpzm7wyPnq')

client.getinfo()
