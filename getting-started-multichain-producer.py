import mcrpc

client = mcrpc.RpcClient('192.168.2.8','7755','multichainrpc','BzKimVP5z5zpsWLUN4yEQ9JnkW6qdfvjkvEtCadZZDE3')

client.getinfo()
