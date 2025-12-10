# 🚀 Groq CLI Coding Agent - Project Summary

**An AI-powered CLI coding assistant built with Groq API, Python, and modern development tools.**

## 🌟 What This Project Does

The Groq CLI Coding Agent is a command-line tool that acts as your personal AI coding assistant. It uses the Groq API to understand coding questions and tasks, and can:

- **Write Code**: Generate Python, JavaScript, and other code
- **Debug Code**: Analyze and fix bugs in your code
- **Explain Concepts**: Teach you programming concepts with examples
- **Manage Files**: Read, write, and organize your files
- **Run Code**: Execute Python code and bash commands
- **Maintain Context**: Remember previous conversations

## 📈 Project Structure

```
groq-cli-coding-agent/
├─ main.py              # CLI entry point (Click framework)
├─ agent.py             # CodingAgent class with streaming support
├─ config.py            # API key management (keyring-based)
├─ tools.py             # Built-in tools for the agent
├─ examples.py          # 7 example use cases
├─ requirements.txt     # Python dependencies
├─ README.md            # Full documentation
├─ QUICK_START.md       # 5-minute setup guide
├─ INSTALLATION.md      # Detailed installation guide
├─ USAGE_GUIDE.md       # Comprehensive usage examples
├─ PROJECT_SUMMARY.md   # This file
├─ LICENSE              # MIT License
├─ .gitignore           # Git ignore rules
```

## 🚄 Installation (TL;DR)

```bash
# 1. Clone
git clone https://github.com/syedabersabil/groq-cli-coding-agent.git
cd groq-cli-coding-agent

# 2. Install
pip install -r requirements.txt

# 3. Setup
python main.py setup  # Enter your Groq API key

# 4. Run
python main.py chat
```

For detailed setup, see [INSTALLATION.md](INSTALLATION.md) or [QUICK_START.md](QUICK_START.md).

## 💫 How to Use

### Interactive Mode (Recommended)

```bash
python main.py chat
👤 You: Create a Python function that calculates Fibonacci numbers
🤖 Agent: [Generates code]
```

### Quick Query Mode

```bash
python main.py chat -q "How do I read a file in Python?"
```

### Check Status

```bash
python main.py status  # Verify API key is configured
```

## 🛠️ Built-in Tools

The agent automatically uses these tools when needed:

| Tool | Purpose | Example |
|------|---------|----------|
| **read_file** | Read file contents | "Read my main.py and find bugs" |
| **write_file** | Create/modify files | "Create a hello.py file" |
| **list_files** | Browse directory | "Show me all Python files here" |
| **execute_python** | Run Python code | "Test this function with value 5" |
| **bash_command** | Run shell commands | "Initialize npm project" |

## 📚 Documentation

### For Quick Start
1. [QUICK_START.md](QUICK_START.md) - Get running in 5 minutes

### For Installation
1. [INSTALLATION.md](INSTALLATION.md) - Step-by-step setup guide
2. Platform-specific instructions (Windows, macOS, Linux)
3. Troubleshooting section

### For Usage
1. [USAGE_GUIDE.md](USAGE_GUIDE.md) - Comprehensive examples
2. Real-world scenarios
3. Best practices and pro tips
4. Safety considerations

### For Reference
1. [README.md](README.md) - Full feature list
2. [examples.py](examples.py) - 7 executable examples

## 📋 In-Chat Commands

```
/help      Show available commands
/clear     Clear conversation history
/history   Show previous messages
/exit      Exit the agent
```

## 💻 Technologies Used

```
✓ Groq API        - Fast LLM inference
✓ Click           - Command-line interface framework
✓ Rich            - Beautiful terminal formatting
✓ Keyring         - Secure credential storage
✓ Python 3.8+     - Core language
```

## 🔐 Security Features

- 🔒 **Secure API Key Storage**: Uses system keyring (not stored in files)
- 🔓 **Environment Variable Support**: GROQ_API_KEY fallback
- ⏰ **Execution Timeout**: Python and bash commands timeout after 10 seconds
- 📄 **Sandboxed Execution**: File operations limited to accessible paths

