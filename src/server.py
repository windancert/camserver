# This Python file uses the following encoding: utf-8

from routes import routes
from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
  
  def do_HEAD(self):
    return
  
  def do_POST(self):
    return
  
  def do_GET(self):
    self.respond()
  
  def handle_http(self, status, content_type):
    self.send_response(status)
    self.send_header('Content-type', content_type)
    self.end_headers()
    return bytes('Hello world!', 'UTF-8')
  
  def respond(self):
    content = self.handle_http(200, 'text/html')
    self.wfile.write(content)
