#!/usr/bin/env python3
"""
iSH-Compatible HTTP Server for Metadata Management
Lightweight REST API server using only Python standard library
Designed to run on iOS via iSH terminal emulator
"""

import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path

# Configuration
CONFIG_FILE = "config.json"
DEFAULT_PORT = 8080
DEFAULT_HOST = "0.0.0.0"

class MetadataServer(BaseHTTPRequestHandler):
    """HTTP Request Handler for metadata API"""
    
    # Base directory for file paths
    base_dir = Path(__file__).parent.parent
    
    def load_resources(self):
        """Load resources from JSON file"""
        try:
            resources_path = self.base_dir / "metadata" / "australian-resources.json"
            with open(resources_path, 'r') as f:
                data = json.load(f)
                return data.get('resources', [])
        except Exception as e:
            print(f"Error loading resources: {e}")
            return []
    
    def load_user_metadata(self):
        """Load user metadata from JSON file"""
        try:
            user_path = self.base_dir / "metadata" / "user-metadata.json"
            with open(user_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading user metadata: {e}")
            return {}
    
    def send_json_response(self, data, status=200):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))
    
    def send_html_response(self, html, status=200):
        """Send HTML response"""
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        # Root endpoint - API documentation
        if path == '/':
            self.handle_root()
        
        # Get all resources
        elif path == '/api/resources':
            self.handle_get_resources()
        
        # Search resources
        elif path.startswith('/api/resources/search'):
            query = query_params.get('q', [''])[0]
            self.handle_search_resources(query)
        
        # Get specific resource by ID
        elif path.startswith('/api/resources/'):
            resource_id = path.split('/')[-1]
            if resource_id and resource_id != 'search':
                self.handle_get_resource(resource_id)
            else:
                self.send_json_response({"error": "Invalid resource ID"}, 400)
        
        # Get user metadata
        elif path == '/api/user':
            self.handle_get_user()
        
        # 404 Not Found
        else:
            self.send_json_response({"error": "Endpoint not found"}, 404)
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        # Add new resource (if enabled)
        if path == '/api/resources':
            self.handle_add_resource()
        else:
            self.send_json_response({"error": "Endpoint not found"}, 404)
    
    def handle_root(self):
        """Handle root endpoint - API documentation"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>iSH Metadata API Server</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; 
               max-width: 900px; margin: 40px auto; padding: 0 20px; 
               background: #f5f5f7; color: #1d1d1f; }
        h1 { color: #06c; border-bottom: 2px solid #06c; padding-bottom: 10px; }
        h2 { color: #333; margin-top: 30px; }
        .endpoint { background: white; padding: 15px; margin: 10px 0; 
                    border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .method { display: inline-block; padding: 4px 12px; border-radius: 4px; 
                  font-weight: bold; margin-right: 10px; }
        .get { background: #28a745; color: white; }
        .post { background: #007bff; color: white; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; 
               font-family: 'Monaco', 'Courier New', monospace; }
        .status { color: #28a745; font-weight: bold; }
        a { color: #06c; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📱 iSH Metadata API Server</h1>
    <p class="status">✅ Server is running</p>
    <p>Lightweight REST API for Australian academic resources metadata.</p>
    
    <h2>📚 Available Endpoints</h2>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/</code>
        <p>Server status and API documentation (this page)</p>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/resources</code>
        <p>List all resources</p>
        <p><a href="/api/resources">Try it →</a></p>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/resources/:id</code>
        <p>Get specific resource by ID</p>
        <p>Example: <a href="/api/resources/abs-002">/api/resources/abs-002</a></p>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/resources/search?q=query</code>
        <p>Search resources by keyword in title, description, or subjects</p>
        <p>Example: <a href="/api/resources/search?q=statistics">/api/resources/search?q=statistics</a></p>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/user</code>
        <p>Get user metadata and profile</p>
        <p><a href="/api/user">Try it →</a></p>
    </div>
    
    <div class="endpoint">
        <span class="method post">POST</span>
        <code>/api/resources</code>
        <p>Add new resource (read-only mode - not implemented)</p>
    </div>
    
    <h2>💡 Usage Examples</h2>
    <p>Using curl:</p>
    <pre><code>curl http://localhost:8080/api/resources
curl http://localhost:8080/api/resources/abs-002
curl "http://localhost:8080/api/resources/search?q=data"
curl http://localhost:8080/api/user</code></pre>
    
    <h2>🔗 Quick Links</h2>
    <p>
        <a href="/api/resources">All Resources</a> | 
        <a href="/api/user">User Profile</a> | 
        <a href="/api/resources/search?q=open">Search "open"</a>
    </p>
    
    <p style="margin-top: 40px; color: #86868b; font-size: 0.9em;">
        iSH-Compatible Metadata Server v1.0 | Python Standard Library Only
    </p>
</body>
</html>
        """
        self.send_html_response(html)
    
    def handle_get_resources(self):
        """Handle GET /api/resources - return all resources"""
        resources = self.load_resources()
        response = {
            "success": True,
            "count": len(resources),
            "resources": resources
        }
        self.send_json_response(response)
    
    def handle_get_resource(self, resource_id):
        """Handle GET /api/resources/:id - return specific resource"""
        resources = self.load_resources()
        resource = next((r for r in resources if r.get('id') == resource_id), None)
        
        if resource:
            response = {
                "success": True,
                "resource": resource
            }
            self.send_json_response(response)
        else:
            response = {
                "success": False,
                "error": f"Resource with ID '{resource_id}' not found"
            }
            self.send_json_response(response, 404)
    
    def handle_search_resources(self, query):
        """Handle GET /api/resources/search?q=query - search resources"""
        if not query:
            self.send_json_response({
                "success": False,
                "error": "Query parameter 'q' is required"
            }, 400)
            return
        
        resources = self.load_resources()
        query_lower = query.lower()
        
        # Search in title, description, and subjects
        results = []
        for resource in resources:
            if (query_lower in resource.get('title', '').lower() or
                query_lower in resource.get('description', '').lower() or
                query_lower in resource.get('alternateTitle', '').lower() or
                any(query_lower in subject.lower() for subject in resource.get('subjects', []))):
                results.append(resource)
        
        response = {
            "success": True,
            "query": query,
            "count": len(results),
            "results": results
        }
        self.send_json_response(response)
    
    def handle_get_user(self):
        """Handle GET /api/user - return user metadata"""
        user_data = self.load_user_metadata()
        if user_data:
            response = {
                "success": True,
                "user": user_data
            }
            self.send_json_response(response)
        else:
            response = {
                "success": False,
                "error": "User metadata not found"
            }
            self.send_json_response(response, 404)
    
    def handle_add_resource(self):
        """Handle POST /api/resources - add new resource"""
        # Read-only mode for now
        response = {
            "success": False,
            "error": "POST endpoint not implemented. Server is in read-only mode."
        }
        self.send_json_response(response, 501)
    
    def log_message(self, format, *args):
        """Custom log message format"""
        sys.stdout.write("%s - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))


def load_server_config():
    """Load server configuration"""
    config_path = Path(__file__).parent / CONFIG_FILE
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
            # Return flattened config for backward compatibility
            return {
                "host": config.get("server", {}).get("host", DEFAULT_HOST),
                "port": config.get("server", {}).get("port", DEFAULT_PORT),
                "full_config": config
            }
    return {
        "port": DEFAULT_PORT,
        "host": DEFAULT_HOST,
        "full_config": {}
    }


def run_server():
    """Start the HTTP server"""
    config = load_server_config()
    host = config.get('host', DEFAULT_HOST)
    port = config.get('port', DEFAULT_PORT)
    
    server_address = (host, port)
    httpd = HTTPServer(server_address, MetadataServer)
    
    print("=" * 60)
    print("🚀 iSH Metadata API Server")
    print("=" * 60)
    print(f"📡 Server running on http://{host}:{port}")
    print(f"📱 Access from iPhone: http://localhost:{port}")
    print(f"🌐 API Endpoints:")
    print(f"   • GET  /api/resources       - List all resources")
    print(f"   • GET  /api/resources/:id   - Get specific resource")
    print(f"   • GET  /api/resources/search?q=query - Search resources")
    print(f"   • GET  /api/user            - Get user metadata")
    print(f"\n💡 Open http://localhost:{port} in your browser for documentation")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
        httpd.server_close()
        sys.exit(0)


if __name__ == '__main__':
    run_server()
