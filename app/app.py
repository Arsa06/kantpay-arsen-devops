import os
import http.server
import socketserver
PORT = 8088
name = os.getenv("STUDENT_NAME", "Arsen")
surname = os.getenv("STUDENT_SURNAME", "Kantpay")
group = os.getenv("STUDENT_GROUP", "IT2-207")
student_id = os.getenv("STUDENT_ID", "37705")
print("================================")
print("DevOps Student Application")
print("================================")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Group: {group}")
print(f"Student ID: {student_id}")
print("Application is running successfully!", flush=True)
class HealthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            banner = f"DevOps Student Application\nName: {name} {surname}\nGroup: {group}\nID: {student_id}\n"
            self.wfile.write(banner.encode('utf-8'))
if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), HealthHandler) as httpd:
        httpd.serve_forever()
