#!/usr/bin/env python3
"""
Skill Manager - Herramienta principal para gestionar skills
"""
import os
import json
import click
from pathlib import Path
from datetime import datetime
from typing import Optional, List

SKILL_TYPES = ['ai-prompts', 'code', 'hybrid']
BASE_DIR = Path(__file__).parent.parent


class SkillManager:
    """Gestor de skills del repositorio"""
    
    def __init__(self, base_path: Path = BASE_DIR):
        self.base_path = base_path
        self.skills_dir = base_path / 'skills'
        
    def create_skill(self, name: str, skill_type: str, description: str = "") -> Path:
        """Crea un nuevo skill desde template"""
        if skill_type not in SKILL_TYPES:
            raise ValueError(f"Tipo debe ser uno de: {SKILL_TYPES}")
        
        skill_path = self.skills_dir / skill_type / name
        
        if skill_path.exists():
            raise FileExistsError(f"El skill ya existe: {skill_path}")
        
        # Crear estructura
        skill_path.mkdir(parents=True, exist_ok=True)
        (skill_path / 'examples').mkdir(exist_ok=True)
        (skill_path / 'tests').mkdir(exist_ok=True)
        
        # Crear archivos base
        self._create_skill_md(skill_path, name, description)
        self._create_metadata(skill_path, name, skill_type, description)
        
        if skill_type == 'ai-prompts':
            self._create_prompt_file(skill_path, name)
        elif skill_type in ['code', 'hybrid']:
            self._create_python_file(skill_path, name)
            
        self._create_test_file(skill_path, name, skill_type)
        self._create_examples_file(skill_path, name)
        
        return skill_path
    
    def _create_skill_md(self, path: Path, name: str, description: str):
        """Crea el archivo SKILL.md"""
        content = f"""# {name}

## Descripción
{description or 'Descripción del skill'}

## Uso

```python
# Ejemplo de uso
```

## Parámetros

- `param1`: Descripción del parámetro

## Ejemplos

Ver carpeta `examples/` para casos de uso detallados.

## Tests

```bash
pytest tests/test_{name.replace('-', '_')}.py
```

## Notas

- Nota 1
- Nota 2

## Changelog

### v1.0.0 - {datetime.now().strftime('%Y-%m-%d')}
- Versión inicial
"""
        (path / 'SKILL.md').write_text(content)
    
    def _create_metadata(self, path: Path, name: str, skill_type: str, description: str):
        """Crea el archivo metadata.json"""
        metadata = {
            "name": name,
            "type": skill_type,
            "version": "1.0.0",
            "description": description,
            "author": "",
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
            "tags": [],
            "dependencies": [],
            "status": "active"
        }
        (path / 'metadata.json').write_text(json.dumps(metadata, indent=2))
    
    def _create_prompt_file(self, path: Path, name: str):
        """Crea archivo de prompt para AI skills"""
        content = f"""# Prompt para {name}

## System Prompt
[Tu prompt de sistema aquí]

## User Prompt Template
[Template de prompt para el usuario]

## Variables
- {{variable1}}: descripción
- {{variable2}}: descripción
"""
        (path / 'prompt.txt').write_text(content)
    
    def _create_python_file(self, path: Path, name: str):
        """Crea archivo Python para code/hybrid skills"""
        module_name = name.replace('-', '_')
        content = f'''"""
{name} - Skill Module
"""

def execute(**kwargs):
    """
    Función principal del skill
    
    Args:
        **kwargs: Parámetros del skill
        
    Returns:
        Resultado de la ejecución
    """
    # Implementación
    pass


class {module_name.title().replace('_', '')}:
    """Clase principal del skill"""
    
    def __init__(self):
        pass
    
    def run(self, *args, **kwargs):
        """Ejecuta el skill"""
        return execute(**kwargs)


if __name__ == "__main__":
    # Ejemplo de uso
    result = execute()
    print(result)
'''
        (path / f'{module_name}.py').write_text(content)
    
    def _create_test_file(self, path: Path, name: str, skill_type: str):
        """Crea archivo de tests"""
        module_name = name.replace('-', '_')
        content = f'''"""
Tests para {name}
"""
import pytest
from pathlib import Path

# Importar el skill
{"# from " + module_name + " import execute" if skill_type != "ai-prompts" else ""}

def test_basic_functionality():
    """Test básico de funcionalidad"""
    assert True  # Reemplazar con test real


def test_with_parameters():
    """Test con parámetros"""
    pass


@pytest.mark.parametrize("input_data,expected", [
    ("input1", "output1"),
    ("input2", "output2"),
])
def test_multiple_cases(input_data, expected):
    """Test con múltiples casos"""
    pass
'''
        (path / 'tests' / f'test_{module_name}.py').write_text(content)
    
    def _create_examples_file(self, path: Path, name: str):
        """Crea archivo de ejemplos"""
        content = f"""# Ejemplos de uso - {name}

## Ejemplo 1: Uso básico

```python
# Código de ejemplo
```

### Resultado esperado
```
Salida esperada
```

## Ejemplo 2: Uso avanzado

```python
# Código de ejemplo avanzado
```

## Ejemplo 3: Integración

```python
# Ejemplo de integración con otros skills
```
"""
        (path / 'examples' / 'README.md').write_text(content)
    
    def list_skills(self, skill_type: Optional[str] = None) -> List[dict]:
        """Lista todos los skills disponibles"""
        skills = []
        
        search_types = [skill_type] if skill_type else SKILL_TYPES
        
        for stype in search_types:
            type_dir = self.skills_dir / stype
            if not type_dir.exists():
                continue
                
            for skill_dir in type_dir.iterdir():
                if not skill_dir.is_dir():
                    continue
                
                metadata_file = skill_dir / 'metadata.json'
                if metadata_file.exists():
                    with open(metadata_file) as f:
                        metadata = json.load(f)
                        metadata['path'] = str(skill_dir.relative_to(self.base_path))
                        skills.append(metadata)
        
        return skills
    
    def validate_skill(self, skill_path: Path) -> dict:
        """Valida que un skill tenga la estructura correcta"""
        required_files = ['SKILL.md', 'metadata.json']
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        for req_file in required_files:
            if not (skill_path / req_file).exists():
                results['valid'] = False
                results['errors'].append(f"Falta archivo requerido: {req_file}")
        
        # Validar metadata.json
        metadata_file = skill_path / 'metadata.json'
        if metadata_file.exists():
            try:
                with open(metadata_file) as f:
                    metadata = json.load(f)
                    required_keys = ['name', 'type', 'version']
                    for key in required_keys:
                        if key not in metadata:
                            results['warnings'].append(f"Metadata falta clave: {key}")
            except json.JSONDecodeError:
                results['valid'] = False
                results['errors'].append("metadata.json no es JSON válido")
        
        return results


