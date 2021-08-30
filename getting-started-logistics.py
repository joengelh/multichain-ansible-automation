import mcrpc

client = mcrpc.RpcClient('192.168.2.13','7755','multichainrpc','25XYhe2UiJbzLVhd9TXfX9r2fHtCHtZx4DNLc1mcgUCA')

client.getinfo()
