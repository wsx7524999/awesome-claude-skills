# Australian Academic Resources API Server

A lightweight, iSH-compatible local server for serving Australian academic resources metadata.

## Features

- **iSH Compatible**: Uses only Python standard library - works perfectly in iSH on iOS
- **Simple REST API**: Easy-to-use endpoints for accessing metadata
- **No Dependencies**: No pip packages required, just Python 3
- **Cross-platform**: Works on macOS, Linux, Windows, and iOS (via iSH)

## Requirements

- Python 3.x (standard library only)

## Quick Start

### On Desktop (macOS, Linux, Windows)

```bash
# Navigate to the server directory
cd server

# Run the server (default port 8000)
python3 ishserver.py

# Or specify a custom port
python3 ishserver.py 8080

# Or specify port and host
python3 ishserver.py 8080 0.0.0.0
```

### In iSH on iOS

```bash
# Navigate to the server directory
cd /path/to/awesome-claude-skills/server

# Run the server
python3 ishserver.py

# Access from Safari at: http://localhost:8000/
```

## API Endpoints

### 1. API Information
**GET** `/`

Returns information about the API and available endpoints.

```bash
curl http://localhost:8000/
```

### 2. List All Resources
**GET** `/resources`

Returns all Australian academic resources.

```bash
curl http://localhost:8000/resources
```

**Response:**
```json
{
  "count": 8,
  "resources": [...]
}
```

### 3. Get Resource by ID
**GET** `/resources/<id>`

Returns a specific resource by its ID.

```bash
curl http://localhost:8000/resources/991001576278503441
```

**Response:**
```json
{
  "id": "991001576278503441",
  "title": "Australian Injectable Drugs Handbook (AIDH)",
  "leader": "00718nac",
  ...
}
```

### 4. Search Resources
**GET** `/search?q=<query>`

Searches resources by title (case-insensitive).

```bash
curl "http://localhost:8000/search?q=statistics"
```

**Response:**
```json
{
  "query": "statistics",
  "count": 1,
  "results": [...]
}
```

## Usage Examples

### View in Browser

1. Start the server: `python3 ishserver.py`
2. Open your browser to: `http://localhost:8000/`
3. Try different endpoints:
   - `http://localhost:8000/resources` - See all resources
   - `http://localhost:8000/resources/991001576278503441` - Get specific resource
   - `http://localhost:8000/search?q=legal` - Search for resources

### Using with curl

```bash
# List all resources
curl http://localhost:8000/resources | python3 -m json.tool

# Get specific resource
curl http://localhost:8000/resources/991001957267503441

# Search for resources
curl "http://localhost:8000/search?q=australian"
```

### Using with Python

```python
import urllib.request
import json

# Fetch all resources
response = urllib.request.urlopen('http://localhost:8000/resources')
data = json.loads(response.read())
print(f"Found {data['count']} resources")

# Search for resources
query = 'statistics'
response = urllib.request.urlopen(f'http://localhost:8000/search?q={query}')
results = json.loads(response.read())
for resource in results['results']:
    print(resource['title'])
```

## iSH-Specific Notes

### Running in Background (iSH)
In iSH, you can run the server in the background using `&`:

```bash
python3 ishserver.py &
```

To bring it back to foreground:
```bash
fg
```

To stop it:
```bash
# Find the process ID
ps aux | grep ishserver

# Kill the process
kill <PID>
```

### Port Considerations
- Default port 8000 works well for local development
- Use `127.0.0.1` (localhost) for local access only
- Use `0.0.0.0` to allow access from other devices on the network (not recommended for public networks)

## Troubleshooting

### "Address already in use" error
Another process is using port 8000. Either:
- Stop the other process
- Use a different port: `python3 ishserver.py 8080`

### "Module not found" error
Make sure you're using Python 3:
```bash
python3 --version
```

### Cannot access from Safari
- Make sure the server is running (check the terminal)
- Use `http://localhost:8000/` (not `https://`)
- Try `http://127.0.0.1:8000/` instead

### File not found errors
Make sure you're running the server from the repository's `server` directory, or that the metadata files are in the correct relative location (`../metadata/`).

## Development

The server uses Python's built-in `http.server` module, making it:
- Lightweight and fast
- Easy to understand and modify
- Compatible with minimal Python installations (including iSH)

No external dependencies means no `pip install` required!

## Security Note

This server is designed for **local development only**. Do not expose it to public networks without proper security measures (authentication, HTTPS, etc.).