@click.group()
def cli():
    """Skill Manager - Gestión de skills"""
    pass


@cli.command()
@click.option('--name', '-n', required=True, help='Nombre del skill')
@click.option('--type', '-t', 'skill_type', type=click.Choice(SKILL_TYPES), 
              required=True, help='Tipo de skill')
@click.option('--description', '-d', default='', help='Descripción del skill')
def create(name: str, skill_type: str, description: str):
    """Crear un nuevo skill"""
    manager = SkillManager()
    try:
        skill_path = manager.create_skill(name, skill_type, description)
        click.echo(f"✅ Skill creado exitosamente en: {skill_path}")
        click.echo(f"\nPróximos pasos:")
        click.echo(f"1. Editar {skill_path}/SKILL.md con la documentación")
        click.echo(f"2. Implementar la funcionalidad")
        click.echo(f"3. Agregar tests en tests/")
        click.echo(f"4. Agregar ejemplos en examples/")
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)


@cli.command()
@click.option('--category', '-c', default='all', help='Categoría de skills a listar')
@click.option('--format', '-f', type=click.Choice(['table', 'json']), default='table')
def list(category: str, format: str):
    """Listar skills disponibles"""
    manager = SkillManager()
    skill_type = None if category == 'all' else category
    
    skills = manager.list_skills(skill_type)
    
    if format == 'json':
        click.echo(json.dumps(skills, indent=2))
    else:
        if not skills:
            click.echo("No se encontraron skills")
            return
            
        click.echo(f"\n{'Nombre':<30} {'Tipo':<15} {'Versión':<10} {'Status':<10}")
        click.echo("-" * 70)
        for skill in skills:
            click.echo(f"{skill.get('name', 'N/A'):<30} "
                      f"{skill.get('type', 'N/A'):<15} "
                      f"{skill.get('version', 'N/A'):<10} "
                      f"{skill.get('status', 'N/A'):<10}")


@cli.command()
@click.argument('skill_path', type=click.Path(exists=True))
def validate(skill_path: str):
    """Validar un skill"""
    manager = SkillManager()
    results = manager.validate_skill(Path(skill_path))
    
    if results['valid']:
        click.echo("✅ Skill válido")
    else:
        click.echo("❌ Skill inválido")
    
    if results['errors']:
        click.echo("\nErrores:")
        for error in results['errors']:
            click.echo(f"  - {error}")
    
    if results['warnings']:
        click.echo("\nAdvertencias:")
        for warning in results['warnings']:
            click.echo(f"  - {warning}")


if __name__ == '__main__':
    cli()
