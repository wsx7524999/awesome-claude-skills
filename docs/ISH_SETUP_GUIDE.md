# iSH Setup Guide for iOS

This guide walks you through setting up iSH on iOS to run the Australian Academic Resources API server.

## Table of Contents

1. [What is iSH?](#what-is-ish)
2. [Installation](#installation)
3. [Initial Setup](#initial-setup)
4. [Installing Python](#installing-python)
5. [Installing Git](#installing-git)
6. [Cloning the Repository](#cloning-the-repository)
7. [Running the Server](#running-the-server)
8. [Accessing via Safari](#accessing-via-safari)
9. [Tips and Tricks](#tips-and-tricks)
10. [Troubleshooting](#troubleshooting)

## What is iSH?

iSH is a Linux shell environment that runs on iOS devices (iPhone and iPad). It provides:
- A full Alpine Linux environment
- Access to package managers (apk)
- Ability to run command-line tools
- Python, Git, and other development tools
- Local server hosting capabilities

Perfect for mobile development and testing!

## Installation

### Step 1: Install iSH from the App Store

1. Open the **App Store** on your iOS device
2. Search for "**iSH Shell**"
3. Download and install the app (it's free!)
4. Open iSH after installation

You should see a terminal prompt that looks like this:
```
localhost:~#
```

## Initial Setup

### Step 2: Update Package Repository

First, update the Alpine Linux package repository:

```bash
apk update
```

This fetches the latest package information.

### Step 3: Upgrade Existing Packages (Optional)

```bash
apk upgrade
```

This ensures all system packages are up to date.

## Installing Python

### Step 4: Install Python 3

```bash
apk add python3
```

### Step 5: Verify Python Installation

```bash
python3 --version
```

You should see something like:
```
Python 3.11.x
```

## Installing Git

### Step 6: Install Git

```bash
apk add git
```

### Step 7: Configure Git (Optional but Recommended)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 8: Verify Git Installation

```bash
git --version
```

## Cloning the Repository

### Step 9: Navigate to Home Directory

```bash
cd ~
```

### Step 10: Clone the Repository

```bash
git clone https://github.com/wsx7524999/awesome-claude-skills.git
```

### Step 11: Navigate to Repository

```bash
cd awesome-claude-skills
```

### Step 12: Verify Files

```bash
ls -la
```

You should see the repository structure including:
- `metadata/` - Contains the academic resources data
- `server/` - Contains the API server
- `docs/` - Documentation
- `README.md`

## Running the Server

### Step 13: Navigate to Server Directory

```bash
cd server
```

### Step 14: Start the Server

```bash
python3 ishserver.py
```

You should see output like:
```
Starting Australian Academic Resources API server...
Server running at http://127.0.0.1:8000/
Press Ctrl+C to stop the server

Available endpoints:
  - http://127.0.0.1:8000/              - API information
  - http://127.0.0.1:8000/resources     - List all resources
  - http://127.0.0.1:8000/resources/<id> - Get resource by ID
  - http://127.0.0.1:8000/search?q=<query> - Search resources
```

**Important:** Keep iSH running in the background or foreground for the server to stay active.

### Step 15: Run Server in Background (Optional)

If you want to use iSH for other tasks while the server runs:

```bash
python3 ishserver.py &
```

To bring it back to the foreground:
```bash
fg
```

To stop the background server:
```bash
# Find the process
ps aux | grep ishserver

# Kill it (replace PID with actual process ID)
kill <PID>
```

## Accessing via Safari

### Step 16: Open Safari

1. Open **Safari** on your iOS device
2. Navigate to: `http://localhost:8000/`

### Step 17: Try Different Endpoints

In Safari's address bar, try:

**API Information:**
```
http://localhost:8000/
```

**List All Resources:**
```
http://localhost:8000/resources
```

**Get Specific Resource:**
```
http://localhost:8000/resources/991001576278503441
```

**Search Resources:**
```
http://localhost:8000/search?q=statistics
```

### Step 18: Bookmark for Quick Access (Optional)

1. In Safari, tap the **Share** button
2. Select **Add to Favorites** or **Add to Reading List**
3. Name it "Academic Resources API"

## Tips and Tricks

### Multitasking

- **Split View:** On iPad, use Split View to have iSH and Safari side by side
- **Slide Over:** On iPhone/iPad, use Slide Over to quickly switch between apps
- **App Switcher:** Double-tap home button (or swipe up) to switch between iSH and Safari

### iSH Keyboard Shortcuts

- **Ctrl+C:** Stop the current process
- **Ctrl+D:** Exit/logout
- **Ctrl+Z:** Suspend current process
- **Tab:** Auto-complete commands and filenames
- **Up Arrow:** Previous command
- **Down Arrow:** Next command

### Useful Commands

```bash
# Check current directory
pwd

# List files
ls -la

# View file contents
cat filename

# Edit files (using vi)
vi filename

# Search command history
history | grep keyword

# Clear screen
clear
```

### Persistent Sessions

iSH sessions persist even when you close the app! Just reopen iSH to return to your previous state.

### External Keyboard Support

iSH works great with external keyboards (Bluetooth or Smart Keyboard). This makes typing commands much easier!

## Troubleshooting

### Server Won't Start

**Problem:** `Address already in use` error

**Solution:**
```bash
# Find and kill the existing process
ps aux | grep python
kill <PID>

# Or use a different port
python3 ishserver.py 8080
```

### Cannot Access in Safari

**Problem:** Safari shows "Cannot connect to server"

**Solutions:**
1. Make sure the server is running in iSH
2. Check that you're using `http://` not `https://`
3. Try `http://127.0.0.1:8000/` instead of `localhost`
4. Make sure iSH is running in the background

### iSH Crashes or Freezes

**Solutions:**
1. Force quit iSH and reopen it
2. Update iSH to the latest version from App Store
3. Restart your iOS device
4. Check if storage is full

### Git Clone Fails

**Problem:** Network errors during clone

**Solutions:**
1. Check your internet connection
2. Try again (sometimes it's just temporary)
3. Clone over HTTPS instead of SSH
4. If repository is large, try cloning with depth limit:
   ```bash
   git clone --depth 1 https://github.com/wsx7524999/awesome-claude-skills.git
   ```

### Python Not Found

**Problem:** `python3: command not found`

**Solution:**
```bash
# Update package list
apk update

# Install Python
apk add python3

# Verify
python3 --version
```

### Permission Denied Errors

**Problem:** Cannot execute scripts

**Solution:**
```bash
# Make script executable
chmod +x ishserver.py

# Or run directly with Python
python3 ishserver.py
```

### Out of Storage Space

**Problem:** Cannot install packages or clone repositories

**Solutions:**
1. Clear Safari cache and data
2. Delete unused apps
3. Check iSH disk usage:
   ```bash
   df -h
   ```
4. Clean up unnecessary files:
   ```bash
   # Remove package cache
   rm -rf /var/cache/apk/*
   ```

## Advanced: Installing Additional Tools

### Text Editors

```bash
# Vim (enhanced vi)
apk add vim

# Nano (easier for beginners)
apk add nano
```

### Node.js (if needed)

```bash
apk add nodejs npm
node --version
```

### Other Useful Tools

```bash
# Curl (for API testing)
apk add curl

# Wget (for downloading files)
apk add wget

# Htop (system monitor)
apk add htop
```

## Next Steps

Now that you have iSH set up and the server running, check out:

- [iOS Development Environment Guide](IOS_DEV_ENVIRONMENT.md) - Learn about iOS development workflows
- [Server README](../server/README.md) - Detailed server documentation
- Explore the metadata in `metadata/` directory

## Additional Resources

- [iSH GitHub Repository](https://github.com/ish-app/ish)
- [iSH Wiki](https://github.com/ish-app/ish/wiki)
- [Alpine Linux Documentation](https://wiki.alpinelinux.org/)

---

**Happy coding on iOS! 🚀**
