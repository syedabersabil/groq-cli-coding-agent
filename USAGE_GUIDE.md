# 📚 Groq CLI Coding Agent - Usage Guide

Complete guide with real-world examples for using the Groq CLI Coding Agent.

## Table of Contents
- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Advanced Examples](#advanced-examples)
- [Tool Usage](#tool-usage)
- [Tips & Tricks](#tips--tricks)

## Quick Start

### 1. Initial Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API key
python main.py setup
# Follow prompts to enter your Groq API key

# Verify setup
python main.py status
```

### 2. Start Coding Assistant

```bash
# Interactive mode (recommended)
python main.py chat

# Or quick mode for single queries
python main.py chat -q "Write a Python function that reverses a string"
```

## Basic Usage

### Interactive Chat

Once in the chat interface:

```
╭──────────────────────────────╮
│  🚀 Groq CLI Coding Agent │
│  AI-Powered Code Assistant   │
╭──────────────────────────────╮

👤 You: Create a Python script that lists all Python files in current directory

🤖 Agent: I'll create a Python script that lists all .py files in the current directory.
[Agent uses write_file tool to create the script]
...
```

### Available Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/help` | `/help` | Show all available commands |
| `/clear` | `/clear` | Clear conversation history |
| `/history` | `/history` | Show previous messages |
| `/exit` | `/exit` | Exit the agent |

## Advanced Examples

### Example 1: Create and Run a Python Project

```
You: Create a Python project structure for a Flask API with:
- Main app file
- Requirements file
- Basic route
- Error handling

Agent: [Creates project files using write_file]
       [Shows you the complete setup]
       [Explains how to run it]
```

### Example 2: Debug and Fix Code

```
You: I have a Python file called app.py that's buggy. 
Read it, find the bugs, and create a fixed version.

Agent: [Reads app.py using read_file]
       [Analyzes the code]
       [Identifies issues]
       [Creates fixed version with write_file]
       [Explains what was wrong]
```

### Example 3: Full Stack Development

```
You: 
1. Create a React component for a todo list
2. Create a Python Flask backend
3. Show me how to connect them

Agent: [Creates multiple files]
       [Provides complete working example]
       [Explains the architecture]
```

### Example 4: Learning New Concepts

```
You: Explain decorators in Python with examples

Agent: [Provides detailed explanation]
       [Creates example files with different decorator patterns]
       [Tests the examples]
```

### Example 5: Code Optimization

```
You: I have code in slow.py. 
Read it and suggest optimizations.

Agent: [Reads the file]
       [Analyzes performance issues]
       [Creates optimized version]
       [Shows benchmarks/comparisons]
```

## Tool Usage

### The agent can use these tools automatically:

#### 1. **Read File**

When you ask the agent to read, analyze, or review code:

```
You: Read my main.py and tell me what it does

Agent: → Using tool: read_file
       [Shows file contents]
       [Explains the code]
```

#### 2. **Write File**

When you ask the agent to create or save code:

```
You: Create a Python script that calculates factorials

Agent: → Using tool: write_file
       [Creates factorial.py]
       [Explains the code]
```

#### 3. **List Files**

When you need to explore your project structure:

```
You: Show me all Python files in this project

Agent: → Using tool: list_files
       [Lists all .py files]
       [Shows the structure]
```

#### 4. **Execute Python**

When code needs to be tested or run:

```
You: Test this Fibonacci function with inputs 1-10

Agent: → Using tool: execute_python
       [Runs the test code]
       [Shows results]
```

#### 5. **Bash Command**

When you need to run system commands:

```
You: Set up a new Node.js project and install Express

Agent: → Using tool: bash_command
       [Runs npm init]
       [Runs npm install express]
       [Shows output]
```

## Tips & Tricks

### 💡 Pro Tips

1. **Be Specific with Requirements**
   ```
   Instead of: "Create a website"
   Try: "Create a single-page HTML website with:
        - Navigation menu
        - Hero section
        - Three feature cards
        - Contact form
        - Dark mode toggle"
   ```

2. **Use Context**
   ```
   You: Read database.py
   You: Now create unit tests for the functions in that file
   [Agent remembers the context from database.py]
   ```

3. **Leverage the Tools**
   ```
   You: Create a Python script, then execute it and show me the output
   [Agent creates script with write_file]
   [Agent tests it with execute_python]
   [Agent shows you results]
   ```

4. **Build Iteratively**
   ```
   You: Create a basic calculator
   [Agent creates it]
   
   You: Add support for division and handle division by zero
   [Agent updates based on previous context]
   
   You: Add error logging
   [Agent continues building on previous code]
   ```

5. **Get Explanations**
   ```
   You: Explain this regex pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
   [Agent breaks it down part by part]
   ```

### 🚧 Best Practices

1. **Start Simple**
   - Begin with basic requests
   - Then add complexity
   - Let the agent build on previous work

2. **Review Generated Code**
   - Always review what the agent creates
   - Test before using in production
   - Ask for improvements if needed

3. **Use Clear Language**
   - Be explicit about requirements
   - Use formatting (bullet points, numbers)
   - Mention constraints (performance, compatibility)

4. **Maintain Context**
   - Use `/history` to review conversation
   - Reference previous files/functions
   - Build incrementally

5. **Provide Feedback**
   ```
   You: That's good, but can you add error handling?
   You: Can you make it more efficient?
   You: Can you add documentation?
   ```

### ⚠️ Safety Considerations

1. **Code Execution Timeout**: 10 seconds max
2. **File Operations**: Limited to accessible paths
3. **Always Review Code**: Before running in production
4. **Test First**: Run in safe environments first
5. **API Keys**: Never share your API key

## Common Scenarios

### Scenario 1: Learning a New Framework

```
You: I'm learning FastAPI. Show me:
- A basic hello world endpoint
- How to handle POST requests
- How to validate request body with Pydantic
- How to add error handling

Agent: [Creates complete FastAPI example]
       [Explains each part]
       [Can test it for you]
```

### Scenario 2: Data Processing

```
You: I have a CSV file. Help me:
1. Read and parse it
2. Clean the data
3. Calculate statistics
4. Export results

Agent: [Creates complete data pipeline]
       [Shows sample output]
```

### Scenario 3: Debugging

```
You: My script keeps failing. Here's the error: [error message]
Read my script and fix it.

Agent: [Reads script]
       [Identifies issue]
       [Creates fixed version]
       [Explains what was wrong]
```

## Keyboard Shortcuts

- `Ctrl+C`: Interrupt current operation
- `Ctrl+D`: Exit (in some shells)
- `Up/Down Arrows`: Navigate command history
- `Ctrl+L`: Clear screen (in terminal)

## Environment Variables

If keyring setup has issues, use environment variable:

```bash
export GROQ_API_KEY="your-api-key-here"
python main.py chat
```

## Troubleshooting

### Agent Takes Too Long to Respond
- It's thinking/processing
- Some complex operations take time
- Be patient, don't interrupt

### File Not Found Errors
- Ensure you're in correct directory
- Use relative paths correctly
- Ask agent to list files first

### API Key Errors
- Verify key is correct
- Check if key has expired
- Run `python main.py setup` again

### Code Execution Timeout
- Break code into smaller parts
- Optimize infinite loops
- Remove heavy computations

---

**Happy Coding! 🚀**
