# iOS Development Environment Guide

A comprehensive guide for setting up and using an iOS development environment with iSH for the Australian Academic Resources project.

## Table of Contents

1. [Overview](#overview)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Text Editors for iOS](#text-editors-for-ios)
4. [Git Workflows on iOS](#git-workflows-on-ios)
5. [Running the Local Server](#running-the-local-server)
6. [Working with Python](#working-with-python)
7. [Working with Node.js (Optional)](#working-with-nodejs-optional)
8. [Development Best Practices](#development-best-practices)
9. [Recommended Workflows](#recommended-workflows)
10. [Tips for Mobile Development](#tips-for-mobile-development)

## Overview

This guide helps you set up a complete development environment on iOS using iSH, enabling you to:
- Edit code and documentation
- Run local servers
- Test APIs
- Manage version control with Git
- Work with Python and Node.js projects

### Prerequisites

Before starting, make sure you've completed the [iSH Setup Guide](ISH_SETUP_GUIDE.md).

## Setting Up Your Environment

### Essential Tools

Install the core development tools in iSH:

```bash
# Update package repository
apk update

# Install essential development tools
apk add git python3 py3-pip vim nano curl wget

# Optional but recommended
apk add nodejs npm htop tree
```

### Create a Development Directory Structure

```bash
# Create a dedicated development directory
mkdir -p ~/dev
cd ~/dev

# Clone your projects here
git clone https://github.com/wsx7524999/awesome-claude-skills.git
cd awesome-claude-skills
```

## Text Editors for iOS

### Option 1: vim (Powerful but Steep Learning Curve)

**Install:**
```bash
apk add vim
```

**Basic Usage:**
```bash
# Open a file
vim filename.py

# Edit mode: Press 'i'
# Exit edit mode: Press 'Esc'
# Save and quit: Type ':wq' and press Enter
# Quit without saving: Type ':q!' and press Enter
```

**Quick vim Cheat Sheet:**
- `i` - Enter insert mode
- `Esc` - Exit insert mode
- `:w` - Save file
- `:q` - Quit
- `:wq` - Save and quit
- `:q!` - Quit without saving
- `dd` - Delete line
- `yy` - Copy line
- `p` - Paste
- `/search` - Search for text
- `u` - Undo
- `Ctrl+r` - Redo

### Option 2: nano (Beginner-Friendly)

**Install:**
```bash
apk add nano
```

**Basic Usage:**
```bash
# Open a file
nano filename.py

# Commands shown at bottom:
# ^X - Exit (Ctrl+X)
# ^O - Save (Ctrl+O)
# ^K - Cut line
# ^U - Paste line
```

**Nano is recommended for beginners!**

### Option 3: External Apps (Recommended for Serious Development)

For a better mobile editing experience, consider these iOS apps:

1. **Working Copy** (Free with paid features)
   - Full-featured Git client
   - Built-in text editor with syntax highlighting
   - Can integrate with iSH file system
   - Supports pull requests and code review

2. **Textastic** (Paid)
   - Professional code editor
   - Syntax highlighting for 80+ languages
   - FTP/SFTP support
   - Can edit files in iSH directory

3. **Koder** (Paid)
   - Syntax highlighting
   - Code completion
   - Multiple tabs

**Workflow with External Apps:**
```bash
# In iSH, create symbolic link to iCloud or local files
ln -s /path/to/icloud/folder ~/dev/sync

# Edit files in external app
# Test changes in iSH
```

## Git Workflows on iOS

### Basic Git Configuration

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Useful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"

# View configuration
git config --list
```

### Common Git Operations

**Check Status:**
```bash
git status
# or use alias
git st
```

**View Changes:**
```bash
# See what changed
git diff

# See specific file changes
git diff filename.py
```

**Stage Changes:**
```bash
# Stage specific file
git add filename.py

# Stage all changes
git add .

# Stage interactively
git add -p
```

**Commit Changes:**
```bash
# Commit with message
git commit -m "Add feature X"

# Commit with detailed message (opens editor)
git commit
```

**Push Changes:**
```bash
# Push to origin
git push origin main

# Or simply
git push
```

**Pull Updates:**
```bash
# Pull latest changes
git pull origin main

# Or simply
git pull
```

**Branch Management:**
```bash
# Create new branch
git checkout -b feature-branch

# Switch branches
git checkout main

# List branches
git branch

# Delete branch
git branch -d feature-branch
```

### Working with Remotes

```bash
# View remotes
git remote -v

# Add a remote
git remote add upstream https://github.com/original/repo.git

# Fetch from remote
git fetch upstream

# Merge remote changes
git merge upstream/main
```

## Running the Local Server

### Starting the Server

**Navigate to server directory:**
```bash
cd ~/dev/awesome-claude-skills/server
```

**Run the server:**
```bash
# Standard mode (foreground)
python3 ishserver.py

# Custom port
python3 ishserver.py 8080

# Background mode
python3 ishserver.py &
```

### Testing the Server

**Using curl in iSH:**
```bash
# Test API information
curl http://localhost:8000/

# List all resources
curl http://localhost:8000/resources | python3 -m json.tool

# Get specific resource
curl http://localhost:8000/resources/991001576278503441

# Search resources
curl "http://localhost:8000/search?q=statistics"
```

**Using Safari:**
1. Open Safari on your iOS device
2. Navigate to `http://localhost:8000/`
3. Bookmark for quick access

### Managing Server Processes

**Find running servers:**
```bash
ps aux | grep python
```

**Stop a server:**
```bash
# If running in foreground: Press Ctrl+C

# If running in background:
kill <PID>

# Force kill if needed
kill -9 <PID>
```

## Working with Python

### Python Basics

**Check Python version:**
```bash
python3 --version
```

**Run Python script:**
```bash
python3 script.py
```

**Interactive Python shell:**
```bash
python3
>>> print("Hello from iOS!")
>>> exit()
```

### Installing Python Packages

```bash
# Install pip if not already installed
apk add py3-pip

# Install a package
pip3 install requests

# Install from requirements.txt
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Uninstall a package
pip3 uninstall package-name
```

### Python Virtual Environments

```bash
# Install venv support
apk add python3-dev

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Deactivate
deactivate
```

### Working with JSON

```bash
# Pretty-print JSON file
python3 -m json.tool metadata/australian-academic-resources.json

# Validate JSON
python3 -c "import json; json.load(open('file.json'))" && echo "Valid JSON"
```

### Working with YAML

```bash
# Install PyYAML
pip3 install pyyaml

# Validate YAML
python3 -c "import yaml; yaml.safe_load(open('file.yaml'))" && echo "Valid YAML"
```

## Working with Node.js (Optional)

### Installing Node.js

```bash
# Install Node.js and npm
apk add nodejs npm

# Verify installation
node --version
npm --version
```

### Basic Node.js Operations

**Initialize a project:**
```bash
npm init -y
```

**Install packages:**
```bash
# Install package locally
npm install package-name

# Install globally
npm install -g package-name

# Install from package.json
npm install
```

**Run scripts:**
```bash
# Run scripts defined in package.json
npm run dev
npm test
npm start
```

### Useful Node.js Tools

```bash
# Install http-server (alternative to Python server)
npm install -g http-server

# Run it
http-server -p 8000

# Install json-server (mock REST API)
npm install -g json-server

# Run with your JSON file
json-server --watch metadata/australian-academic-resources.json
```

## Development Best Practices

### 1. Keep Your Environment Updated

```bash
# Update package repository
apk update

# Upgrade packages
apk upgrade

# Check for outdated Python packages
pip3 list --outdated
```

### 2. Use Version Control Frequently

```bash
# Commit often with descriptive messages
git add .
git commit -m "Descriptive message about changes"
git push
```

### 3. Test Before Committing

```bash
# Run your tests
python3 -m pytest

# Test the server
python3 server/ishserver.py &
curl http://localhost:8000/resources
kill %1
```

### 4. Document Your Changes

- Update README files
- Add comments to complex code
- Keep documentation in sync with code

### 5. Backup Your Work

- Push to GitHub regularly
- Use branches for experiments
- Consider using iCloud or another backup solution

## Recommended Workflows

### Workflow 1: Quick Edits

```bash
# 1. Pull latest changes
git pull

# 2. Edit files with nano
nano server/ishserver.py

# 3. Test changes
python3 server/ishserver.py

# 4. Commit and push
git add .
git commit -m "Update server configuration"
git push
```

### Workflow 2: Feature Development

```bash
# 1. Create feature branch
git checkout -b new-feature

# 2. Make changes
nano file.py

# 3. Test locally
python3 file.py

# 4. Commit changes
git add .
git commit -m "Add new feature"

# 5. Push branch
git push origin new-feature

# 6. Create pull request (via GitHub web or Working Copy app)
```

### Workflow 3: Server Development

```bash
# Terminal 1: Run server
python3 server/ishserver.py

# Terminal 2: Test server (or use Safari)
curl http://localhost:8000/resources

# Make changes to server
# Restart server to see changes (Ctrl+C, then rerun)
```

## Tips for Mobile Development

### 1. Use External Keyboard

- Bluetooth keyboard greatly improves productivity
- Smart Keyboard works great with iPad
- Keyboard shortcuts speed up terminal work

### 2. Split Screen (iPad)

- iSH on one side, Safari on the other
- Perfect for development and testing
- Drag and drop files between apps

### 3. Shortcuts and Aliases

Create aliases in `~/.profile`:

```bash
# Edit profile
nano ~/.profile

# Add aliases
alias ll='ls -la'
alias gs='git status'
alias gp='git pull'
alias gpu='git push'
alias dev='cd ~/dev/awesome-claude-skills'
alias server='cd ~/dev/awesome-claude-skills/server && python3 ishserver.py'

# Save and reload
source ~/.profile
```

### 4. Screen Management

```bash
# Use screen for persistent sessions
apk add screen

# Start screen
screen

# Detach: Ctrl+A then D
# Reattach: screen -r

# List screens
screen -ls
```

### 5. Quick Access Scripts

Create a `~/bin` directory with utility scripts:

```bash
mkdir -p ~/bin

# Add to PATH in ~/.profile
echo 'export PATH=$PATH:~/bin' >> ~/.profile

# Create utility scripts
echo '#!/bin/sh' > ~/bin/start-server
echo 'cd ~/dev/awesome-claude-skills/server && python3 ishserver.py' >> ~/bin/start-server
chmod +x ~/bin/start-server

# Now just run:
start-server
```

### 6. Bookmarks in Safari

Create bookmarks for common endpoints:
- `http://localhost:8000/` - API root
- `http://localhost:8000/resources` - All resources
- `http://localhost:8000/search?q=` - Search (edit query in address bar)

### 7. Siri Shortcuts (Advanced)

Create Siri Shortcuts to:
- Open iSH and navigate to project
- Open Safari to API endpoint
- Run test commands

## Troubleshooting Common Issues

### iSH Keeps Restarting

- Save work frequently
- Use `screen` for persistent sessions
- Update iSH from App Store

### Slow Performance

- Clear package cache: `rm -rf /var/cache/apk/*`
- Close other apps
- Restart iOS device

### Git Authentication Issues

```bash
# Use HTTPS with token instead of password
git remote set-url origin https://USERNAME:TOKEN@github.com/user/repo.git

# Or use Working Copy app for authentication
```

### Python Import Errors

```bash
# Make sure package is installed
pip3 install package-name

# Check Python path
python3 -c "import sys; print(sys.path)"

# Install in user directory if needed
pip3 install --user package-name
```

## Next Steps

- Explore the [server documentation](../server/README.md)
- Review the [metadata files](../metadata/)
- Set up your own development workflow
- Contribute to the project!

## Additional Resources

- [iSH Documentation](https://github.com/ish-app/ish/wiki)
- [Git Documentation](https://git-scm.com/doc)
- [Python Documentation](https://docs.python.org/3/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [Alpine Linux Packages](https://pkgs.alpinelinux.org/packages)

---

**Happy developing on iOS! 🎨✨**
