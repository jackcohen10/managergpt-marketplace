#!/usr/bin/env python3
"""Tiny local server for the interactive Leverage Quadrant on Codex (or any
in-app/local browser). Serves quadrant.html, feeds it the ranked items, and
captures the user's placements when they click "Complete and prep delegation".

Usage:
  python3 serve.py [port]

Before starting, write the ranked items to items.json next to this file:
  [{"n": "Project name", "imp": 80, "oth": 20}, ...]
  (imp = impact 0-100, oth = how much others-can-do 0-100; both default to 50)

Then open http://localhost:<port>/quadrant.html in the in-app browser.
On "Complete and prep delegation", the page POSTs to /save and this server
writes placements.json — the agent reads that to continue into Clean Handoffs.
"""
import json, os, sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def do_POST(self):
        if self.path.rstrip("/") == "/save":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body or b"[]")
            except json.JSONDecodeError:
                self.send_response(400); self.end_headers(); return
            with open(os.path.join(HERE, "placements.json"), "w") as f:
                json.dump(data, f, indent=2)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            print("Wrote placements.json")
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"Leverage Quadrant server on http://localhost:{PORT}/quadrant.html")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
