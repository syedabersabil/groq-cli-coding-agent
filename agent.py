import json
from typing import Optional
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from config import ConfigManager
from tools import CodingTools

console = Console()


class CodingAgent:
    """AI Coding Agent using Groq API"""

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.model = "mixtral-8x7b-32768"
        self.conversation_history = []
        self.tools = CodingTools.get_tool_definitions()
        self.max_retries = 5

    def add_message(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})

    def get_system_prompt(self) -> str:
        """Get system prompt for the agent"""
        return """You are an expert AI coding assistant with access to powerful tools for file operations and code execution. You help users write, debug, and improve code.

You can:
- Read and write files
- List files in directories
- Execute Python code
- Run bash commands
- Analyze code and provide improvements

Always explain your actions and provide clear, helpful responses. Use tools when necessary to help the user.
When suggesting code, provide complete working examples.
Be safety-conscious and warn users about potentially dangerous operations."""

    def process_tool_call(self, tool_name: str, tool_input: dict) -> str:
        """Process a tool call and return result"""
        console.print(f"\n[cyan]→ Using tool: {tool_name}[/cyan]")
        result = CodingTools.execute_tool(tool_name, tool_input)
        return result

    def stream_response(self, user_input: str) -> bool:
        """Stream response from Groq API with tool support"""
        self.add_message("user", user_input)

        try:
            # Check if this is a tool-requiring request
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.get_system_prompt()},
                    *self.conversation_history,
                ],
                tools=self.tools,
                max_tokens=8192,
                temperature=0.7,
                stream=True,
            )

            full_response = ""
            current_tool_call = None
            tool_calls = []

            for chunk in response:
                delta = chunk.choices[0].delta

                # Handle content streaming
                if delta.content:
                    console.print(delta.content, end="", highlight=False)
                    full_response += delta.content

                # Handle tool use
                if hasattr(delta, "tool_calls") and delta.tool_calls:
                    for tool_call in delta.tool_calls:
                        if hasattr(tool_call, "id") and tool_call.id:
                            current_tool_call = {
                                "id": tool_call.id,
                                "function": {"name": "", "arguments": ""},
                            }
                            tool_calls.append(current_tool_call)

                        if hasattr(tool_call, "function"):
                            if hasattr(tool_call.function, "name"):
                                current_tool_call["function"]["name"] = (
                                    tool_call.function.name
                                )
                            if hasattr(tool_call.function, "arguments"):
                                current_tool_call["function"]["arguments"] += (
                                    tool_call.function.arguments
                                )

            console.print()  # New line after streaming

            # Process tool calls if any
            if tool_calls:
                self.add_message("assistant", full_response)

                for tool_call in tool_calls:
                    tool_name = tool_call["function"]["name"]
                    try:
                        tool_input = json.loads(
                            tool_call["function"]["arguments"]
                        )
                    except json.JSONDecodeError:
                        tool_input = {}

                    # Execute tool
                    tool_result = self.process_tool_call(tool_name, tool_input)

                    # Add tool result to history
                    self.add_message(
                        "user",
                        f'Tool "{tool_name}" returned: {tool_result}',
                    )

                    # Get follow-up response
                    console.print("\n[yellow]→ Processing tool result...[/yellow]\n")
                    follow_up = self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": self.get_system_prompt()},
                            *self.conversation_history,
                        ],
                        tools=self.tools,
                        max_tokens=8192,
                        temperature=0.7,
                        stream=True,
                    )

                    followup_response = ""
                    for chunk in follow_up:
                        if chunk.choices[0].delta.content:
                            console.print(
                                chunk.choices[0].delta.content, end="", highlight=False
                            )
                            followup_response += chunk.choices[0].delta.content

                    console.print()  # New line after streaming
                    self.add_message("assistant", followup_response)
            else:
                # No tool calls, just add the response
                self.add_message("assistant", full_response)

            return True

        except Exception as e:
            console.print(f"[red]✗ Error: {e}[/red]")
            return False

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        console.print("[yellow]→ Conversation history cleared[/yellow]")

    def show_commands(self):
        """Display available commands"""
        commands = [
            ("/clear", "Clear conversation history"),
            ("/exit", "Exit the agent"),
            ("/history", "Show conversation history"),
            ("/help", "Show this help message"),
        ]
        panel = Panel(
            "\n".join([f"[cyan]{cmd}[/cyan] - {desc}" for cmd, desc in commands]),
            title="[bold]Available Commands[/bold]",
            border_style="blue",
        )
        console.print(panel)

    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            console.print("[yellow]No conversation history yet[/yellow]")
            return

        for i, msg in enumerate(self.conversation_history, 1):
            role = "[cyan]User[/cyan]" if msg["role"] == "user" else "[green]Agent[/green]"
            preview = msg["content"][:100].replace("\n", " ")
            console.print(f"{i}. {role}: {preview}...")
