# This Python file uses the following encoding: utf-8

from http.server import HTTPServer
from server import Server

HOST_NAME = 'localhost'
PORT = 1729

if __name__ == '__main__':
  httpd = HTTPServer((HOST_NAME, PORT), Server)

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  httpd.server_close()
