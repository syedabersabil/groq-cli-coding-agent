# 🚀 Quick Start

Get your Groq CLI Coding Agent running in 5 minutes!

## ⏱️ 5-Minute Setup

### 1. Clone & Navigate (30 seconds)

```bash
git clone https://github.com/syedabersabil/groq-cli-coding-agent.git
cd groq-cli-coding-agent
```

### 2. Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

### 3. Get API Key (1 minute)

- Visit [console.groq.com](https://console.groq.com)
- Sign up (free)
- Create API key
- Copy the key

### 4. Configure (1 minute)

```bash
python main.py setup
# Paste your API key when prompted
```

### 5. Start Coding! (1 minute)

```bash
python main.py chat
```

## 🤔 First Questions to Try

```bash
# Basic help
"Hello! What can you do?"

# Code generation
"Create a Python script that prints the Fibonacci sequence up to 10 numbers"

# Debugging
"Create a Python function with a bug, then fix it"

# Learning
"Explain list comprehensions in Python with examples"

# File operations
"Create a hello.py file with a function that greets someone by name"
```

## 📚 Quick Commands

```bash
# Start chat
python main.py chat

# Single query (no interactive loop)
python main.py chat -q "Your question here"

# Check setup status
python main.py status

# Reconfigure API key
python main.py setup
```

## 💭 In-Chat Commands

```
/help      - Show help
/clear     - Clear history
/history   - Show previous messages
/exit      - Exit
```

## 🦁 Useful Examples

### Create a File

```
You: Create a Python file called hello.py that prints "Hello World"

Agent: → Using tool: write_file
       [File created]
```

### Read a File

```
You: Read hello.py and tell me what it does

Agent: → Using tool: read_file
       [Shows content and explanation]
```

### Execute Code

```
You: Create a function that calculates factorial, then test it with 5

Agent: → Using tool: write_file
       → Using tool: execute_python
       [Shows result]
```

### Run Commands

```
You: Initialize a Python project with pip

Agent: → Using tool: bash_command
       [Runs pip init]
```

## 🪧 Important Notes

- **First time?** Start with interactive mode
- **Questions?** Use `/help` command
- **Not working?** Check [INSTALLATION.md](INSTALLATION.md)
- **Want more?** Read [USAGE_GUIDE.md](USAGE_GUIDE.md)

## 퉪️ Troubleshooting

### API key not saved?

```bash
# Try again
python main.py setup

# Or use environment variable
export GROQ_API_KEY="your-key"
python main.py chat
```

### ModuleNotFoundError?

```bash
# Reinstall
pip install -r requirements.txt
```

### Agent not responding?

- Check internet connection
- Verify API key is valid
- Wait a moment and try again

## 📖 Documentation

- **[README.md](README.md)** - Full documentation
- **[INSTALLATION.md](INSTALLATION.md)** - Setup guide
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Detailed examples
- **[LICENSE](LICENSE)** - MIT License

## 🚀 Next Steps

1. ✅ Run `python main.py chat`
2. ✅ Try asking a question
3. ✅ Try `/help` for commands
4. ✅ Explore the tools by asking to read/write files
5. ✅ Check [USAGE_GUIDE.md](USAGE_GUIDE.md) for more examples

## 📱 Pro Tips

- **Conversation Context**: The agent remembers previous messages in the same session
- **Tool Auto-Use**: Just ask naturally; the agent will use tools when needed
- **Clear History**: Use `/clear` to start fresh conversation
- **Code Testing**: Ask the agent to create AND test code in one go

## 🤘 Need Help?

1. Check [USAGE_GUIDE.md](USAGE_GUIDE.md) for examples
2. Try `/help` in the chat
3. Review error messages carefully
4. Check [INSTALLATION.md](INSTALLATION.md) for troubleshooting
5. Open an issue on [GitHub](https://github.com/syedabersabil/groq-cli-coding-agent)

---

**Enjoy your AI coding assistant! 🚀📋**
