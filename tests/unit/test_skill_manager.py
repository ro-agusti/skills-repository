"""
Tests for skill-manager
"""
import pytest
import json
from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'scripts'))

from skill_manager import SkillManager


class TestSkillManager:
    """Tests for the SkillManager class"""
    
    def test_create_skill_ai_prompts(self, tmp_path):
        """Test AI skill creation"""
        manager = SkillManager(base_path=tmp_path)
        
        skill_path = manager.create_skill(
            name="test-ai-skill",
            skill_type="ai-prompts",
            description="Test AI skill"
        )
        
        assert skill_path.exists()
        assert (skill_path / 'SKILL.md').exists()
        assert (skill_path / 'metadata.json').exists()
        assert (skill_path / 'prompt.txt').exists()
        assert (skill_path / 'examples').exists()
        assert (skill_path / 'tests').exists()
    
    def test_create_skill_code(self, tmp_path):
        """Test code skill creation"""
        manager = SkillManager(base_path=tmp_path)
        
        skill_path = manager.create_skill(
            name="test-code-skill",
            skill_type="code",
            description="Test code skill"
        )
        
        assert skill_path.exists()
        python_files = list(skill_path.glob('*.py'))
        assert len(python_files) > 0
    
    def test_create_duplicate_skill_fails(self, tmp_path):
        """Test that duplicate skill creation fails"""
        manager = SkillManager(base_path=tmp_path)
        
        manager.create_skill("duplicate", "code")
        
        with pytest.raises(FileExistsError):
            manager.create_skill("duplicate", "code")
    
    def test_list_skills_empty(self, tmp_path):
        """Test listing skills when none exist"""
        manager = SkillManager(base_path=tmp_path)
        skills = manager.list_skills()
        
        assert skills == []
    
    def test_list_skills_with_content(self, tmp_path):
        """Test listing skills with content"""
        manager = SkillManager(base_path=tmp_path)
        
        # Create several skills
        manager.create_skill("skill1", "ai-prompts")
        manager.create_skill("skill2", "code")
        
        skills = manager.list_skills()
        
        assert len(skills) == 2
        assert any(s['name'] == 'skill1' for s in skills)
        assert any(s['name'] == 'skill2' for s in skills)
    
    def test_validate_skill_valid(self, tmp_path):
        """Test validation of a valid skill"""
        manager = SkillManager(base_path=tmp_path)
        skill_path = manager.create_skill("valid-skill", "code")
        
        results = manager.validate_skill(skill_path)
        
        assert results['valid'] is True
        assert len(results['errors']) == 0
    
    def test_validate_skill_missing_files(self, tmp_path):
        """Test validation of a skill with missing files"""
        manager = SkillManager(base_path=tmp_path)
        
        # Create directory but without required files
        skill_path = tmp_path / 'skills' / 'code' / 'incomplete'
        skill_path.mkdir(parents=True)
        
        results = manager.validate_skill(skill_path)
        
        assert results['valid'] is False
        assert len(results['errors']) > 0
    
    def test_metadata_has_correct_structure(self, tmp_path):
        """Test that metadata has the correct structure"""
        manager = SkillManager(base_path=tmp_path)
        skill_path = manager.create_skill("metadata-test", "hybrid")
        
        with open(skill_path / 'metadata.json') as f:
            metadata = json.load(f)
        
        required_keys = ['name', 'type', 'version', 'description']
        for key in required_keys:
            assert key in metadata
        
        assert metadata['name'] == 'metadata-test'
        assert metadata['type'] == 'hybrid'


@pytest.mark.parametrize("skill_type", ['ai-prompts', 'code', 'hybrid'])
def test_create_all_skill_types(tmp_path, skill_type):
    """Parameterized test for all skill types"""
    manager = SkillManager(base_path=tmp_path)
    
    skill_path = manager.create_skill(
        name=f"test-{skill_type}",
        skill_type=skill_type
    )
    
    assert skill_path.exists()
    assert (skill_path / 'metadata.json').exists()