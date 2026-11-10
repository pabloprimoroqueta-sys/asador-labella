# Servidor local de vista previa (solo para revisar la web en este ordenador).
# Envía cabeceras "no-store" para que el navegador muestre siempre la última versión.
import http.server, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()

http.server.ThreadingHTTPServer(("127.0.0.1", PORT), NoCache).serve_forever()
