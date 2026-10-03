"""Small browser dashboard for the Orange Pi robot."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import webbrowser, html
def open_chrome(url):
    import shutil, subprocess, os, webbrowser
    candidates=["google-chrome","google-chrome-stable","chromium","chromium-browser","chrome"]
    for name in candidates:
        exe=shutil.which(name)
        if exe:
            subprocess.Popen([exe,url]); return
    if os.name=="nt":
        for p in [r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"]:
            if os.path.exists(p): subprocess.Popen([p,url]); return
    open_chrome(url)

HOST,PORT="127.0.0.1",8770
PAGE="""<!doctype html><html><head><meta charset="utf-8"><title>Orange Pi Robot</title><style>body{font-family:Arial;max-width:800px;margin:40px auto;padding:20px;background:#f5f7fb}.card{background:white;padding:25px;border-radius:14px}button{padding:14px 20px;margin:5px;font-size:16px}</style></head><body><div class="card"><h1>Orange Pi Robot 🤖</h1><p>Simple browser control panel. Hardware commands are sent only when the robot program is running.</p><button onclick="send('forward')">Forward</button><button onclick="send('backward')">Backward</button><button onclick="send('left')">Left</button><button onclick="send('right')">Right</button><button onclick="send('stop')">Stop</button><p id="out">Ready.</p><script>async function send(c){let r=await fetch('/command?c='+encodeURIComponent(c));document.getElementById('out').textContent=await r.text()}</script></div></body></html>"""
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/command"):
            from urllib.parse import parse_qs,urlparse
            c=parse_qs(urlparse(self.path).query).get("c",[""])[0]
            self.send_text("Browser command received: "+c+" (connect this endpoint to the robot command layer when hardware control is enabled)."); return
        self.send_text(PAGE,"text/html")
    def send_text(self,s,typ="text/plain"):
        b=s.encode(); self.send_response(200); self.send_header("Content-Type",typ+"; charset=utf-8"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
if __name__=="__main__":
    server=ThreadingHTTPServer((HOST,PORT),H); url=f"http://{HOST}:{PORT}"; print(url); webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
