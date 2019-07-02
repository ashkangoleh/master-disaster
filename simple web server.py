import http.server
import socketserver




hlr = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('',5000),hlr) as htpd:
    htpd.serve_forever()