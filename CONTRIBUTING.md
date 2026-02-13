# Contributing Guide 🤝

Thank you for your interest in contributing! This document will guide you through the process.

## Code of Conduct

- Be respectful and constructive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy toward other members

## How Can I Contribute?

### Report Bugs 🐛

Before creating an issue, check that a similar one doesn't exist. Include:

- **Clear description** of the problem
- **Steps to reproduce**
- **Expected behavior** vs actual
- **Screenshots** if applicable
- **Version** of Python and OS

**Template:**
```markdown
## Description
[Bug description]

## Steps to reproduce
1. ...
2. ...
3. ...

## Expected behavior
[What should happen]

## Actual behavior
[What actually happens]

## Environment
- OS: [e.g., Ubuntu 22.04]
- Python: [e.g., 3.10.5]
- Repo version: [commit hash]
```

### Suggest Features ✨

Open an issue with the `enhancement` label:

- **Problem it solves**
- **Proposed solution**
- **Alternatives considered**
- **Expected impact**

### Contribute Code 💻

#### 1. Fork and Clone

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR-USERNAME/skills-repository.git
cd skills-repository
git remote add upstream https://github.com/ORIGINAL-OWNER/skills-repository.git
```

#### 2. Create Branch

```bash
git checkout -b feature/descriptive-name
# or
git checkout -b fix/description-of-fix
```

**Naming convention:**
- `feature/` - New functionality
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Refactoring
- `test/` - Add tests
- `chore/` - Maintenance tasks

#### 3. Make Changes

##### Add a New Skill

```bash
# Use the manager
python scripts/skill-manager.py create \
  --name "my-skill" \
  --type [ai-prompts|code|hybrid] \
  --description "Brief description"

# Edit generated files
# Follow template structure
```

#### 4. Tests

**ALL changes must include tests.**

```python
# tests/test_my_functionality.py
import pytest
from my_module import my_function

class TestMyFunction:
    def test_basic_case(self):
        """Test basic case"""
        result = my_function("input")
        assert result == "expected"
    
    def test_error_case(self):
        """Test error handling"""
        with pytest.raises(ValueError):
            my_function("")
```

**Run tests:**

```bash
# All
pytest

# Specific
pytest tests/test_my_functionality.py

# With coverage
pytest --cov=. --cov-report=html
```

**Minimum 80% coverage** for new code.

#### 5. Validation

Before committing, run:

```bash
# Formatting
black .

# Linting
flake8 . --max-line-length=100

# Type checking
mypy scripts/ --ignore-missing-imports

# Tests
pytest

# Validate skills
python scripts/skill-manager.py validate skills/category/my-skill/
```

#### 6. Commit

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git add .
git commit -m "type(scope): brief message"
```

**Types:**
- `feat`: New functionality
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Refactoring
- `test`: Add tests
- `chore`: Maintenance

**Examples:**
```bash
git commit -m "feat(skills): add text-summarizer skill"
git commit -m "fix(compound-engine): fix bug in SkillChain"
git commit -m "docs(readme): update installation instructions"
```

#### 7. Push and Pull Request

```bash
# Push to your fork
git push origin feature/my-feature

# Create PR on GitHub
```

## Code Standards

### Python

```python
# ✅ GOOD
def calculate_total(items: List[dict]) -> float:
    """Calculate total of items."""
    return sum(item['price'] for item in items)

# ❌ BAD
def calc(x):
    return sum([i['price'] for i in x])
```

### Documentation

```markdown
# ✅ GOOD - Clear, examples, complete
## Usage

The skill processes long texts:

```python
from skills.text import process
result = process("long text...")
```

Returns a dict with:
- summary: summary
- keywords: list of keywords

# ❌ BAD - Vague, no examples
## Usage
Processes texts.
```

## Code Review

When reviewing PRs:

**Look for:**
- ✅ Clear and maintainable code
- ✅ Adequate tests
- ✅ Updated documentation
- ✅ No duplicate code
- ✅ Appropriate error handling

**Comment:**
- Constructively
- With specific suggestions
- Acknowledge good things too

## Merge Process

1. **Reviewer approves** the PR
2. **CI/CD passes** (all checks green)
3. **Update branch** if necessary
4. **Squash and merge** (keeps clean history)

## FAQ

**Q: Can I work on multiple features simultaneously?**
A: Yes, but use separate branches for each.

**Q: What do I do if my PR has conflicts?**
A: Update your branch with main:
```bash
git fetch upstream
git rebase upstream/main
# Resolve conflicts
git push --force-with-lease origin your-branch
```

**Q: How long does review take?**
A: We aim for 48 hours, but it may vary by complexity.

## Resources

- [PEP 8](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [pytest docs](https://docs.pytest.org/)

---

**Questions?** Open an issue with the `question` label or ask in [Discussions](https://github.com/your-username/skills-repository/discussions).
