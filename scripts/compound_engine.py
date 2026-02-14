#!/usr/bin/env python3
"""
Compound Engine - System for combining multiple skills into complex workflows
"""
import yaml
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import importlib.util


@dataclass
class SkillNode:
    """Represents a skill in a chain"""
    name: str
    path: Path
    skill_type: str
    config: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.config is None:
            self.config = {}


class SkillExecutor:
    """Individual skill executor"""
    
    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.metadata = self._load_metadata()
        
    def _load_metadata(self) -> dict:
        """Load skill metadata"""
        metadata_file = self.skill_path / 'metadata.json'
        if metadata_file.exists():
            with open(metadata_file) as f:
                return json.load(f)
        return {}
    
    def execute(self, input_data: Any, **kwargs) -> Any:
        """Execute the skill"""
        skill_type = self.metadata.get('type', 'code')
        
        if skill_type == 'ai-prompts':
            return self._execute_prompt(input_data, **kwargs)
        elif skill_type in ['code', 'hybrid']:
            return self._execute_code(input_data, **kwargs)
        else:
            raise ValueError(f"Unsupported skill type: {skill_type}")
    
    def _execute_prompt(self, input_data: Any, **kwargs) -> str:
        """Execute an AI prompt skill"""
        prompt_file = self.skill_path / 'prompt.txt'
        
        if not prompt_file.exists():
            raise FileNotFoundError(f"prompt.txt not found in {self.skill_path}")
        
        prompt_template = prompt_file.read_text()
        
        # Replace variables
        variables = {'input': input_data, **kwargs}
        prompt = prompt_template
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        # Here you would integrate with Anthropic API or similar
        # For now, return processed prompt
        return {
            'prompt': prompt,
            'input': input_data,
            'metadata': self.metadata
        }
    
    def _execute_code(self, input_data: Any, **kwargs) -> Any:
        """Execute a code skill"""
        # Find main Python file
        python_files = list(self.skill_path.glob('*.py'))
        
        if not python_files:
            raise FileNotFoundError(f"No .py file found in {self.skill_path}")
        
        module_file = python_files[0]
        
        # Load module dynamically
        spec = importlib.util.spec_from_file_location("skill_module", module_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Find execute function
        if hasattr(module, 'execute'):
            return module.execute(input=input_data, **kwargs)
        else:
            raise AttributeError("Module doesn't have an 'execute' function")


class SkillChain:
    """Chain of skills executed sequentially"""
    
    def __init__(self, skill_paths: List[str], base_dir: Path = None):
        self.base_dir = base_dir or Path(__file__).parent.parent
        self.skills = []
        
        for path in skill_paths:
            skill_path = self.base_dir / path
            if not skill_path.exists():
                raise FileNotFoundError(f"Skill not found: {skill_path}")
            
            executor = SkillExecutor(skill_path)
            self.skills.append(executor)
    
    def execute(self, initial_input: Any, **kwargs) -> Any:
        """Execute complete skill chain"""
        current_data = initial_input
        results = []
        
        for i, skill in enumerate(self.skills):
            print(f"Executing skill {i+1}/{len(self.skills)}: {skill.metadata.get('name')}")
            
            try:
                result = skill.execute(current_data, **kwargs)
                results.append({
                    'skill': skill.metadata.get('name'),
                    'result': result,
                    'status': 'success'
                })
                current_data = result
            except Exception as e:
                results.append({
                    'skill': skill.metadata.get('name'),
                    'error': str(e),
                    'status': 'error'
                })
                raise
        
        return {
            'final_output': current_data,
            'chain_results': results
        }


class SkillPipeline:
    """Complex pipeline with branching, conditionals, and parallel execution"""
    
    def __init__(self, config_file: Path):
        self.config = self._load_config(config_file)
        self.base_dir = Path(__file__).parent.parent
        
    def _load_config(self, config_file: Path) -> dict:
        """Load pipeline configuration from YAML"""
        with open(config_file) as f:
            return yaml.safe_load(f)
    
    def execute(self, input_data: Any) -> Any:
        """Execute complete pipeline"""
        steps = self.config.get('steps', [])
        current_data = input_data
        context = {'input': input_data}
        
        for step in steps:
            step_type = step.get('type', 'execute')
            
            if step_type == 'execute':
                current_data = self._execute_step(step, current_data, context)
            elif step_type == 'conditional':
                current_data = self._execute_conditional(step, current_data, context)
            elif step_type == 'parallel':
                current_data = self._execute_parallel(step, current_data, context)
            
            # Save to context
            if 'output_var' in step:
                context[step['output_var']] = current_data
        
        return current_data
    
    def _execute_step(self, step: dict, data: Any, context: dict) -> Any:
        """Execute individual step"""
        skill_path = self.base_dir / step['skill']
        executor = SkillExecutor(skill_path)
        
        # Prepare kwargs from context
        kwargs = {}
        if 'params' in step:
            for key, value in step['params'].items():
                # If value is a context reference
                if isinstance(value, str) and value.startswith('$'):
                    var_name = value[1:]
                    kwargs[key] = context.get(var_name, value)
                else:
                    kwargs[key] = value
        
        return executor.execute(data, **kwargs)
    
    def _execute_conditional(self, step: dict, data: Any, context: dict) -> Any:
        """Execute conditional block"""
        # Simplified implementation
        if 'then' in step:
            return self._execute_step(step['then'], data, context)
        return data
    
    def _execute_parallel(self, step: dict, data: Any, context: dict) -> List[Any]:
        """Execute multiple skills in parallel (simulated)"""
        results = []
        
        for parallel_step in step.get('steps', []):
            result = self._execute_step(parallel_step, data, context)
            results.append(result)
        
        # Combine results according to strategy
        combine_strategy = step.get('combine', 'list')
        
        if combine_strategy == 'list':
            return results
        elif combine_strategy == 'merge':
            if all(isinstance(r, dict) for r in results):
                merged = {}
                for r in results:
                    merged.update(r)
                return merged
        
        return results


if __name__ == '__main__':
    # Usage example
    print("Compound Engine - Skill composition system")
    print("\nUsage example:")
    print("""
    from compound_engine import SkillChain
    
    # Create a chain
    chain = SkillChain([
        'skills/ai-prompts/analyzer',
        'skills/code/processor',
        'skills/hybrid/formatter'
    ])
    
    result = chain.execute("input data")
    """)