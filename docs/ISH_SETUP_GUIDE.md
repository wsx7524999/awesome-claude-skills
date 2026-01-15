# iSH Setup Guide for iPhone/iPad

Complete step-by-step instructions for running the awesome-claude-skills metadata server on iOS using iSH.

## Table of Contents
1. [What is iSH?](#what-is-ish)
2. [Installing iSH](#installing-ish)
3. [Setting Up Python](#setting-up-python)
4. [Installing Git](#installing-git)
5. [Cloning the Repository](#cloning-the-repository)
6. [Running the Server](#running-the-server)
7. [Accessing Metadata](#accessing-metadata)
8. [Troubleshooting](#troubleshooting)

## What is iSH?

iSH is a Linux shell environment for iOS that allows you to run command-line programs and scripts on your iPhone or iPad. It provides:
- Alpine Linux environment
- Package manager (apk)
- Python, Git, and other development tools
- Local file system access
- Network capabilities

Perfect for running lightweight servers and development tools on iOS!

## Installing iSH

### Step 1: Download from App Store

1. Open the **App Store** on your iPhone or iPad
2. Search for **"iSH Shell"**
3. Download and install the app (it's free!)
4. Open iSH after installation

### Step 2: First Launch

When you first open iSH, you'll see a terminal interface with a command prompt:
```
localhost:~#
```

This is your Linux shell running on iOS! 🎉

## Setting Up Python

iSH comes with Alpine Linux, which uses the `apk` package manager.

### Step 1: Update Package Lists

```bash
apk update
```

This updates the package repository lists. Wait for it to complete.

### Step 2: Install Python 3

```bash
apk add python3
```

This installs Python 3 (typically Python 3.9 or later).

### Step 3: Verify Installation

```bash
python3 --version
```

You should see output like: `Python 3.9.x` or similar.

### Step 4: Install pip (Python Package Manager)

```bash
apk add py3-pip
```

This is optional but useful for future package installations.

## Installing Git

### Step 1: Install Git

```bash
apk add git
```

### Step 2: Configure Git (Optional)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Verify Installation

```bash
git --version
```

You should see output like: `git version 2.x.x`

## Cloning the Repository

### Step 1: Navigate to Home Directory

```bash
cd ~
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/wsx7524999/awesome-claude-skills.git
```

Wait for the clone to complete. This might take a minute depending on your connection.

### Step 3: Navigate to Repository

```bash
cd awesome-claude-skills
```

### Step 4: Verify Files

```bash
ls -la
```

You should see the repository files including:
- `README.md`
- `metadata/` directory
- `server/` directory
- `docs/` directory

## Running the Server

### Step 1: Navigate to Server Directory

```bash
cd ~/awesome-claude-skills/server
```

### Step 2: Make Server Script Executable

```bash
chmod +x ishserver.py
```

### Step 3: Start the Server

```bash
python3 ishserver.py
```

You should see output like:
```
============================================================
🚀 iSH Metadata API Server
============================================================
📡 Server running on http://0.0.0.0:8080
📱 Access from iPhone: http://localhost:8080
🌐 API Endpoints:
   • GET  /api/resources       - List all resources
   • GET  /api/resources/:id   - Get specific resource
   • GET  /api/resources/search?q=query - Search resources
   • GET  /api/user            - Get user metadata

💡 Open http://localhost:8080 in your browser for documentation
============================================================
Press Ctrl+C to stop the server
```

### Step 4: Keep Server Running

⚠️ **Important:** Keep the iSH app open and don't let your device sleep, or the server will stop.

To run the server in the background:
1. Keep iSH in foreground
2. Or use `nohup` command (advanced):
   ```bash
   nohup python3 ishserver.py > server.log 2>&1 &
   ```

## Accessing Metadata

### From Safari on the Same Device

1. Open **Safari** browser on your iPhone/iPad
2. Navigate to: `http://localhost:8080`
3. You'll see the API documentation page
4. Click on links to explore different endpoints

### Available Endpoints

#### 1. Home Page / API Documentation
```
http://localhost:8080/
```
Shows all available endpoints and usage examples.

#### 2. List All Resources
```
http://localhost:8080/api/resources
```
Returns JSON with all 8 Australian academic resources.

#### 3. Get Specific Resource
```
http://localhost:8080/api/resources/abs-002
```
Returns details for the Australian Bureau of Statistics.

Other resource IDs:
- `aidh-001` - Australian Injectable Drugs Handbook
- `abs-002` - Australian Bureau of Statistics
- `abares-003` - ABARES
- `proquest-004` - Australia & NZ Newsstream
- `austlii-005` - AustLII
- `ardc-006` - ARDC Research Data Australia
- `apo-007` - Analysis & Policy Observatory
- `ada-008` - ADA Dataverse

#### 4. Search Resources
```
http://localhost:8080/api/resources/search?q=statistics
```
Searches for "statistics" in titles, descriptions, and subjects.

Try searching for:
- `data` - finds data-related resources
- `research` - finds research resources
- `open` - finds open access resources
- `law` - finds legal resources

#### 5. User Profile
```
http://localhost:8080/api/user
```
Returns user metadata and profile information.

### Using curl in iSH

You can also test the API from within iSH using curl:

```bash
# Install curl first
apk add curl

# Test endpoints
curl http://localhost:8080/api/resources
curl http://localhost:8080/api/resources/abs-002
curl "http://localhost:8080/api/resources/search?q=data"
curl http://localhost:8080/api/user
```

### From Another Device on the Same Network

1. Find your iPhone's IP address:
   ```bash
   # In iSH
   ifconfig | grep inet
   ```
   Look for something like: `192.168.1.xxx`

2. On another device, navigate to:
   ```
   http://192.168.1.xxx:8080
   ```

⚠️ **Note:** This only works if both devices are on the same WiFi network.

## Troubleshooting

### Server Won't Start

**Problem:** Error message when starting server

**Solutions:**
1. Check Python is installed:
   ```bash
   python3 --version
   ```

2. Verify you're in the correct directory:
   ```bash
   pwd
   # Should show: /root/awesome-claude-skills/server
   ```

3. Check if port 8080 is already in use:
   ```bash
   netstat -an | grep 8080
   ```
   If in use, edit `config.json` to use a different port.

### Can't Access in Browser

**Problem:** Safari shows "Cannot connect to server"

**Solutions:**
1. Verify server is running in iSH (should see server logs)
2. Check you're using `http://` not `https://`
3. Try `http://127.0.0.1:8080` instead of `localhost`
4. Make sure iSH is running in foreground

### Server Stops When Switching Apps

**Problem:** Server stops when leaving iSH

**Solutions:**
1. Keep iSH in foreground while using server
2. Use Split View on iPad to see both iSH and Safari
3. Disable auto-lock: Settings → Display & Brightness → Auto-Lock → Never
4. Use a background process (advanced):
   ```bash
   nohup python3 ishserver.py &
   ```

### Slow Performance

**Problem:** Server responds slowly

**Solutions:**
1. Close other apps to free memory
2. Restart iSH app
3. Restart your device
4. Reduce server timeout in `config.json`

### File Not Found Errors

**Problem:** Server can't find metadata files

**Solutions:**
1. Verify files exist:
   ```bash
   ls -la ~/awesome-claude-skills/metadata/
   ```

2. Check you ran git clone successfully:
   ```bash
   cd ~/awesome-claude-skills
   git status
   ```

3. Re-clone if necessary:
   ```bash
   cd ~
   rm -rf awesome-claude-skills
   git clone https://github.com/wsx7524999/awesome-claude-skills.git
   ```

### Python Module Import Errors

**Problem:** Error about missing modules

**Solutions:**
1. The server uses only standard library - no extra packages needed
2. Update Python if very old:
   ```bash
   apk upgrade python3
   ```

## Tips & Best Practices

### 1. Save Battery
- Use Low Power Mode when running server for extended periods
- Keep screen brightness low
- Close unnecessary apps

### 2. Persistent Sessions
Create an alias for easy server startup:
```bash
echo 'alias startserver="cd ~/awesome-claude-skills/server && python3 ishserver.py"' >> ~/.profile
source ~/.profile
```

Now you can start the server with just:
```bash
startserver
```

### 3. Auto-Start on iSH Launch
Add to `~/.profile`:
```bash
echo 'cd ~/awesome-claude-skills/server && python3 ishserver.py &' >> ~/.profile
```

### 4. View Logs
If running in background, check logs:
```bash
tail -f ~/awesome-claude-skills/server/server.log
```

### 5. Update Repository
To get latest changes:
```bash
cd ~/awesome-claude-skills
git pull origin main
```

## Next Steps

- Read [iOS Development Environment](IOS_DEV_ENVIRONMENT.md) for advanced setup
- Check [Metadata Format](METADATA_FORMAT.md) to understand data structure
- Explore customizing the server in `server/ishserver.py`
- Add your own resources to the metadata files

## Additional Resources

- [iSH GitHub Repository](https://github.com/ish-app/ish)
- [Alpine Linux Documentation](https://wiki.alpinelinux.org/)
- [Python Documentation](https://docs.python.org/3/)

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section above
2. Review server logs for error messages
3. Open an issue on GitHub with details about your problem

---

**Last Updated:** 2026-01-15  
**Version:** 1.0  
**Platform:** iOS/iPadOS via iSH
