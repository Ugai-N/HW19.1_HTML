from http.server import HTTPServer
from utils import MyServer

hostName = "localhost"
serverPort = 8080

webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()
print("Server stopped.")
