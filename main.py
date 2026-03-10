from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

# usuario, senha, pasta, permissões
authorizer.add_user("ruan", "1234", ".", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 8080), handler)

print("FTP rodando na porta 8080...")
server.serve_forever()