## 📊 Features & Capabilities

### Core Features
- ✅ Streaming responses for real-time feedback
- ✅ Multi-turn conversations with context memory
- ✅ Tool-use capability (read/write files, execute code)
- ✅ Error handling and recovery
- ✅ Beautiful CLI interface with Rich formatting

### Advanced Features
- 🤖 Automatic tool selection based on your request
- 📚 Conversation history tracking
- 🚄 Extensible tool system
- 🛠️ Configurable models and parameters
- 🔡 Customizable system prompts

## 🚘 Use Cases

### 1. Learning Programming
- Explain concepts with examples
- Debug your code
- Suggest improvements
- Test your understanding

### 2. Rapid Development
- Generate boilerplate code
- Create project structures
- Implement common patterns
- Refactor existing code

### 3. Problem Solving
- Debug production issues
- Optimize slow code
- Add error handling
- Improve code quality

### 4. Code Review
- Analyze code for issues
- Suggest improvements
- Check for security issues
- Verify best practices

### 5. Documentation
- Generate docstrings
- Create README files
- Write API documentation
- Explain complex code

## 🤈 Examples

See [examples.py](examples.py) for 7 runnable examples:

1. Basic usage
2. Conversation context
3. Custom tools
4. File operations
5. Code testing
6. Tool extension guide
7. Performance monitoring

Run an example:
```bash
python examples.py 1  # Run example 1
```

## 📆 License

MIT License - See [LICENSE](LICENSE) file for details.

## 👤 Author

Created by [syedabersabil](https://github.com/syedabersabil)

## 🔗 Links

- **GitHub**: [groq-cli-coding-agent](https://github.com/syedabersabil/groq-cli-coding-agent)
- **Groq**: [console.groq.com](https://console.groq.com)
- **API Docs**: [Groq API Documentation](https://console.groq.com/docs)

## 📌 Contributing

Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🢡 Tips & Tricks

### Pro Tips
- **Use context**: The agent remembers previous messages in the same session
- **Be specific**: Detailed requirements lead to better results
- **Test together**: Ask the agent to create AND test code
- **Iterate**: Build features incrementally
- **Review always**: Always review generated code before using

### Common Patterns
```bash
# Create and test
"Create a function that [does something], then test it with [test cases]"

# Improve existing
"Read [filename] and improve it by [adding feature/fixing issue]"

# Understand code
"Read [filename] and explain what it does"

# Debug
"Read [filename] and find any bugs or issues"

# Refactor
"Read [filename] and refactor it for [performance/readability/etc]"
```

## 🪧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| API key not found | Run `python main.py setup` again |
| Module not found | Run `pip install -r requirements.txt` |
| Timeout errors | Break code into smaller functions |
| Connection errors | Check internet, verify API key |
| Keyring errors (Linux) | Install: `sudo apt-get install python3-keyring` |

For more help, see [INSTALLATION.md](INSTALLATION.md).

## 🚀 Future Enhancements

Planned features:
- [ ] Web search capability
- [ ] Database integration
- [ ] Git operations tools
- [ ] Custom tool builder
- [ ] Code testing framework
- [ ] Performance profiling
- [ ] Multi-language support
- [ ] VSCode extension

## 📋 Summary

The Groq CLI Coding Agent is a powerful, user-friendly tool for developers who want:

1. **Fast AI assistance** - Groq's fast inference
2. **Easy setup** - Just an API key needed
3. **Powerful tools** - File operations, code execution
4. **Secure** - Keyring-based API key storage
5. **Extensible** - Easy to add custom tools
6. **Well-documented** - Guides for all levels

## 🙋 Getting Help

1. **Quick questions?** Check [QUICK_START.md](QUICK_START.md)
2. **Setup issues?** See [INSTALLATION.md](INSTALLATION.md)
3. **Usage questions?** Read [USAGE_GUIDE.md](USAGE_GUIDE.md)
4. **Want examples?** Check [examples.py](examples.py)
5. **Found a bug?** Open an issue on GitHub

---

**Happy coding! 🚀**

Built with ❤️ using Groq API
