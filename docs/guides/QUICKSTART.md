# Quick Start Guide 🚀

This guide will help you start using the skills repository in less than 5 minutes.

## Prerequisites

- Python 3.8 or higher
- Git
- GitHub account

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/skills-repository.git
cd skills-repository
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Your First Skill

### Create an AI Skill

```bash
python scripts/skill-manager.py create \
  --name "my-first-skill" \
  --type ai-prompts \
  --description "My first analysis skill"
```

This creates:
```
skills/ai-prompts/my-first-skill/
├── SKILL.md          # Documentation
├── prompt.txt        # Prompt template
├── metadata.json     # Metadata
├── examples/         # Examples
└── tests/           # Tests
```

### Edit the Skill

1. Open `skills/ai-prompts/my-first-skill/prompt.txt`
2. Add your prompt:

```
# System Prompt
You are an expert data analysis assistant.

# User Prompt
Analyze the following data: {input}

Provide:
1. Summary
2. Key insights
3. Recommendations
```

3. Document in `SKILL.md`

### Test the Skill

```python
from scripts.compound_engine import SkillExecutor

executor = SkillExecutor('skills/ai-prompts/my-first-skill')
result = executor.execute("test data")
print(result)
```

## Compound Engineering

### Create a Simple Chain

```python
from scripts.compound_engine import SkillChain

# Create chain of 3 skills
chain = SkillChain([
    'skills/ai-prompts/my-first-skill',
    'skills/code/processor',
    'skills/hybrid/formatter'
])

# Execute
result = chain.execute("initial input")
print(result)
```

### Create a Complex Pipeline

1. Create configuration in `compound/configs/my-pipeline.yaml`:

```yaml
name: "My Pipeline"
steps:
  - name: "Step 1"
    type: execute
    skill: "skills/ai-prompts/my-first-skill"
    output_var: "result1"
  
  - name: "Step 2"
    type: execute
    skill: "skills/code/processor"
    params:
      input: "$result1"
```

2. Execute:

```python
from scripts.compound_engine import SkillPipeline

pipeline = SkillPipeline('compound/configs/my-pipeline.yaml')
result = pipeline.execute("data")
```

## Useful Commands

### List Skills

```bash
# List all
python scripts/skill-manager.py list

# By category
python scripts/skill-manager.py list --category ai-prompts

# As JSON
python scripts/skill-manager.py list --format json
```

### Validate Skills

```bash
python scripts/skill-manager.py validate skills/ai-prompts/my-first-skill/
```

### Run Tests

```bash
# All tests
pytest

# Specific tests
pytest tests/unit/

# With coverage
pytest --cov=scripts --cov=skills
```

## Development Workflow

### 1. Create Branch

```bash
git checkout -b feature/new-skill
```

### 2. Develop Skill

```bash
python scripts/skill-manager.py create --name "new-skill" --type code
# Edit files...
```

### 3. Write Tests

```python
# In tests/test_new_skill.py
def test_basic():
    from skills.code.new_skill import execute
    result = execute("test")
    assert result is not None
```

### 4. Validate

```bash
# Format
black .

# Linting
flake8 .

# Tests
pytest

# Validate skill
python scripts/skill-manager.py validate skills/code/new-skill/
```

### 5. Commit and Push

```bash
git add .
git commit -m "feat: add new-skill"
git push origin feature/new-skill
```

### 6. Create Pull Request

Go to GitHub and create a PR from your branch.

## Next Steps

1. **Read complete documentation** in `docs/`
2. **Explore existing skills** as examples
3. **Contribute** following guides in CONTRIBUTING.md
4. **Join the community** in Discussions

## Additional Resources

- [Complete Documentation](../README.md)
- [Skill Templates](../skills/templates/)
- [Examples](../docs/examples/)
- [FAQ](../docs/FAQ.md)

## Problems?

- Check [Troubleshooting](../docs/TROUBLESHOOTING.md)
- Open an [Issue](https://github.com/your-username/skills-repository/issues)
- Ask in [Discussions](https://github.com/your-username/skills-repository/discussions)

---

**Happy coding! 🎉**
