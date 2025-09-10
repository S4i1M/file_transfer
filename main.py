import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# It can be customized
PORT = 8010

# Set working directory to OneDrive (or Desktop if preferred)
desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive')
os.chdir(desktop)

# Create HTTP handler
Handler = http.server.SimpleHTTPRequestHandler

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
s.close()

# Generate QR code locally 
url = pyqrcode.create(IP)
url.svg("myqr.svg", scale=8)

# Open QR code in browser
webbrowser.open("myqr.svg")

# Start server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser:", IP)
    print("Or scan the QR code")
    httpd.serve_forever()
