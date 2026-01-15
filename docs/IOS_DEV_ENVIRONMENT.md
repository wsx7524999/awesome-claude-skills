# iOS Development Environment Setup

Comprehensive guide for setting up a complete development environment on iOS using iSH, including Node.js, code editors, testing tools, and optimization techniques.

## Table of Contents
1. [Overview](#overview)
2. [Node.js & npm Setup](#nodejs--npm-setup)
3. [Code Editor Options](#code-editor-options)
4. [Development Tools](#development-tools)
5. [Testing & Debugging](#testing--debugging)
6. [Common Issues](#common-issues)
7. [Performance Optimization](#performance-optimization)
8. [Workflow Tips](#workflow-tips)

## Overview

While iOS is not traditionally a development platform, iSH enables a surprisingly capable development environment. This guide covers everything you need to build, test, and run projects on your iPhone or iPad.

### What You Can Do
✅ Run Node.js applications  
✅ Execute Python scripts  
✅ Use Git for version control  
✅ Edit code with terminal-based editors  
✅ Run local web servers  
✅ Install npm packages  
✅ Test APIs and scripts  

### Limitations
❌ No native IDE support  
❌ Limited performance for heavy builds  
❌ No GUI applications  
❌ Background processes restricted  
❌ Can't run Docker containers  

## Node.js & npm Setup

### Installing Node.js

iSH provides Node.js through the Alpine package manager.

#### Step 1: Update Package Repository
```bash
apk update
```

#### Step 2: Install Node.js and npm
```bash
apk add nodejs npm
```

This installs both Node.js and npm together.

#### Step 3: Verify Installation
```bash
node --version
npm --version
```

Expected output:
```
v18.x.x (or similar)
9.x.x (or similar)
```

### Alternative: Install Specific Version

If you need a specific Node.js version (advanced):

```bash
# List available versions
apk search nodejs

# Install specific version (if available)
apk add nodejs=18.17.1-r0
```

### Configuring npm

#### Set npm Global Directory
By default, npm installs global packages to a system directory. It's better to use a local directory:

```bash
# Create directory for global packages
mkdir -p ~/.npm-global

# Configure npm to use this directory
npm config set prefix '~/.npm-global'

# Add to PATH
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
source ~/.profile
```

#### Test Global Installation
```bash
npm install -g npm-check-updates
ncu --version
```

### Setting Up a Node.js Project

#### Initialize a New Project
```bash
mkdir ~/my-project
cd ~/my-project
npm init -y
```

This creates a `package.json` file.

#### Install Dependencies
```bash
# Install packages locally
npm install express

# Install dev dependencies
npm install --save-dev nodemon
```

⚠️ **Note:** Some packages with native bindings may not work on iSH. Stick to pure JavaScript packages when possible.

### iOS-Compatible Packages

These packages are known to work well on iSH:

**Web Servers:**
- `express` - Web framework
- `koa` - Lightweight web framework
- `http-server` - Simple static file server

**Utilities:**
- `lodash` - Utility functions
- `axios` - HTTP client
- `date-fns` - Date utilities
- `commander` - CLI tools

**Testing:**
- `jest` - Testing framework (may be slow)
- `mocha` - Test runner
- `chai` - Assertions

**Development:**
- `nodemon` - Auto-restart on changes
- `dotenv` - Environment variables
- `eslint` - Linting (may be slow)

### Running Node.js Applications

#### Basic Execution
```bash
node app.js
```

#### With npm Scripts
Add to `package.json`:
```json
{
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  }
}
```

Run with:
```bash
npm start
npm run dev
```

## Code Editor Options

Since iOS doesn't support traditional IDEs, you'll need terminal-based editors.

### Option 1: Nano (Easiest)

Nano is the simplest editor, perfect for beginners.

#### Install Nano
```bash
apk add nano
```

#### Basic Usage
```bash
# Open/create file
nano myfile.js

# Common shortcuts:
# Ctrl+O - Save file
# Ctrl+X - Exit
# Ctrl+K - Cut line
# Ctrl+U - Paste
# Ctrl+W - Search
```

#### Configure Nano
Create `~/.nanorc`:
```bash
set tabsize 2
set autoindent
set smooth
include /usr/share/nano/*.nanorc
```

### Option 2: Vim (Powerful)

Vim is more powerful but has a learning curve.

#### Install Vim
```bash
apk add vim
```

#### Basic Vim Commands
```bash
# Open file
vim myfile.js

# Insert mode: Press 'i'
# Normal mode: Press 'Esc'
# Save: ':w' (in normal mode)
# Quit: ':q'
# Save and quit: ':wq'
# Quit without saving: ':q!'
```

#### Basic .vimrc
Create `~/.vimrc`:
```vim
syntax on
set number
set tabstop=2
set shiftwidth=2
set expandtab
set autoindent
set hlsearch
```

### Option 3: External Editors (Best Experience)

For the best experience, use external apps that sync with iSH:

#### Textastic (Paid)
- Full-featured code editor for iOS
- Syntax highlighting for many languages
- Can access iSH files via Files app
- SFTP support

#### Working Copy (Git Client)
- Excellent Git client for iOS
- Built-in code editor
- Can work with iSH repositories

#### a-Shell (Alternative to iSH)
- Another Linux shell for iOS
- Includes Vim and other editors
- Can share files with iSH

### Workflow: External Editor + iSH

1. **Edit in Textastic** (or another editor)
   - Open file from Files app
   - Make changes with syntax highlighting
   - Save

2. **Run in iSH**
   - Switch to iSH app
   - Run your script/server
   - See output immediately

3. **Split View on iPad**
   - Editor on one side
   - iSH terminal on other side
   - Best of both worlds!

## Development Tools

### Git Configuration

Already covered in [iSH Setup Guide](ISH_SETUP_GUIDE.md), but here are advanced tips:

#### Set Default Editor
```bash
git config --global core.editor nano
# or
git config --global core.editor vim
```

#### Useful Aliases
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
```

Now use: `git st`, `git co`, etc.

#### View Pretty Logs
```bash
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

Use: `git lg`

### Other Useful Tools

#### curl - HTTP Client
```bash
apk add curl

# Make requests
curl http://localhost:8080/api/resources
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://api.example.com
```

#### jq - JSON Processor
```bash
apk add jq

# Pretty print JSON
curl http://localhost:8080/api/resources | jq '.'

# Extract specific fields
curl http://localhost:8080/api/resources | jq '.resources[0].title'
```

#### tree - Directory Visualization
```bash
apk add tree

# View project structure
tree -L 2
```

#### htop - System Monitor
```bash
apk add htop

# Monitor system resources
htop
```

## Testing & Debugging

### Testing Node.js Applications

#### Using Jest
```bash
npm install --save-dev jest

# Add to package.json
{
  "scripts": {
    "test": "jest"
  }
}

# Run tests
npm test
```

⚠️ **Note:** Jest can be slow on iSH. Consider simpler test frameworks.

#### Using Mocha (Lighter)
```bash
npm install --save-dev mocha chai

# Add to package.json
{
  "scripts": {
    "test": "mocha"
  }
}

# Create test/test.js
# Run tests
npm test
```

### Debugging Python Applications

#### Using pdb (Python Debugger)
```python
# In your Python code
import pdb

# Set breakpoint
pdb.set_trace()
```

Run script, it will pause at breakpoint:
```bash
python3 script.py
```

Commands in pdb:
- `n` - Next line
- `c` - Continue
- `p variable` - Print variable
- `l` - List code
- `q` - Quit

#### Using print() Debugging
```python
print(f"Debug: variable value is {variable}")
```

### Debugging Node.js Applications

#### Using console.log
```javascript
console.log('Debug:', variable);
console.error('Error:', error);
console.table(array);
```

#### Using Node.js Debugger
```bash
node inspect app.js
```

Commands:
- `cont` or `c` - Continue
- `next` or `n` - Next line
- `step` or `s` - Step into
- `repl` - Open REPL
- `quit` - Exit

### Server Debugging

#### Check if Server is Running
```bash
# List processes
ps aux | grep python
ps aux | grep node

# Check port usage
netstat -tuln | grep 8080
```

#### View Server Logs
If running in background:
```bash
# Redirect output to log file
python3 ishserver.py > server.log 2>&1 &

# View logs
tail -f server.log
```

#### Test Endpoints
```bash
# Test with curl
curl -v http://localhost:8080/api/resources

# -v flag shows detailed request/response
```

## Common Issues

### Issue 1: Package Installation Fails

**Problem:** npm install fails with errors

**Solutions:**
1. Clear npm cache:
   ```bash
   npm cache clean --force
   ```

2. Remove node_modules and reinstall:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. Try installing without optional dependencies:
   ```bash
   npm install --no-optional
   ```

4. Use --legacy-peer-deps:
   ```bash
   npm install --legacy-peer-deps
   ```

### Issue 2: Process Killed

**Problem:** "Killed" message when running commands

**Solutions:**
1. Free up memory:
   ```bash
   # Close other apps
   # Restart iSH
   ```

2. Increase process limits (doesn't always work on iOS):
   ```bash
   ulimit -n 4096
   ```

3. Process in smaller chunks
4. Use lighter alternatives (e.g., mocha instead of jest)

### Issue 3: Slow Performance

**Problem:** Commands take very long to complete

**Solutions:**
1. Use --production flag:
   ```bash
   npm install --production
   ```

2. Avoid development dependencies when possible
3. Use .npmrc to skip unnecessary scripts:
   ```bash
   echo "ignore-scripts=true" > ~/.npmrc
   ```

4. Close other apps
5. Restart device

### Issue 4: File Permission Errors

**Problem:** "Permission denied" errors

**Solutions:**
1. Check file permissions:
   ```bash
   ls -la filename
   ```

2. Make file executable:
   ```bash
   chmod +x filename
   ```

3. Change ownership:
   ```bash
   chown root:root filename
   ```

### Issue 5: Module Not Found

**Problem:** "Cannot find module" error

**Solutions:**
1. Verify module is installed:
   ```bash
   npm list modulename
   ```

2. Reinstall module:
   ```bash
   npm install modulename
   ```

3. Check NODE_PATH:
   ```bash
   echo $NODE_PATH
   export NODE_PATH=~/my-project/node_modules
   ```

## Performance Optimization

### 1. Minimize Dependencies

Only install what you need:
```bash
# Check what's installed
npm list --depth=0

# Remove unused packages
npm prune
```

### 2. Use Production Mode

```bash
npm install --production
NODE_ENV=production node app.js
```

### 3. Optimize Code

- Minimize synchronous operations
- Use streams for large files
- Avoid heavy computations
- Cache results when possible

### 4. iSH Settings

1. **Enable Location Services** (helps with performance)
   - Settings → Privacy → Location Services → iSH → While Using

2. **Disable Auto-Lock**
   - Settings → Display & Brightness → Auto-Lock → Never

3. **Close Background Apps**
   - Swipe up on other apps to close them

### 5. Manage Memory

```bash
# Monitor memory usage
free -m

# Clear cache
sync && echo 3 > /proc/sys/vm/drop_caches
```

### 6. Use Lightweight Alternatives

Instead of:
- webpack → esbuild or rollup
- Jest → Mocha
- Babel → SWC
- TypeScript → Use --transpileOnly

## Workflow Tips

### 1. Create Aliases

Add to `~/.profile`:
```bash
alias ll='ls -la'
alias gs='git status'
alias gp='git pull'
alias serve='python3 -m http.server'
alias jcat='jq "." '
```

Source it:
```bash
source ~/.profile
```

### 2. Use Screen/Tmux

Keep sessions running:
```bash
apk add screen

# Start screen
screen

# Detach: Ctrl+A, D
# Reattach: screen -r
```

### 3. Project Structure

Organize your projects:
```
~/projects/
  ├── awesome-claude-skills/
  ├── my-api/
  └── test-scripts/
```

### 4. Quick Start Scripts

Create `~/start-dev.sh`:
```bash
#!/bin/sh
cd ~/awesome-claude-skills/server
python3 ishserver.py
```

Make executable:
```bash
chmod +x ~/start-dev.sh
```

Run:
```bash
~/start-dev.sh
```

### 5. Version Control Best Practices

```bash
# Before making changes
git checkout -b feature-name

# After changes
git add .
git commit -m "Description of changes"
git push origin feature-name
```

### 6. Documentation

Keep notes in your repo:
```bash
# Create notes
nano ~/awesome-claude-skills/NOTES.md
```

## Advanced Topics

### Running Multiple Services

Use screen or background processes:
```bash
# Terminal 1
python3 server1.py &

# Terminal 2 (using screen)
screen
node server2.js
# Ctrl+A, D to detach
```

### Environment Variables

Create `.env` file:
```
PORT=8080
API_KEY=your-key-here
NODE_ENV=development
```

Load in Node.js:
```bash
npm install dotenv
```

```javascript
require('dotenv').config();
const port = process.env.PORT || 3000;
```

### Scheduling Tasks

Use cron:
```bash
apk add dcron

# Edit crontab
crontab -e

# Run script every hour
0 * * * * /root/myscript.sh
```

## Resources

### Documentation
- [Node.js Docs](https://nodejs.org/docs/)
- [npm Docs](https://docs.npmjs.com/)
- [Alpine Linux Wiki](https://wiki.alpinelinux.org/)
- [Vim Docs](https://www.vim.org/docs.php)

### iOS Apps for Development
- **Textastic** - Code editor
- **Working Copy** - Git client
- **a-Shell** - Alternative shell
- **Secure ShellFish** - SSH/SFTP client

### Learning Resources
- [Learn Vim](https://vim-adventures.com/)
- [Learn Git](https://learngitbranching.js.org/)
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)

## Next Steps

1. ✅ Set up your preferred editor
2. ✅ Install necessary development tools
3. ✅ Create test project to verify setup
4. ✅ Configure aliases and shortcuts
5. ✅ Optimize performance settings
6. ✅ Start developing!

---

**Last Updated:** 2026-01-15  
**Version:** 1.0  
**Platform:** iOS/iPadOS via iSH
