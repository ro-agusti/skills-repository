# Skills Repository 🚀

Centralized repository for managing AI/LLM skills, programming scripts, and compound engineering.

## 📋 Table of Contents

- [Repository Structure](#repository-structure)
- [Skill Types](#skill-types)
- [Installation and Setup](#installation-and-setup)
- [Quick Start](#quick-start)
- [Testing and Evaluation](#testing-and-evaluation)
- [Compound Engineering](#compound-engineering)
- [Contributing](#contributing)

## 🗂️ Repository Structure

```
skills-repository/
├── skills/                    # Skills organized by category
│   ├── ai-prompts/           # LLM skills (prompts, instructions)
│   ├── code/                 # Code skills (functions, modules)
│   ├── hybrid/               # Skills combining both
│   └── templates/            # Templates for creating new skills
├── scripts/                   # Utility scripts
│   ├── skill-manager.py      # Main skill manager
│   ├── validator.py          # Format validator
│   └── compound-engine.py    # Compound engineering engine
├── tests/                     # Tests and evaluations
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── benchmarks/           # Performance benchmarks
├── docs/                      # Additional documentation
│   ├── guides/               # Usage guides
│   ├── examples/             # Practical examples
│   └── api/                  # API documentation
├── compound/                  # Compound engineering configurations
│   ├── chains/               # Skill chains
│   ├── pipelines/            # Complex pipelines
│   └── configs/              # Configurations
└── .github/                   # GitHub configuration
    └── workflows/            # GitHub Actions
```

## 🎯 Skill Types

### AI/LLM Skills
Skills based on prompts and instructions for language models:
- Optimized prompts
- System instructions
- Reasoning chains
- Few-shot examples

### Code Skills
Reusable modules and functions:
- Python utilities
- Automation scripts
- Custom libraries
- Helpers and wrappers

### Hybrid Skills
Combination of AI and code:
- Agents with tooling
- Processing pipelines
- Automated workflows

## 🚀 Installation and Setup

### Requirements
```bash
- Python 3.8+
- Git
- pip
```

### Initial Setup
```bash
# Clone the repository
git clone https://github.com/your-username/skills-repository.git
cd skills-repository

# Install dependencies
pip install -r requirements.txt

# Configure
python scripts/setup.py
```

## 💡 Quick Start

### Create a New Skill
```bash
python scripts/skill-manager.py create --name "my-skill" --type ai-prompts
```

### List Available Skills
```bash
python scripts/skill-manager.py list --category all
```

### Validate a Skill
```bash
python scripts/skill-manager.py validate skills/ai-prompts/my-skill/
```

### Run Tests
```bash
pytest tests/
```

## 🧪 Testing and Evaluation

### Test Structure
Each skill must include:
- `test_<skill-name>.py`: Unit tests
- `benchmark_<skill-name>.py`: Performance evaluation
- `examples.md`: Documented use cases

### Run Evaluations
```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# Benchmarks
python tests/benchmarks/run_all.py
```

## 🔗 Compound Engineering

### What is Compound Engineering?
System for combining multiple skills into complex workflows and creating more powerful skills from basic ones.

### Create a Chain
```python
from scripts.compound_engine import SkillChain

chain = SkillChain([
    'skills/ai-prompts/analyzer',
    'skills/code/processor',
    'skills/hybrid/formatter'
])

result = chain.execute(input_data)
```

### Configure a Pipeline
See `compound/configs/example-pipeline.yaml` for examples.

## 🤝 Contributing

### Adding a New Skill

1. Create from template:
```bash
python scripts/skill-manager.py create --name "new-skill" --type [ai-prompts|code|hybrid]
```

2. Develop the skill following the structure:
```
skills/category/skill-name/
├── SKILL.md              # Main documentation
├── skill.py or prompt.txt # Implementation
├── examples/             # Usage examples
├── tests/               # Skill tests
└── metadata.json        # Metadata
```

3. Validate:
```bash
python scripts/skill-manager.py validate skills/category/skill-name/
```

4. Create PR with clear description

### Code Standards
- Python: PEP 8
- Documentation: Markdown with examples
- Tests: >80% coverage
- Commits: Conventional Commits

## 📊 Metrics and Statistics

```bash
# View repository statistics
python scripts/stats.py
```

## 🔖 Versioning

We use [SemVer](http://semver.org/) for versioning. See [tags](https://github.com/your-username/skills-repository/tags) for available versions.

## 📝 License

This project is under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Contributor community
- Claude ecosystem base skills
- Anthropic documentation

---

**Need help?** Open an [issue](https://github.com/your-username/skills-repository/issues) or check the [documentation](docs/).
