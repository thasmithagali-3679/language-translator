from http.server import BaseHTTPRequestHandler
import json
from googletrans import Translator
from urllib.parse import parse_qs

translator = Translator()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_params = parse_qs(self.path.split('?')[1] if '?' in self.path else '')
        
        text = query_params.get('text', [''])[0]
        source_lang = query_params.get('source', ['en'])[0]
        target_lang = query_params.get('target', ['es'])[0]
        
        if not text:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Text parameter is required'}).encode())
            return
        
        try:
            result = translator.translate(text, src_language=source_lang, dest_language=target_lang)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': True,
                'original': text,
                'translated': result['text'],
                'source_language': source_lang,
                'target_language': target_lang
            }
            
            self.wfile.write(json.dumps(response).encode())
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': False,
                'error': str(e)
            }
            
            self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body.decode())
            text = data.get('text', '')
            source_lang = data.get('source', 'en')
            target_lang = data.get('target', 'es')
            
            if not text:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Text field is required'}).encode())
                return
            
            result = translator.translate(text, src_language=source_lang, dest_language=target_lang)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': True,
                'original': text,
                'translated': result['text'],
                'source_language': source_lang,
                'target_language': target_lang
            }
            
            self.wfile.write(json.dumps(response).encode())
        
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode())
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()