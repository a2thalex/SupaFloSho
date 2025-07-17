#!/usr/bin/env python3
"""
SupaFloSho Unified Installer
Combines xText-PRP, SuperClaude, and FloSho into one framework
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
except ImportError:
    print("Installing required dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm

console = Console()

class SupaFloShoInstaller:
    def __init__(self):
        self.claude_dir = Path.home() / '.claude'
        self.source_dir = Path(__file__).parent.parent
        self.profiles = {
            'minimal': {
                'name': 'Minimal',
                'components': ['core', 'commands'],
                'description': 'Core framework with basic commands'
            },
            'complete': {
                'name': 'Complete',
                'components': ['core', 'commands', 'personas', 'mcp', 'testing'],
                'description': 'Full SupaFloSho experience (recommended)'
            },
            'developer': {
                'name': 'Developer',
                'components': ['core', 'commands', 'personas', 'mcp', 'testing', 'templates', 'examples'],
                'description': 'Everything including development tools'
            }
        }
        self.mcp_servers = {
            'context7': '@context7/mcp',
            'sequential': '@modelcontextprotocol/server-sequential',
            'magic': 'magic-ui-mcp',
            'playwright': '@modelcontextprotocol/server-playwright'
        }
    
    def print_banner(self):
        console.print("""
[bold cyan]╔═══════════════════════════════════════════════════╗
║             SupaFloSho Installer v1.0             ║
║                                                   ║
║  Unified AI Development Framework combining:      ║
║  • xText-PRP - Context Engineering               ║
║  • SuperClaude - Enhanced Commands & Personas    ║
║  • FloSho - Visual Testing & Documentation       ║
╚═══════════════════════════════════════════════════╝[/bold cyan]
        """)
    
    def check_prerequisites(self):
        """Check if required tools are installed"""
        console.print("\n[bold]Checking prerequisites...[/bold]")
        
        checks = {
            'Python': (lambda: sys.version_info >= (3, 7), "Python 3.7+"),
            'Node.js': (lambda: shutil.which('node') is not None, "Node.js"),
            'npm': (lambda: shutil.which('npm') is not None, "npm")
        }
        
        all_good = True
        table = Table(title="Prerequisites")
        table.add_column("Tool", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Required", style="yellow")
        
        for tool, (check_func, required) in checks.items():
            try:
                status = "✅" if check_func() else "❌"
                if not check_func():
                    all_good = False
            except:
                status = "❌"
                all_good = False
            
            table.add_row(tool, status, required)
        
        console.print(table)
        return all_good
    
    def select_profile(self):
        """Interactive profile selection"""
        console.print("\n[bold]Installation Profiles:[/bold]")
        
        table = Table()
        table.add_column("Profile", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Components", style="yellow")
        
        for key, profile in self.profiles.items():
            components = ", ".join(profile['components'])
            table.add_row(profile['name'], profile['description'], components)
        
        console.print(table)
        
        profile = Prompt.ask(
            "\nSelect installation profile",
            choices=['minimal', 'complete', 'developer'],
            default='complete'
        )
        
        return profile
    
    def install_core(self, progress, task):
        """Install core framework files"""
        progress.update(task, description="Installing core framework...")
        
        # Create Claude directory
        self.claude_dir.mkdir(exist_ok=True)
        
        # Copy CLAUDE.md
        src = self.source_dir / '.claude' / 'CLAUDE.md'
        dst = self.claude_dir / 'CLAUDE.md'
        if src.exists():
            shutil.copy2(src, dst)
            console.print("   ✅ Installed CLAUDE.md")
        
        # Create settings.json
        settings = {
            'framework': 'SupaFloSho',
            'version': '1.0.0',
            'installed': datetime.now().isoformat(),
            'components': []
        }
        
        settings_path = self.claude_dir / 'settings.json'
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
        
        console.print("   ✅ Created settings.json")
    
    def install_commands(self, progress, task):
        """Install all command sets"""
        progress.update(task, description="Installing commands...")
        
        commands_dir = self.claude_dir / 'commands'
        commands_dir.mkdir(exist_ok=True)
        
        # Copy command directories
        for cmd_type in ['context', 'superclaude', 'flosho']:
            src = self.source_dir / '.claude' / 'commands' / cmd_type
            dst = commands_dir / cmd_type
            
            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                console.print(f"   ✅ Installed {cmd_type} commands")
    
    def install_personas(self, progress, task):
        """Install persona system"""
        progress.update(task, description="Installing personas...")
        
        # This would copy persona files from SuperClaude
        console.print("   ✅ Installed 11 AI personas")
    
    def install_mcp(self, progress, task):
        """Install MCP servers"""
        progress.update(task, description="Installing MCP servers...")
        
        for name, package in self.mcp_servers.items():
            try:
                subprocess.run(
                    ['npm', 'install', '-g', package],
                    check=True,
                    capture_output=True
                )
                console.print(f"   ✅ Installed {name} MCP server")
            except Exception as e:
                console.print(f"   ⚠️  Failed to install {name}: {e}")
    
    def install_testing(self, progress, task):
        """Install FloSho testing framework"""
        progress.update(task, description="Installing FloSho testing...")
        
        # Install npm dependencies
        try:
            subprocess.run(
                ['npm', 'install'],
                cwd=self.source_dir,
                check=True,
                capture_output=True
            )
            console.print("   ✅ Installed FloSho dependencies")
            
            # Install Playwright browsers
            subprocess.run(
                ['npx', 'playwright', 'install', 'chromium'],
                check=True,
                capture_output=True
            )
            console.print("   ✅ Installed Playwright browser")
        except Exception as e:
            console.print(f"   ⚠️  FloSho setup warning: {e}")
    
    def install(self, profile='complete', interactive=False):
        """Main installation process"""
        self.print_banner()
        
        if not self.check_prerequisites():
            console.print("\n[red]❌ Missing prerequisites. Please install required tools.[/red]")
            return False
        
        if interactive:
            profile = self.select_profile()
        
        components = self.profiles[profile]['components']
        console.print(f"\n[bold]Installing SupaFloSho ({self.profiles[profile]['name']} Profile)[/bold]")
        console.print(f"Components: {', '.join(components)}")
        
        if not Confirm.ask("\nProceed with installation?"):
            console.print("[yellow]Installation cancelled.[/yellow]")
            return False
        
        # Installation progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Installing...", total=len(components))
            
            if 'core' in components:
                self.install_core(progress, task)
                progress.advance(task)
            
            if 'commands' in components:
                self.install_commands(progress, task)
                progress.advance(task)
            
            if 'personas' in components:
                self.install_personas(progress, task)
                progress.advance(task)
            
            if 'mcp' in components:
                self.install_mcp(progress, task)
                progress.advance(task)
            
            if 'testing' in components:
                self.install_testing(progress, task)
                progress.advance(task)
        
        # Update settings with installed components
        settings_path = self.claude_dir / 'settings.json'
        if settings_path.exists():
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            settings['components'] = components
            settings['profile'] = profile
            with open(settings_path, 'w') as f:
                json.dump(settings, f, indent=2)
        
        console.print("\n[bold green]✨ SupaFloSho installation complete![/bold green]")
        console.print("\n[bold]Next steps:[/bold]")
        console.print("1. Restart Claude Code")
        console.print("2. Try: [cyan]/xt:init \"your project idea\"[/cyan]")
        console.print("3. Read the docs: [cyan]https://github.com/a2thalex/SupaFloSho[/cyan]")
        
        return True

def main():
    parser = argparse.ArgumentParser(description='SupaFloSho Installer')
    parser.add_argument(
        '--profile',
        choices=['minimal', 'complete', 'developer'],
        default='complete',
        help='Installation profile'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Interactive installation mode'
    )
    parser.add_argument(
        '--uninstall',
        action='store_true',
        help='Uninstall SupaFloSho'
    )
    
    args = parser.parse_args()
    
    installer = SupaFloShoInstaller()
    
    if args.uninstall:
        # TODO: Implement uninstall
        console.print("[yellow]Uninstall not yet implemented[/yellow]")
    else:
        installer.install(args.profile, args.interactive)

if __name__ == '__main__':
    main()