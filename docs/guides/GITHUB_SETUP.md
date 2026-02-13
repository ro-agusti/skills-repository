# Step-by-Step Guide: Upload to GitHub 📤

This guide will take you from local setup to having your repository on GitHub.

## Part 1: Local Preparation

### 1. Navigate to your working directory

```bash
cd /home/claude/skills-repository
```

### 2. Initialize Git (if not already initialized)

```bash
git init
```

### 3. Configure your Git information

```bash
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### 4. Review created files

```bash
# View structure
tree -L 2

# Or simply list
ls -la
```

### 5. Add all files

```bash
git add .
```

### 6. Verify what will be committed

```bash
git status
```

### 7. Create the first commit

```bash
git commit -m "feat: initial commit - base repository structure"
```

## Part 2: Create Repository on GitHub

### Option A: Using GitHub web interface

1. **Go to GitHub**: https://github.com
2. **Sign in** to your account
3. **Click the "+" button** (top right) → **"New repository"**
4. **Configure the repository**:
   - **Repository name**: `skills-repository` (or your preferred name)
   - **Description**: "Centralized repository for managing AI/LLM skills, scripts, and compound engineering"
   - **Visibility**: 
     - ✅ **Public** (if you want to share it)
     - ✅ **Private** (if it's just for you)
   - ⚠️ **DO NOT check** "Initialize with README" (we already have one)
   - ⚠️ **DO NOT add** .gitignore (we already have one)
   - ⚠️ **DO NOT add** License (we already have one)
5. **Click "Create repository"**

### Option B: Using GitHub CLI (if you have gh installed)

```bash
# Install gh if you don't have it
# On Ubuntu/Debian:
# curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
# echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
# sudo apt update
# sudo apt install gh

# Authenticate
gh auth login

# Create repository
gh repo create skills-repository --public --source=. --remote=origin
# Or for private:
# gh repo create skills-repository --private --source=. --remote=origin
```

## Part 3: Connect Local with GitHub

### If you used the web interface (Option A):

GitHub will show you commands. Copy and execute:

```bash
# Add remote
git remote add origin https://github.com/YOUR-USERNAME/skills-repository.git

# Or if you prefer SSH:
# git remote add origin git@github.com:YOUR-USERNAME/skills-repository.git
```

### If you used GitHub CLI (Option B):

The remote is already configured. You can verify:

```bash
git remote -v
```

## Part 4: Push Code

### 1. Rename branch to 'main' (if it's 'master')

```bash
git branch -M main
```

### 2. Initial push

```bash
git push -u origin main
```

If using HTTPS and it asks for credentials:
- **Username**: your GitHub username
- **Password**: use a **Personal Access Token** (PAT), not your password
  - Create one at: https://github.com/settings/tokens
  - Required permissions: `repo` (all sub-permissions)

### 3. Verify on GitHub

Go to `https://github.com/YOUR-USERNAME/skills-repository` and you should see all files.

## Part 5: Additional Configuration on GitHub

### 1. Add Topics

In your repository → "About" → ⚙️ → Add topics:
```
python, skills, ai, llm, automation, compound-engineering, 
anthropic-claude, prompt-engineering, skill-library
```

### 2. Configure Branch Protection (Optional but recommended)

Settings → Branches → Add rule:
- Branch name pattern: `main`
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
- ✅ Require conversation resolution before merging

### 3. Enable GitHub Actions

The workflow is already in `.github/workflows/ci.yml`. 

Check in: Actions tab → should run automatically.

### 4. Configure Codecov (Optional)

1. Go to https://codecov.io
2. Connect your repository
3. Copy the token
4. In GitHub: Settings → Secrets → New secret
   - Name: `CODECOV_TOKEN`
   - Value: [your token]

### 5. Create Useful Labels

Settings → Labels → New label:

```
skill:ai-prompts
skill:code
skill:hybrid
status:active
status:deprecated
priority:high
priority:medium
priority:low
good-first-issue
help-wanted
```

## Part 6: Create README Badges (Optional)

Add to the beginning of README.md:

```markdown
# Skills Repository 🚀

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://github.com/YOUR-USERNAME/skills-repository/workflows/Skills%20CI%2FCD/badge.svg)
[![codecov](https://codecov.io/gh/YOUR-USERNAME/skills-repository/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR-USERNAME/skills-repository)
![Contributors](https://img.shields.io/github/contributors/YOUR-USERNAME/skills-repository.svg)
```

## Part 7: Daily Workflow

### Add changes

```bash
# See what changed
git status

# Add specific files
git add file1 file2

# Or add everything
git add .

# Commit
git commit -m "type(scope): message"

# Push
git push
```

### Work with branches

```bash
# Create new feature
git checkout -b feature/new-skill

# Make changes...
git add .
git commit -m "feat(skills): add new-skill"

# Push branch
git push -u origin feature/new-skill

# Create PR on GitHub
# After merge, update main:
git checkout main
git pull origin main

# Delete local branch
git branch -d feature/new-skill
```

### Update from GitHub

```bash
git pull origin main
```

## Part 8: Collaboration

### For contributors

1. **Fork** the repository
2. **Clone** your fork
3. **Create branch** for your feature
4. **Make changes** and commit
5. **Push** to your fork
6. **Open Pull Request** in original repo

### For you (owner)

1. **Review PRs** on GitHub
2. **Comment** and request changes if needed
3. **Approve** and **merge** when ready
4. **Pull** locally to update

## Troubleshooting

### Error: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/skills-repository.git
```

### Error: "Permission denied (publickey)"

If using SSH:
```bash
# Generate new SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key and add it in GitHub Settings → SSH Keys
cat ~/.ssh/id_ed25519.pub
```

### Error: "failed to push some refs"

```bash
# Someone made changes on GitHub that you don't have locally
git pull origin main --rebase
git push origin main
```

### Reject accidentally pushed commit

```bash
# If it was the last commit:
git reset HEAD~1
git push --force-with-lease origin main
```

## Final Checklist ✅

- [ ] Repository created on GitHub
- [ ] Remote configured correctly
- [ ] First push successful
- [ ] README.md looks good on GitHub
- [ ] GitHub Actions working
- [ ] Branch protection configured (optional)
- [ ] Topics added
- [ ] License visible

## Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub CLI Manual](https://cli.github.com/manual/)

---

**Problems?** Open an issue in the repository or check [GitHub documentation](https://docs.github.com/).

**Done! 🎉** Your repository is on GitHub and ready for collaboration.
