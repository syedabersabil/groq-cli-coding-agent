#!/usr/bin/env python3
import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from config import ConfigManager
from agent import CodingAgent

console = Console()


def show_banner():
    """Display welcome banner"""
    banner_text = """
    ╭──────────────────────────────╮
    │  [bold cyan]🚀 Groq CLI Coding Agent[/bold cyan] │
    │  AI-Powered Code Assistant   │
    ╭──────────────────────────────╮
    """
    console.print(banner_text)


def show_welcome():
    """Display welcome message"""
    welcome = Panel(
        "[bold]Welcome to Groq CLI Coding Agent![/bold]\n\n"
        "Type your coding questions or commands.\n"
        "Use [cyan]/help[/cyan] for available commands.",
        border_style="green",
        title="[green]✅ Ready[/green]",
    )
    console.print(welcome)


@click.group()
def cli():
    """Groq CLI Coding Agent"""
    pass


@cli.command()
def setup():
    """Setup API key"""
    config_manager = ConfigManager()
    if config_manager.setup_api_key():
        console.print("\n[green]✓ Setup complete![/green]")
    else:
        console.print("\n[red]✗ Setup failed![/red]")
        sys.exit(1)


@cli.command()
@click.option(
    "--quick",
    "-q",
    is_flag=True,
    help="Quick mode (single query, no interactive loop)",
)
@click.argument("query", required=False, default=None)
def chat(quick, query):
    """Start interactive chat with the agent"""
    config_manager = ConfigManager()

    # Check if API key is configured
    api_key = config_manager.get_api_key()
    if not api_key:
        console.print(
            "\n[red]✗ API key not configured![/red]\n"
            "Run: [cyan]python main.py setup[/cyan] to configure."
        )
        sys.exit(1)

    try:
        show_banner()
        agent = CodingAgent(api_key)

        # Quick mode: process single query
        if quick and query:
            console.print(f"\n[cyan]👤 You:[/cyan] {query}\n")
            console.print(f"[green]🤖 Agent:[/green] ", end="")
            agent.stream_response(query)
            return

        # Interactive mode
        show_welcome()

        while True:
            try:
                user_input = console.input(
                    "\n[cyan]👤 You:[/cyan] "
                ).strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.startswith("/"):
                    if user_input == "/exit":
                        console.print("\n[yellow]🚫 Goodbye![/yellow]")
                        break
                    elif user_input == "/clear":
                        agent.clear_history()
                    elif user_input == "/history":
                        agent.show_history()
                    elif user_input == "/help":
                        agent.show_commands()
                    else:
                        console.print(f"[red]Unknown command: {user_input}[/red]")
                    continue

                # Stream response
                console.print(f"\n[green]🤖 Agent:[/green] ", end="")
                agent.stream_response(user_input)

            except KeyboardInterrupt:
                console.print("\n\n[yellow]🚫 Interrupted. Goodbye![/yellow]")
                break
            except Exception as e:
                console.print(f"\n[red]✗ Error: {e}[/red]")

    except Exception as e:
        console.print(f"[red]✗ Error: {e}[/red]")
        sys.exit(1)


@cli.command()
def status():
    """Check configuration status"""
    config_manager = ConfigManager()
    api_key_set = config_manager.check_api_key()
    config = config_manager.load_config()

    status_info = Panel(
        f"API Key Configured: [{'green'}✓[/] yes" if api_key_set else "[red]✗[/] no\n",
        title="[bold]Status[/bold]",
        border_style="blue",
    )
    console.print(status_info)


if __name__ == "__main__":
    cli()
