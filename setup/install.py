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

class SupaFloShoInstaller:
    def __init__(self):
        self.home_dir = Path.home()
        self.claude_dir = self.home_dir / '.claude'
        self.repo_dir = Path(__file__).parent.parent
        
        self.profiles = {
            'minimal': {
                'name': 'Minimal',
                'components': ['core', 'commands'],
                'description': 'Core framework with basic commands'
            },
            'standard': {
                'name': 'Standard',
                'components': ['core', 'commands', 'personas', 'testing'],
                'description': 'Standard installation with testing framework'
            },
            'complete': {
                'name': 'Complete',
                'components': ['core', 'commands', 'personas', 'testing', 'templates'],
                'description': 'Everything except MCP servers'
            },
            'developer': {
                'name': 'Developer',
                'components': ['core', 'commands', 'personas', 'testing', 'templates', 'examples', 'mcp'],
                'description': 'Full installation including MCP tools (optional)'
            }
        }
        
        # Correct MCP packages based on actual npm registry
        self.mcp_packages = {
            'sdk': '@modelcontextprotocol/sdk',
            'filesystem': '@modelcontextprotocol/server-filesystem',
            'inspector': '@modelcontextprotocol/inspector',
            'framework': 'mcp-framework'
        }

    def print_banner(self):
        banner = """
╔═══════════════════════════════════════════════════════════╗
║                    SupaFloSho Installer                    ║
║                                                           ║
║  Unified AI-Driven Development Framework                  ║
║  Combining: xText-PRP + SuperClaude + FloSho             ║
╚═══════════════════════════════════════════════════════════╝
        """
        print(banner)

    def check_prerequisites(self):
        """Check if required tools are installed"""
        print("\n📋 Checking prerequisites...")
        
        # Check Python version
        if sys.version_info < (3, 7):
            print("❌ Python 3.7+ required")
            return False
        print("✅ Python version OK")
        
        # Check Node.js
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Node.js installed")
            else:
                raise Exception()
        except:
            print("❌ Node.js not found - required for FloSho and MCP")
            print("   Install from: https://nodejs.org/")
            return False
        
        # Check npm
        try:
            subprocess.run(['npm', '--version'], capture_output=True, check=True)
            print("✅ npm installed")
        except:
            print("❌ npm not found")
            return False
        
        return True

    def install_core(self):
        """Install core framework files"""
        print("\n📦 Installing core framework...")
        
        # Create .claude directory
        self.claude_dir.mkdir(exist_ok=True)
        
        # Copy CLAUDE.md
        shutil.copy2(
            self.repo_dir / '.claude' / 'CLAUDE.md',
            self.claude_dir / 'CLAUDE.md'
        )
        print("✅ Installed CLAUDE.md")
        
        # Copy core documentation
        core_files = ['COMMANDS.md', 'FLAGS.md', 'RULES.md', 'PRINCIPLES.md']
        for file in core_files:
            if (self.repo_dir / 'core' / file).exists():
                shutil.copy2(
                    self.repo_dir / 'core' / file,
                    self.claude_dir / file
                )
                print(f"✅ Installed {file}")

    def install_commands(self):
        """Install all command definitions"""
        print("\n📝 Installing commands...")
        
        commands_dir = self.claude_dir / 'commands'
        commands_dir.mkdir(exist_ok=True)
        
        # Copy command categories
        for category in ['context', 'superclaude', 'flosho']:
            src_dir = self.repo_dir / '.claude' / 'commands' / category
            dst_dir = commands_dir / category
            
            if src_dir.exists():
                shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
                print(f"✅ Installed {category} commands")

    def install_personas(self):
        """Install persona system"""
        print("\n🎭 Installing personas...")
        
        personas_file = self.repo_dir / 'core' / 'personas' / 'PERSONAS.md'
        if personas_file.exists():
            shutil.copy2(personas_file, self.claude_dir / 'PERSONAS.md')
            print("✅ Installed persona system")

    def install_testing(self):
        """Install FloSho testing framework"""
        print("\n🧪 Installing FloSho testing framework...")
        
        # Install npm dependencies
        testing_dir = self.repo_dir / 'testing'
        if testing_dir.exists():
            os.chdir(testing_dir)
            
            print("📦 Installing npm packages...")
            subprocess.run(['npm', 'install'], check=True)
            
            # Install Playwright browsers
            print("🌐 Installing Playwright browsers...")
            subprocess.run(['npx', 'playwright', 'install', 'chromium'], check=True)
            
            print("✅ FloSho testing framework installed")

    def install_mcp(self):
        """Install MCP servers with correct packages"""
        print("\n🔧 Optional: MCP Server Installation")
        print("MCP (Model Context Protocol) enables advanced AI-to-tool connections.")
        
        response = input("\nInstall MCP development tools? [y/N]: ")
        if response.lower() != 'y':
            print("⏭️  Skipping MCP installation")
            return
        
        print("\n📦 Installing MCP packages...")
        
        # Install MCP SDK for development
        packages_to_install = []
        
        print("\nWhich MCP packages would you like to install?")
        print("1. SDK - Core development kit (recommended)")
        print("2. Filesystem Server - File access capabilities")
        print("3. Inspector - Debugging tool")
        print("4. Framework - Full MCP server framework")
        print("5. All of the above")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1' or choice == '5':
            packages_to_install.append(self.mcp_packages['sdk'])
        if choice == '2' or choice == '5':
            packages_to_install.append(self.mcp_packages['filesystem'])
        if choice == '3' or choice == '5':
            packages_to_install.append(self.mcp_packages['inspector'])
        if choice == '4' or choice == '5':
            packages_to_install.append(self.mcp_packages['framework'])
        
        for package in packages_to_install:
            print(f"📦 Installing {package}...")
            try:
                # Install locally in the project instead of globally
                subprocess.run(['npm', 'install', package], 
                             cwd=self.repo_dir,
                             check=True)
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"⚠️  Failed to install {package}")
        
        if packages_to_install:
            self.create_mcp_config()

    def create_mcp_config(self):
        """Create MCP configuration for Claude"""
        print("\n📝 Creating MCP configuration...")
        
        mcp_config = {
            "servers": {
                "filesystem": {
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        str(self.home_dir / "Documents"),
                        str(self.home_dir / "Desktop")
                    ],
                    "description": "Access to Documents and Desktop folders"
                }
            }
        }
        
        mcp_config_path = self.claude_dir / 'mcp-config.json'
        with open(mcp_config_path, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        
        print("✅ Created MCP configuration")
        print("📌 Note: You can edit ~/.claude/mcp-config.json to add more MCP servers")

    def install_templates(self):
        """Install PRP templates"""
        print("\n📋 Installing templates...")
        
        templates_dir = self.claude_dir / 'templates'
        templates_dir.mkdir(exist_ok=True)
        
        src_templates = self.repo_dir / 'templates'
        if src_templates.exists():
            shutil.copytree(src_templates, templates_dir, dirs_exist_ok=True)
            print("✅ Installed PRP templates")

    def install_examples(self):
        """Install example projects"""
        print("\n📚 Installing examples...")
        
        examples_dir = self.claude_dir / 'examples'
        examples_dir.mkdir(exist_ok=True)
        
        src_examples = self.repo_dir / 'examples'
        if src_examples.exists():
            shutil.copytree(src_examples, examples_dir, dirs_exist_ok=True)
            print("✅ Installed example projects")

    def create_settings(self, profile):
        """Create SupaFloSho settings file"""
        settings = {
            "version": "1.0.0",
            "profile": profile,
            "installedComponents": self.profiles[profile]['components'],
            "framework": {
                "xtext": True,
                "superclaude": True,
                "flosho": True
            },
            "features": {
                "prpIntegration": True,
                "smartPersonas": True,
                "visualTesting": True,
                "autoDocumentation": True
            },
            "mcp": {
                "enabled": 'mcp' in self.profiles[profile]['components'],
                "configPath": str(self.claude_dir / 'mcp-config.json')
            }
        }
        
        settings_path = self.claude_dir / 'supaflosho.json'
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
        
        print("✅ Created SupaFloSho settings")

    def install(self, profile='complete', interactive=False):
        """Main installation process"""
        self.print_banner()
        
        if not self.check_prerequisites():
            print("\n❌ Prerequisites not met. Please install missing tools.")
            return False
        
        if interactive:
            profile = self.interactive_setup()
        
        print(f"\n🚀 Installing SupaFloSho ({self.profiles[profile]['name']} profile)...")
        print(f"   {self.profiles[profile]['description']}")
        
        components = self.profiles[profile]['components']
        
        try:
            if 'core' in components:
                self.install_core()
            
            if 'commands' in components:
                self.install_commands()
            
            if 'personas' in components:
                self.install_personas()
            
            if 'testing' in components:
                self.install_testing()
            
            if 'mcp' in components:
                self.install_mcp()
            
            if 'templates' in components:
                self.install_templates()
            
            if 'examples' in components:
                self.install_examples()
            
            self.create_settings(profile)
            
            self.print_success()
            return True
            
        except Exception as e:
            print(f"\n❌ Installation failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    def interactive_setup(self):
        """Interactive installation mode"""
        print("\n🎯 Choose your installation profile:\n")
        
        profiles = list(self.profiles.items())
        for i, (key, profile) in enumerate(profiles):
            print(f"  {i+1}. {profile['name']} - {profile['description']}")
        
        while True:
            try:
                choice = int(input("\nSelect profile (1-4): ")) - 1
                if 0 <= choice < len(profiles):
                    return profiles[choice][0]
            except:
                pass
            print("Invalid choice. Please try again.")

    def print_success(self):
        """Print success message and next steps"""
        success_msg = """
╔═══════════════════════════════════════════════════════════╗
║                 ✨ Installation Complete! ✨               ║
╚═══════════════════════════════════════════════════════════╝

SupaFloSho is ready to use! 🎉

📝 Next Steps:
1. Restart Claude Code to activate the framework
2. Try: /xt:init "your project idea"
3. Then: /sc:implement "feature"
4. Test: /fs:flow "user journey"

📚 Documentation:
- Quick Start: ~/.claude/examples/quick-start.md
- Commands: ~/.claude/COMMANDS.md
- Personas: ~/.claude/PERSONAS.md

💡 MCP Development (if installed):
- Inspector: npx @modelcontextprotocol/inspector
- Create server: npx mcp-framework create my-server
- Docs: https://modelcontextprotocol.io

🌊 Happy coding with SupaFloSho!
        """
        print(success_msg)

    def uninstall(self):
        """Uninstall SupaFloSho"""
        print("\n🗑️ Uninstalling SupaFloSho...")
        
        if self.claude_dir.exists():
            # Backup user data
            backup_dir = self.home_dir / 'supaflosho-backup'
            backup_dir.mkdir(exist_ok=True)
            
            # Only backup user-created content
            for item in ['projects', 'custom-templates']:
                src = self.claude_dir / item
                if src.exists():
                    shutil.move(str(src), str(backup_dir / item))
            
            # Remove SupaFloSho files
            files_to_remove = [
                'CLAUDE.md', 'COMMANDS.md', 'PERSONAS.md', 
                'FLAGS.md', 'RULES.md', 'supaflosho.json',
                'mcp-config.json'
            ]
            
            for file in files_to_remove:
                file_path = self.claude_dir / file
                if file_path.exists():
                    file_path.unlink()
            
            # Remove directories
            dirs_to_remove = ['commands', 'templates', 'examples']
            for dir_name in dirs_to_remove:
                dir_path = self.claude_dir / dir_name
                if dir_path.exists():
                    shutil.rmtree(dir_path)
            
            print("✅ SupaFloSho uninstalled")
            if backup_dir.exists():
                print(f"📁 User data backed up to: {backup_dir}")
        else:
            print("❌ SupaFloSho not found")


def main():
    parser = argparse.ArgumentParser(
        description='SupaFloSho Installer - Unified AI Development Framework'
    )
    
    parser.add_argument(
        'action',
        choices=['install', 'uninstall'],
        help='Action to perform'
    )
    
    parser.add_argument(
        '--profile',
        choices=['minimal', 'standard', 'complete', 'developer'],
        default='complete',
        help='Installation profile (default: complete)'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Interactive installation mode'
    )
    
    args = parser.parse_args()
    
    installer = SupaFloShoInstaller()
    
    if args.action == 'install':
        success = installer.install(args.profile, args.interactive)
        sys.exit(0 if success else 1)
    elif args.action == 'uninstall':
        installer.uninstall()

if __name__ == '__main__':
    main()