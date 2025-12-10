#!/usr/bin/env python3
"""
Examples and tool extension guide for Groq CLI Coding Agent

This file shows how to:
1. Use the agent programmatically
2. Extend with custom tools
3. Handle responses
"""

from agent import CodingAgent
from config import ConfigManager
from tools import CodingTools
import json


# ============================================================================
# EXAMPLE 1: Programmatic Usage
# ============================================================================

def example_basic_usage():
    """Example: Basic programmatic usage of the agent"""
    print("\n=== Example 1: Basic Usage ===")

    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()

    if not api_key:
        print("API key not configured. Run: python main.py setup")
        return

    agent = CodingAgent(api_key)

    # Ask a simple question
    query = "Write a Python function that checks if a number is prime"
    print(f"\nQuery: {query}")
    print("\nResponse:")
    agent.stream_response(query)


# ============================================================================
# EXAMPLE 2: Conversation History
# ============================================================================

def example_conversation_context():
    """Example: Using conversation history for context"""
    print("\n=== Example 2: Conversation Context ===")

    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()

    if not api_key:
        print("API key not configured.")
        return

    agent = CodingAgent(api_key)

    # First message
    print("\n1. Creating a calculator class...")
    agent.stream_response("Create a Python Calculator class with add, subtract, multiply, divide methods")

    # Second message - uses context from first
    print("\n2. Adding error handling...")
    agent.stream_response("Add error handling for division by zero")

    # Third message - continues the conversation
    print("\n3. Adding documentation...")
    agent.stream_response("Add docstrings and type hints to all methods")


# ============================================================================
# EXAMPLE 3: Extending Tools
# ============================================================================

class ExtendedTools(CodingTools):
    """Example: Extending CodingTools with custom tools"""

    @staticmethod
    def get_git_status():
        """Custom tool: Get git status"""
        result = CodingTools.bash_command("git status")
        return result

    @staticmethod
    def count_lines_of_code(directory="."):
        """Custom tool: Count lines of code in Python files"""
        result = CodingTools.bash_command(
            f'find {directory} -name "*.py" -exec wc -l {{}} + | tail -1'
        )
        return result

    @staticmethod
    def list_project_structure(directory="."):
        """Custom tool: Show project tree"""
        result = CodingTools.bash_command(f"tree {directory} -I '__pycache__|*.pyc'")
        return result


def example_custom_tools():
    """Example: Using custom tools"""
    print("\n=== Example 3: Custom Tools ===")

    # Get git status
    print("\nGit Status:")
    result = ExtendedTools.get_git_status()
    print(result)

    # Count lines of code
    print("\nLines of Code:")
    result = ExtendedTools.count_lines_of_code(".")
    print(result)


# ============================================================================
# EXAMPLE 4: File Operations
# ============================================================================

def example_file_operations():
    """Example: File operations with the agent"""
    print("\n=== Example 4: File Operations ===")

    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()

    if not api_key:
        print("API key not configured.")
        return

    agent = CodingAgent(api_key)

    # Create a file
    print("\n1. Creating a test file...")
    test_code = '''def greet(name):
    """Greet someone by name"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
'''
    result = CodingTools.write_file("example_greeting.py", test_code)
    print(f"File created: {result}")

    # Ask agent to analyze the file
    print("\n2. Asking agent to analyze the file...")
    agent.stream_response("Read the file example_greeting.py and tell me what it does")

    # Ask to improve it
    print("\n3. Asking to improve...")
    agent.stream_response("Now improve that function by adding error handling and type hints")


# ============================================================================
# EXAMPLE 5: Code Testing
# ============================================================================

def example_code_testing():
    """Example: Creating and testing code"""
    print("\n=== Example 5: Code Testing ===")

    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()

    if not api_key:
        print("API key not configured.")
        return

    agent = CodingAgent(api_key)

    # Ask agent to create AND test code
    print("\nAsking agent to create and test a function...")
    agent.stream_response(
        "Create a Python function that calculates factorial. "
        "Then test it with inputs 0, 1, 5, and 10 and show the results."
    )


# ============================================================================
# EXAMPLE 6: How to Add Custom Tools to Agent
# ============================================================================

def how_to_add_custom_tools():
    """
    Guide: How to add custom tools to the agent

    Steps:
    1. Add the tool function to tools.py in the CodingTools class
    2. Add the function to get_tool_definitions() return list
    3. Add the tool execution logic to execute_tool() method
    4. Use in agent

    Example:
    """

    example = '''
    # Step 1: Add to tools.py

    @staticmethod
    def search_web(query: str) -> dict[str, Any]:
        """Search the web for something"""
        try:
            # Implementation here
            return {"success": True, "results": [...]}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # Step 2: Add to get_tool_definitions()
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        }
    }

    # Step 3: Add to execute_tool()
    elif tool_name == "search_web":
        result = CodingTools.search_web(tool_input.get("query", ""))

    # Step 4: Use in agent
    agent.stream_response("Search the web for latest Python news")
    '''

    print("\n=== How to Add Custom Tools ===")
    print(example)


# ============================================================================
# EXAMPLE 7: Performance Monitoring
# ============================================================================

def example_with_timing():
    """Example: Track agent response times"""
    import time

    print("\n=== Example 7: Performance Monitoring ===")

    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()

    if not api_key:
        print("API key not configured.")
        return

    agent = CodingAgent(api_key)

    queries = [
        "Write a hello world function in Python",
        "Explain list comprehensions briefly",
        "Create a simple class for a todo item",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{i}. Query: {query}")
        start_time = time.time()
        agent.stream_response(query)
        elapsed_time = time.time() - start_time
        print(f"\n\nTime taken: {elapsed_time:.2f} seconds")


# ============================================================================
# MAIN - Run Examples
# ============================================================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python examples.py <example_number>")
        print("\nAvailable examples:")
        print("1 - Basic Usage")
        print("2 - Conversation Context")
        print("3 - Custom Tools")
        print("4 - File Operations")
        print("5 - Code Testing")
        print("6 - How to Add Custom Tools")
        print("7 - Performance Monitoring")
        sys.exit(1)

    example_num = sys.argv[1]

    try:
        if example_num == "1":
            example_basic_usage()
        elif example_num == "2":
            example_conversation_context()
        elif example_num == "3":
            example_custom_tools()
        elif example_num == "4":
            example_file_operations()
        elif example_num == "5":
            example_code_testing()
        elif example_num == "6":
            how_to_add_custom_tools()
        elif example_num == "7":
            example_with_timing()
        else:
            print(f"Unknown example: {example_num}")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()
