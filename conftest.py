"""
Configuración de pytest para el repositorio de skills
"""
import pytest
from pathlib import Path
import sys

# Agregar el directorio raíz al path
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))


@pytest.fixture
def base_dir():
    """Fixture que retorna el directorio base del repositorio"""
    return ROOT_DIR


@pytest.fixture
def skills_dir(base_dir):
    """Fixture que retorna el directorio de skills"""
    return base_dir / 'skills'


@pytest.fixture
def sample_skill_data():
    """Fixture con datos de ejemplo para skills"""
    return {
        'name': 'test-skill',
        'type': 'code',
        'version': '1.0.0',
        'description': 'Skill de prueba',
        'author': 'Test Author',
        'tags': ['test', 'example'],
        'status': 'active'
    }


@pytest.fixture
def temp_skill_dir(tmp_path):
    """Fixture que crea un directorio temporal para skills"""
    skill_dir = tmp_path / 'test-skill'
    skill_dir.mkdir()
    (skill_dir / 'tests').mkdir()
    (skill_dir / 'examples').mkdir()
    return skill_dir


def pytest_configure(config):
    """Configuración de pytest"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
