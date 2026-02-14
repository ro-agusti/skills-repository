#!/usr/bin/env python3
"""
Setup Script - Initial repository setup
"""
import os
import sys
from pathlib import Path
from typing import List

def create_directories(base_path: Path, dirs: List[str]):
    """Create required directories"""
    for dir_path in dirs:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}")

def setup_git_hooks(repo_path: Path):
    """Configure git hooks"""
    hooks_dir = repo_path / '.git' / 'hooks'
    
    if not hooks_dir.exists():
        print("⚠ .git/hooks directory not found (is this not a git repo?)")
        return
    
    # Pre-commit hook
    pre_commit_hook = hooks_dir / 'pre-commit'
    hook_content = """#!/bin/bash
# Pre-commit hook for validation

echo "🔍 Running validations..."

# Black formatting check
black --check . || {
    echo "❌ Code not formatted. Run: black ."
    exit 1
}

# Flake8 linting
flake8 . --max-line-length=100 --exclude=venv,env || {
    echo "❌ Linting issues found"
    exit 1
}

# Quick tests
pytest tests/unit --maxfail=1 || {
    echo "❌ Unit tests failed"
    exit 1
}

echo "✅ Validations passed!"
"""
    
    pre_commit_hook.write_text(hook_content)
    os.chmod(pre_commit_hook, 0o755)
    print("✓ Git pre-commit hook configured")

def create_env_template(repo_path: Path):
    """Create .env template"""
    env_template = repo_path / '.env.template'
    content = """# Environment Variables Configuration

# API Keys (if needed)
ANTHROPIC_API_KEY=your-api-key-here
OPENAI_API_KEY=your-api-key-here

# Settings
DEBUG=false
LOG_LEVEL=info

# Paths (optional)
SKILLS_DIR=skills/
COMPOUND_DIR=compound/

# Others
MAX_WORKERS=4
CACHE_ENABLED=true
"""
    env_template.write_text(content)
    print("✓ .env.template created")

def main():
    """Main setup function"""
    print("🚀 Setting up Skills Repository...\n")
    
    repo_path = Path(__file__).parent.parent
    os.chdir(repo_path)
    
    # 1. Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # 2. Create additional directories if they don't exist
    additional_dirs = [
        'logs',
        'cache',
        '.skill_cache',
        'temp',
    ]
    
    print("\n📁 Creating directories...")
    create_directories(repo_path, additional_dirs)
    
    # 3. Configure git hooks
    print("\n🪝 Configuring git hooks...")
    setup_git_hooks(repo_path)
    
    # 4. Create .env template
    print("\n⚙️ Setting up environment...")
    create_env_template(repo_path)
    
    # 5. Check dependencies
    print("\n📦 Checking dependencies...")
    try:
        import yaml
        import click
        print("✓ Main dependencies installed")
    except ImportError as e:
        print(f"⚠ Missing dependency: {e.name}")
        print("  Run: pip install -r requirements.txt")
    
    # 6. Create example skill if it doesn't exist
    print("\n📝 Checking example skills...")
    example_skill = repo_path / 'skills' / 'ai-prompts' / 'text-summarizer'
    if example_skill.exists():
        print("✓ Example skill already exists")
    else:
        print("ℹ To create an example skill, run:")
        print("  python scripts/skill-manager.py create --name text-summarizer --type ai-prompts")
    
    # 7. Final summary
    print("\n" + "="*60)
    print("✅ Setup completed!")
    print("="*60)
    print("\n📚 Next steps:")
    print("1. Copy .env.template to .env and configure your variables")
    print("2. Read documentation at docs/guides/QUICKSTART.md")
    print("3. Create your first skill:")
    print("   python scripts/skill-manager.py create --name my-skill --type ai-prompts")
    print("\n💡 Useful commands:")
    print("  - List skills: python scripts/skill-manager.py list")
    print("  - Run tests: pytest")
    print("  - View documentation: cat README.md")
    print("\n🎉 Happy coding!")

if __name__ == '__main__':
    main()
