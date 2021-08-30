import mcrpc

client = mcrpc.RpcClient('192.168.2.2','7755','multichainrpc','BzKimVP5z5zpsWLUN4yEQ9JnkW6qdfvjkvEtCadZZDE3')

print(client.getinfo())
