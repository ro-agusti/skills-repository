"""
Pytest configuration for the skills repository
"""
import pytest
from pathlib import Path
import sys

# Add the root directory to the sys.path
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))


@pytest.fixture
def base_dir():
    """Fixture that returns the repository's base directory"""
    return ROOT_DIR


@pytest.fixture
def skills_dir(base_dir):
    """Fixture that returns the skills directory"""
    return base_dir / 'skills'


@pytest.fixture
def sample_skill_data():
    """Fixture containing sample data for skills"""
    return {
        'name': 'test-skill',
        'type': 'code',
        'version': '1.0.0',
        'description': 'Test skill',
        'author': 'Test Author',
        'tags': ['test', 'example'],
        'status': 'active'
    }


@pytest.fixture
def temp_skill_dir(tmp_path):
    """Fixture that creates a temporary directory for skills"""
    skill_dir = tmp_path / 'test-skill'
    skill_dir.mkdir()
    (skill_dir / 'tests').mkdir()
    (skill_dir / 'examples').mkdir()
    return skill_dir


def pytest_configure(config):
    """Pytest configuration and custom marker registration"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )