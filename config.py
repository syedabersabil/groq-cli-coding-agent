import os
import json
from pathlib import Path
from typing import Optional
import keyring
from rich.console import Console
from rich.prompt import Prompt

console = Console()

CONFIG_DIR = Path.home() / ".groq_agent"
CONFIG_FILE = CONFIG_DIR / "config.json"
SERVICE_NAME = "groq-cli-agent"


class ConfigManager:
    """Manages API keys and configuration"""

    def __init__(self):
        self.config_dir = CONFIG_DIR
        self.config_file = CONFIG_FILE
        self.ensure_config_dir()

    @staticmethod
    def ensure_config_dir():
        """Create config directory if it doesn't exist"""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    def get_api_key(self) -> Optional[str]:
        """Get API key from keyring or environment"""
        # Check environment variable first
        if api_key := os.getenv("GROQ_API_KEY"):
            return api_key

        # Check keyring
        try:
            if api_key := keyring.get_password(SERVICE_NAME, "api_key"):
                return api_key
        except Exception as e:
            console.print(f"[yellow]Keyring error: {e}[/yellow]")

        return None

    def set_api_key(self, api_key: str) -> bool:
        """Store API key securely in keyring"""
        try:
            keyring.set_password(SERVICE_NAME, "api_key", api_key)
            console.print("[green]✓ API key saved securely[/green]")
            return True
        except Exception as e:
            console.print(f"[red]✗ Failed to save API key: {e}[/red]")
            return False

    def save_config(self, config_data: dict) -> bool:
        """Save configuration to JSON file"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(config_data, f, indent=2)
            return True
        except Exception as e:
            console.print(f"[red]✗ Failed to save config: {e}[/red]")
            return False

    def load_config(self) -> dict:
        """Load configuration from JSON file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to load config: {e}[/yellow]")
        return {}

    def setup_api_key(self) -> bool:
        """Interactive API key setup"""
        console.print("\n[bold cyan]🔐 API Key Setup[/bold cyan]")
        console.print("Get your API key from: [blue]https://console.groq.com[/blue]\n")

        api_key = Prompt.ask("Enter your Groq API key")

        if not api_key or len(api_key) < 10:
            console.print("[red]✗ Invalid API key format[/red]")
            return False

        if self.set_api_key(api_key):
            config = self.load_config()
            config["api_key_set"] = True
            self.save_config(config)
            return True

        return False

    def check_api_key(self) -> bool:
        """Check if API key is configured"""
        return bool(self.get_api_key())
