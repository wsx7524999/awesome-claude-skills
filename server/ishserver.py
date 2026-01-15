#!/usr/bin/env python3
"""
iSH-compatible local server for Australian academic resources metadata.
Uses only Python standard library for compatibility with iSH on iOS.
"""

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class MetadataHandler(BaseHTTPRequestHandler):
    """HTTP request handler for metadata API endpoints."""
    
    def _send_json_response(self, data, status=200):
        """Send JSON response with proper headers."""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def _send_error_response(self, message, status=404):
        """Send error response in JSON format."""
        self._send_json_response({'error': message}, status)
    
    def _load_resources(self):
        """Load resources from JSON file."""
        metadata_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'metadata',
            'australian-academic-resources.json'
        )
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        # Root endpoint - API information
        if path == '/' or path == '':
            self._send_json_response({
                'name': 'Australian Academic Resources API',
                'version': '1.0',
                'endpoints': {
                    '/': 'API information',
                    '/resources': 'List all resources',
                    '/resources/<id>': 'Get resource by ID',
                    '/search?q=<query>': 'Search resources by title'
                }
            })
            return
        
        # List all resources
        if path == '/resources' or path == '/resources/':
            resources = self._load_resources()
            self._send_json_response({
                'count': len(resources),
                'resources': resources
            })
            return
        
        # Get resource by ID
        if path.startswith('/resources/'):
            resource_id = path.split('/resources/')[1].strip('/')
            resources = self._load_resources()
            
            for resource in resources:
                if resource.get('id') == resource_id:
                    self._send_json_response(resource)
                    return
            
            self._send_error_response(f'Resource with ID {resource_id} not found')
            return
        
        # Search resources
        if path == '/search' or path == '/search/':
            query = query_params.get('q', [''])[0].lower()
            if not query:
                self._send_error_response('Search query parameter "q" is required', 400)
                return
            
            resources = self._load_resources()
            results = [
                r for r in resources
                if query in r.get('title', '').lower()
            ]
            
            self._send_json_response({
                'query': query,
                'count': len(results),
                'results': results
            })
            return
        
        # Not found
        self._send_error_response('Endpoint not found')
    
    def log_message(self, format, *args):
        """Override to customize log messages."""
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=8000, host='127.0.0.1'):
    """Start the HTTP server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, MetadataHandler)
    
    print(f"Starting Australian Academic Resources API server...")
    print(f"Server running at http://{host}:{port}/")
    print(f"Press Ctrl+C to stop the server")
    print()
    print("Available endpoints:")
    print(f"  - http://{host}:{port}/              - API information")
    print(f"  - http://{host}:{port}/resources     - List all resources")
    print(f"  - http://{host}:{port}/resources/<id> - Get resource by ID")
    print(f"  - http://{host}:{port}/search?q=<query> - Search resources")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()


if __name__ == '__main__':
    import sys
    
    # Default port
    port = 8000
    host = '127.0.0.1'
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            sys.exit(1)
    
    if len(sys.argv) > 2:
        host = sys.argv[2]
    
    run_server(port, host)
