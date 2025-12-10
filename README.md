# 🚀 Groq CLI Coding Agent

An AI-powered CLI coding assistant that uses the Groq API to help you write, debug, and improve code. Built with Python and equipped with powerful development tools.

## ✨ Features

- **AI-Powered Code Assistant**: Uses Groq's fast inference for real-time code help
- **Tool Integration**: Read/write files, execute Python code, run bash commands
- **Streaming Responses**: Real-time response streaming for better UX
- **Secure API Key Management**: Keyring-based secure storage
- **Interactive CLI**: User-friendly command-line interface
- **Conversation History**: Maintains context across multiple queries
- **Multi-Tool Support**: File operations, code execution, bash commands

## 🚄 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- A Groq API key from [console.groq.com](https://console.groq.com)

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/syedabersabil/groq-cli-coding-agent.git
cd groq-cli-coding-agent
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure API key**:
```bash
python main.py setup
```
This will prompt you to enter your Groq API key. It will be stored securely in your system's keyring.

## 🚀 Quick Start

### Interactive Mode
Start an interactive conversation:
```bash
python main.py chat
```

### Quick Query Mode
Ask a single question without entering interactive mode:
```bash
python main.py chat -q "How do I read a file in Python?"
```

### Check Status
Verify your configuration:
```bash
python main.py status
```

## 📚 Commands

Inside the interactive chat, use these commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `/history` | Show conversation history |
| `/exit` | Exit the agent |

## 🛠️ Built-in Tools

The agent can access these tools automatically:

### 1. Read File
```
Read the contents of a file
Usage: Agent will use this when you ask to read files
```

### 2. Write File
```
Write or create files with content
Usage: Agent will use this to create/modify files
```

### 3. List Files
```
Browse directory structure
Usage: Agent will list files in specified directories
```

### 4. Execute Python
```
Run Python code safely with 10s timeout
Usage: Agent will execute Python for testing/validation
```

### 5. Bash Command
```
Run shell commands with 10s timeout
Usage: Agent will run bash for git, npm, pip commands, etc.
```

## 💬 Usage Examples

### Example 1: Create a Python Script
```
You: Create a Python script that calculates Fibonacci numbers
Agent: [Creates and saves the file using write_file tool]
```

### Example 2: Debug Code
```
You: Read test.py and fix any bugs you find
Agent: [Reads file, analyzes, executes to test, suggests fixes]
```

### Example 3: Project Setup
```
You: Initialize a new Node.js project and install dependencies
Agent: [Uses bash_command to run npm init and npm install]
```

### Example 4: Code Explanation
```
You: Explain what this code does and suggest improvements
Agent: [Reads file, explains logic, suggests optimizations]
```

## 🔓 Security

- **Secure Storage**: API keys are stored in your system's secure keyring, not in files
- **Environment Variable Support**: Can read GROQ_API_KEY from environment
- **Code Execution**: Python and bash commands run with 10-second timeout limits
- **File Operations**: Limited to accessible directories (no system protection bypasses)

## 🚘 Project Structure

```
groq-cli-coding-agent/
├─ main.py          # CLI entry point with Click framework
├─ agent.py         # Main CodingAgent class with streaming
├─ config.py        # Configuration and API key management
├─ tools.py         # Tool definitions and execution
├─ requirements.txt # Python dependencies
├─ README.md        # This file
├─ .gitignore       # Git ignore rules
├─ LICENSE          # MIT License

```

## 💻 Technologies Used

- **Groq SDK**: Fast LLM inference
- **Click**: CLI framework
- **Rich**: Beautiful terminal formatting
- **Keyring**: Secure credential storage
- **Python 3.8+**: Core language

## 🔐 API Key Setup

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Go to API keys section
4. Create a new API key
5. Run `python main.py setup` and paste the key

## 🚘 Models Available

The agent uses `mixtral-8x7b-32768` by default. You can modify `agent.py` to use:
- `mixtral-8x7b-32768` (recommended)
- `llama-2-70b-chat`
- `llama-2-7b-chat`
- And other available Groq models

## ⚠️ Limitations

- Commands timeout after 10 seconds
- File operations are limited to accessible paths
- Some system-level operations may be restricted
- Code execution runs in the current Python process context

## 🚂 Troubleshooting

### API key not found
```bash
# Set as environment variable
export GROQ_API_KEY="your-api-key"
python main.py chat

# Or run setup again
python main.py setup
```

### Keyring issues on Linux
```bash
# Install required package
sudo apt-get install python3-keyring
```

### Command timeout
If code execution exceeds 10 seconds:
- Break into smaller functions
- Test locally first
- Ask the agent to optimize

## 💉 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

Created by [syedabersabil](https://github.com/syedabersabil)

## 🙋 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review Groq API documentation
3. Open an issue on GitHub
4. Check existing issues for solutions

## 🚀 Future Enhancements

- [ ] Support for more programming languages
- [ ] Database integration
- [ ] Web search capability
- [ ] Custom tool creation
- [ ] Code testing framework
- [ ] Performance profiling tools
- [ ] Documentation generation
- [ ] Git integration tools

---

**Made with ❤️ using Groq API**
