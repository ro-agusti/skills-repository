#!/usr/bin/env python3
"""
Skill Manager - Main tool for managing skills
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
    """Repository skill manager"""
    
    def __init__(self, base_path: Path = BASE_DIR):
        self.base_path = base_path
        self.skills_dir = base_path / 'skills'
        
    def create_skill(self, name: str, skill_type: str, description: str = "") -> Path:
        """Creates a new skill from template"""
        if skill_type not in SKILL_TYPES:
            raise ValueError(f"Type must be one of: {SKILL_TYPES}")
        
        skill_path = self.skills_dir / skill_type / name
        
        if skill_path.exists():
            raise FileExistsError(f"Skill already exists: {skill_path}")
        
        # Create structure
        skill_path.mkdir(parents=True, exist_ok=True)
        (skill_path / 'examples').mkdir(exist_ok=True)
        (skill_path / 'tests').mkdir(exist_ok=True)
        
        # Create base files
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
        """Creates the SKILL.md file"""
        content = f"""# {name}

## Description
{description or 'Skill description'}

## Usage

```python
# Usage example
```

## Parameters

- `param1`: Parameter description

## Examples

See `examples/` folder for detailed use cases.

## Tests

```bash
pytest tests/test_{name.replace('-', '_')}.py
```

## Notes

- Note 1
- Note 2

## Changelog

### v1.0.0 - {datetime.now().strftime('%Y-%m-%d')}
- Initial version
"""
        (path / 'SKILL.md').write_text(content)
    
    def _create_metadata(self, path: Path, name: str, skill_type: str, description: str):
        """Creates the metadata.json file"""
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
        """Creates prompt file for AI skills"""
        content = f"""# Prompt for {name}

## System Prompt
[Your system prompt here]

## User Prompt Template
[Template for user prompt]

## Variables
- {{variable1}}: description
- {{variable2}}: description
"""
        (path / 'prompt.txt').write_text(content)
    
    def _create_python_file(self, path: Path, name: str):
        """Creates Python file for code/hybrid skills"""
        module_name = name.replace('-', '_')
        content = f'''"""
{name} - Skill Module
"""

def execute(**kwargs):
    """
    Main skill function
    
    Args:
        **kwargs: Skill parameters
        
    Returns:
        Execution result
    """
    # Implementation
    pass


class {module_name.title().replace('_', '')}:
    """Main skill class"""
    
    def __init__(self):
        pass
    
    def run(self, *args, **kwargs):
        """Executes the skill"""
        return execute(**kwargs)


if __name__ == "__main__":
    # Usage example
    result = execute()
    print(result)
'''
        (path / f'{module_name}.py').write_text(content)
    
    def _create_test_file(self, path: Path, name: str, skill_type: str):
        """Creates test file"""
        module_name = name.replace('-', '_')
        content = f'''"""
Tests for {name}
"""
import pytest
from pathlib import Path

# Import the skill
{"# from " + module_name + " import execute" if skill_type != "ai-prompts" else ""}

def test_basic_functionality():
    """Test basic functionality"""
    assert True  # Replace with actual test


def test_with_parameters():
    """Test with parameters"""
    pass


@pytest.mark.parametrize("input_data,expected", [
    ("input1", "output1"),
    ("input2", "output2"),
])
def test_multiple_cases(input_data, expected):
    """Test with multiple cases"""
    pass
'''
        (path / 'tests' / f'test_{module_name}.py').write_text(content)
    
    def _create_examples_file(self, path: Path, name: str):
        """Creates examples file"""
        content = f"""# Usage Examples - {name}

## Example 1: Basic Usage

```python
# Example code
```

### Expected Result
```
Expected output
```

## Example 2: Advanced Usage

```python
# Advanced example code
```

## Example 3: Integration

```python
# Integration example with other skills
```
"""
        (path / 'examples' / 'README.md').write_text(content)
    
    def list_skills(self, skill_type: Optional[str] = None) -> List[dict]:
        """Lists all available skills"""
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
        """Validates that a skill has the correct structure"""
        required_files = ['SKILL.md', 'metadata.json']
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        for req_file in required_files:
            if not (skill_path / req_file).exists():
                results['valid'] = False
                results['errors'].append(f"Missing required file: {req_file}")
        
        # Validate metadata.json
        metadata_file = skill_path / 'metadata.json'
        if metadata_file.exists():
            try:
                with open(metadata_file) as f:
                    metadata = json.load(f)
                    required_keys = ['name', 'type', 'version']
                    for key in required_keys:
                        if key not in metadata:
                            results['warnings'].append(f"Metadata missing key: {key}")
            except json.JSONDecodeError:
                results['valid'] = False
                results['errors'].append("metadata.json is not valid JSON")
        
        return results


@click.group()
def cli():
    """Skill Manager - Skill management"""
    pass


@cli.command()
@click.option('--name', '-n', required=True, help='Skill name')
@click.option('--type', '-t', 'skill_type', type=click.Choice(SKILL_TYPES), 
              required=True, help='Skill type')
@click.option('--description', '-d', default='', help='Skill description')
def create(name: str, skill_type: str, description: str):
    """Create a new skill"""
    manager = SkillManager()
    try:
        skill_path = manager.create_skill(name, skill_type, description)
        click.echo(f"✅ Skill created successfully at: {skill_path}")
        click.echo(f"\nNext steps:")
        click.echo(f"1. Edit {skill_path}/SKILL.md with documentation")
        click.echo(f"2. Implement functionality")
        click.echo(f"3. Add tests in tests/")
        click.echo(f"4. Add examples in examples/")
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)


@cli.command()
@click.option('--category', '-c', default='all', help='Category of skills to list')
@click.option('--format', '-f', type=click.Choice(['table', 'json']), default='table')
def list(category: str, format: str):
    """List available skills"""
    manager = SkillManager()
    skill_type = None if category == 'all' else category
    
    skills = manager.list_skills(skill_type)
    
    if format == 'json':
        click.echo(json.dumps(skills, indent=2))
    else:
        if not skills:
            click.echo("No skills found")
            return
            
        click.echo(f"\n{'Name':<30} {'Type':<15} {'Version':<10} {'Status':<10}")
        click.echo("-" * 70)
        for skill in skills:
            click.echo(f"{skill.get('name', 'N/A'):<30} "
                      f"{skill.get('type', 'N/A'):<15} "
                      f"{skill.get('version', 'N/A'):<10} "
                      f"{skill.get('status', 'N/A'):<10}")


@cli.command()
@click.argument('skill_path', type=click.Path(exists=True))
def validate(skill_path: str):
    """Validate a skill"""
    manager = SkillManager()
    results = manager.validate_skill(Path(skill_path))
    
    if results['valid']:
        click.echo("✅ Valid skill")
    else:
        click.echo("❌ Invalid skill")
    
    if results['errors']:
        click.echo("\nErrors:")
        for error in results['errors']:
            click.echo(f"  - {error}")
    
    if results['warnings']:
        click.echo("\nWarnings:")
        for warning in results['warnings']:
            click.echo(f"  - {warning}")


if __name__ == '__main__':
    cli()