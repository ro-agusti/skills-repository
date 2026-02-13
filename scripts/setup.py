#!/usr/bin/env python3
"""
Setup Script - Configuración inicial del repositorio
"""
import os
import sys
from pathlib import Path
from typing import List

def create_directories(base_path: Path, dirs: List[str]):
    """Crea directorios necesarios"""
    for dir_path in dirs:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Creado: {dir_path}")

def setup_git_hooks(repo_path: Path):
    """Configura git hooks"""
    hooks_dir = repo_path / '.git' / 'hooks'
    
    if not hooks_dir.exists():
        print("⚠ No se encontró directorio .git/hooks (¿no es un repo git?)")
        return
    
    # Pre-commit hook
    pre_commit_hook = hooks_dir / 'pre-commit'
    hook_content = """#!/bin/bash
# Pre-commit hook para validación

echo "🔍 Ejecutando validaciones..."

# Black formatting check
black --check . || {
    echo "❌ Código no formateado. Ejecuta: black ."
    exit 1
}

# Flake8 linting
flake8 . --max-line-length=100 --exclude=venv,env || {
    echo "❌ Problemas de linting encontrados"
    exit 1
}

# Tests rápidos
pytest tests/unit --maxfail=1 || {
    echo "❌ Tests unitarios fallaron"
    exit 1
}

echo "✅ Validaciones pasadas!"
"""
    
    pre_commit_hook.write_text(hook_content)
    os.chmod(pre_commit_hook, 0o755)
    print("✓ Git pre-commit hook configurado")

def create_env_template(repo_path: Path):
    """Crea template de .env"""
    env_template = repo_path / '.env.template'
    content = """# Configuración de Environment Variables

# API Keys (si es necesario)
ANTHROPIC_API_KEY=your-api-key-here
OPENAI_API_KEY=your-api-key-here

# Configuración
DEBUG=false
LOG_LEVEL=info

# Paths (opcional)
SKILLS_DIR=skills/
COMPOUND_DIR=compound/

# Otros
MAX_WORKERS=4
CACHE_ENABLED=true
"""
    env_template.write_text(content)
    print("✓ Template .env.template creado")

def main():
    """Función principal de setup"""
    print("🚀 Configurando Skills Repository...\n")
    
    repo_path = Path(__file__).parent.parent
    os.chdir(repo_path)
    
    # 1. Verificar Python version
    if sys.version_info < (3, 8):
        print("❌ Se requiere Python 3.8 o superior")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # 2. Crear directorios adicionales si no existen
    additional_dirs = [
        'logs',
        'cache',
        '.skill_cache',
        'temp',
    ]
    
    print("\n📁 Creando directorios...")
    create_directories(repo_path, additional_dirs)
    
    # 3. Configurar git hooks
    print("\n🪝 Configurando git hooks...")
    setup_git_hooks(repo_path)
    
    # 4. Crear .env template
    print("\n⚙️ Configurando environment...")
    create_env_template(repo_path)
    
    # 5. Verificar instalación de dependencias
    print("\n📦 Verificando dependencias...")
    try:
        import yaml
        import click
        print("✓ Dependencias principales instaladas")
    except ImportError as e:
        print(f"⚠ Falta dependencia: {e.name}")
        print("  Ejecuta: pip install -r requirements.txt")
    
    # 6. Crear skill de ejemplo si no existe
    print("\n📝 Verificando skills de ejemplo...")
    example_skill = repo_path / 'skills' / 'ai-prompts' / 'text-summarizer'
    if example_skill.exists():
        print("✓ Skill de ejemplo ya existe")
    else:
        print("ℹ Para crear un skill de ejemplo, ejecuta:")
        print("  python scripts/skill-manager.py create --name text-summarizer --type ai-prompts")
    
    # 7. Resumen final
    print("\n" + "="*60)
    print("✅ Setup completado!")
    print("="*60)
    print("\n📚 Próximos pasos:")
    print("1. Copia .env.template a .env y configura tus variables")
    print("2. Lee la documentación en docs/guides/QUICKSTART.md")
    print("3. Crea tu primer skill:")
    print("   python scripts/skill-manager.py create --name mi-skill --type ai-prompts")
    print("\n💡 Comandos útiles:")
    print("  - Listar skills: python scripts/skill-manager.py list")
    print("  - Ejecutar tests: pytest")
    print("  - Ver documentación: cat README.md")
    print("\n🎉 ¡Feliz coding!")

if __name__ == '__main__':
    main()
