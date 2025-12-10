import os
import subprocess
import json
from pathlib import Path
from typing import Any
from rich.console import Console

console = Console()


class CodingTools:
    """Provides tools for the coding agent"""

    @staticmethod
    def read_file(file_path: str) -> dict[str, Any]:
        """Read contents of a file"""
        try:
            path = Path(file_path)
            if not path.exists():
                return {"success": False, "error": f"File not found: {file_path}"}
            if not path.is_file():
                return {"success": False, "error": f"Not a file: {file_path}"}
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            return {"success": True, "content": content}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def write_file(file_path: str, content: str) -> dict[str, Any]:
        """Write content to a file"""
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return {"success": True, "message": f"File written: {file_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def list_files(directory: str = ".") -> dict[str, Any]:
        """List files in directory"""
        try:
            path = Path(directory)
            if not path.exists():
                return {"success": False, "error": f"Directory not found: {directory}"}
            files = [
                str(f.relative_to(path))
                for f in path.rglob("*")
                if f.is_file() and not str(f.relative_to(path)).startswith(".")
            ][:50]
            return {"success": True, "files": files[:50]}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def execute_python(code: str) -> dict[str, Any]:
        """Execute Python code safely"""
        try:
            result = subprocess.run(
                ["python", "-c", code],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return {
                "success": True,
                "output": result.stdout,
                "error": result.stderr if result.stderr else None,
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Code execution timeout (10s)"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def bash_command(command: str) -> dict[str, Any]:
        """Execute bash command"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10,
            )
            return {
                "success": True,
                "output": result.stdout,
                "error": result.stderr if result.stderr else None,
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Command timeout (10s)"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def get_tool_definitions() -> list[dict]:
        """Get tool definitions for Groq API"""
        return [
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "description": "Read the contents of a file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Path to the file to read",
                            }
                        },
                        "required": ["file_path"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "description": "Write content to a file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Path to the file to write",
                            },
                            "content": {
                                "type": "string",
                                "description": "Content to write to the file",
                            },
                        },
                        "required": ["file_path", "content"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "list_files",
                    "description": "List files in a directory",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "directory": {
                                "type": "string",
                                "description": "Directory path (default: current directory)",
                            }
                        },
                        "required": [],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "execute_python",
                    "description": "Execute Python code",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "Python code to execute",
                            }
                        },
                        "required": ["code"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "bash_command",
                    "description": "Execute bash command",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "Bash command to execute",
                            }
                        },
                        "required": ["command"],
                    },
                },
            },
        ]

    @staticmethod
    def execute_tool(tool_name: str, tool_input: dict) -> str:
        """Execute a tool and return result as string"""
        try:
            if tool_name == "read_file":
                result = CodingTools.read_file(tool_input.get("file_path", ""))
            elif tool_name == "write_file":
                result = CodingTools.write_file(
                    tool_input.get("file_path", ""), tool_input.get("content", "")
                )
            elif tool_name == "list_files":
                result = CodingTools.list_files(tool_input.get("directory", "."))
            elif tool_name == "execute_python":
                result = CodingTools.execute_python(tool_input.get("code", ""))
            elif tool_name == "bash_command":
                result = CodingTools.bash_command(tool_input.get("command", ""))
            else:
                result = {"success": False, "error": f"Unknown tool: {tool_name}"}
            return json.dumps(result)
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})
