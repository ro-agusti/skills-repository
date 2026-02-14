"""
Tests for sentiment-analyzer skill
"""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'scripts'))
from compound_engine import SkillExecutor


class TestSentimentAnalyzer:
    """Tests for sentiment analyzer skill"""
    
    def setup_method(self):
        """Setup before each test"""
        self.executor = SkillExecutor(
            Path(__file__).parent.parent
        )
    
    def test_prompt_contains_input(self):
        """Test that input is included in generated prompt"""
        text = "This is a test"
        result = self.executor.execute(text)
        
        assert text in result['prompt']
        assert 'sentiment' in result['prompt'].lower()
    
    def test_variables_replaced(self):
        """Test that {input} variable is replaced"""
        text = "Another test"
        result = self.executor.execute(text)
        
        assert '{input}' not in result['prompt']
        assert text in result['prompt']
    
    def test_multiple_executions(self):
        """Test executing multiple times"""
        texts = ["test 1", "test 2", "test 3"]
        
        for text in texts:
            result = self.executor.execute(text)
            assert text in result['prompt']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])