# 🚄 Installation Guide

Step-by-step installation instructions for the Groq CLI Coding Agent.

## Prerequisites

- **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Usually comes with Python
- **Git**: For cloning the repository
- **Groq API Key**: [Get one here](https://console.groq.com)

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/syedabersabil/groq-cli-coding-agent.git
cd groq-cli-coding-agent
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `groq` - Groq API SDK
- `click` - CLI framework
- `rich` - Beautiful terminal output
- `keyring` - Secure credential storage
- `python-dotenv` - Environment variable management
- `requests` - HTTP library

### Step 4: Get Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in with your account
3. Go to the API keys section
4. Create a new API key
5. Copy the key (keep it safe!)

### Step 5: Configure API Key

```bash
python main.py setup
```

When prompted, paste your Groq API key.

### Step 6: Verify Installation

```bash
python main.py status
```

You should see:
```
┏━━━━━━━━━━━━━━┓
┃ API Key Configured: ✓ yes ┃
┗━━━━━━━━━━━━━━┛
```

## Platform-Specific Instructions

### Windows

```bash
# Install dependencies
pip install -r requirements.txt

# Setup
python main.py setup

# Run
python main.py chat
```

### macOS

```bash
# Might need to use python3 instead of python
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py setup
python3 main.py chat
```

### Linux (Ubuntu/Debian)

```bash
# Install Python if not present
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install and run
pip3 install -r requirements.txt
python3 main.py setup
python3 main.py chat
```

If you get keyring errors:

```bash
# Install keyring dependencies
sudo apt-get install python3-keyring
```

### Linux (Fedora/RHEL)

```bash
# Install dependencies
sudo dnf install python3 python3-pip python3-devel

# Proceed with installation
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py setup
python3 main.py chat
```

## Troubleshooting

### Issue: `python: command not found`

**Solution:**
```bash
# Use python3 instead
python3 main.py chat

# Or create alias
alias python=python3
```

### Issue: `pip: command not found`

**Solution:**
```bash
# Use pip3
pip3 install -r requirements.txt

# Or upgrade pip
python3 -m pip install --upgrade pip
```

### Issue: Virtual environment not activating

**Solution:**

Windows:
```bash
# Use the correct path
venv\Scripts\activate.bat  # For Command Prompt
venv\Scripts\Activate.ps1  # For PowerShell
```

Mac/Linux:
```bash
# Make sure to use dot source
source venv/bin/activate
```

### Issue: `ModuleNotFoundError: No module named 'groq'`

**Solution:**
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt

# Or install individually
pip install groq click rich keyring requests python-dotenv
```

### Issue: `keyring.errors.InitError` on Linux

**Solution:**
```bash
# Install required dependencies
sudo apt-get install python3-keyring gnome-keyring

# Or use environment variable as workaround
export GROQ_API_KEY="your-api-key"
python3 main.py chat
```

### Issue: `Permission denied` when running script

**Solution:**
```bash
# Make the script executable
chmod +x main.py

# Or run with python
python main.py chat
```

### Issue: `ConnectionError: Failed to connect to Groq API`

**Causes & Solutions:**
1. **No internet connection**: Check your connection
2. **API key invalid**: Run `python main.py setup` again
3. **API key expired**: Generate a new one on console.groq.com
4. **API rate limited**: Wait a moment and try again

### Issue: `Certificate verification failed`

**Solution:**
```bash
# Update certificates
pip install --upgrade certifi

# Or disable verification (not recommended for production)
export REQUESTS_CA_BUNDLE=""
```

## Verify Everything Works

```bash
# 1. Check Python version
python --version  # Should be 3.8+

# 2. Check dependencies
pip list

# 3. Check API key is configured
python main.py status

# 4. Test with quick query
python main.py chat -q "Hello, are you working?"
```

## Uninstall

To completely remove the agent:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv  # On Mac/Linux
rmdir /s venv  # On Windows

# Remove API key from keyring (optional)
python -c "import keyring; keyring.delete_password('groq-cli-agent', 'api_key')"

# Remove the project directory
rm -rf groq-cli-coding-agent
```

## Getting Help

If you encounter issues:

1. **Check logs**: Look at error messages carefully
2. **Verify prerequisites**: Make sure Python and dependencies are installed
3. **Review troubleshooting**: Check this guide
4. **Check GitHub Issues**: See if someone had the same problem
5. **Ask for help**: Open a new issue on GitHub

## Next Steps

After installation:

1. Read [USAGE_GUIDE.md](USAGE_GUIDE.md) for how to use the agent
2. Check [README.md](README.md) for features and commands
3. Start with interactive mode: `python main.py chat`
4. Try some examples from USAGE_GUIDE.md

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 512 MB | 2 GB |
| Disk Space | 100 MB | 500 MB |
| Internet | Required | Stable connection |

---

**Installation complete! Happy coding! 🚀**
