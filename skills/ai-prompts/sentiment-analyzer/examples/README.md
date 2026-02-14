# Examples - sentiment-analyzer

## Example 1: Basic Usage
```python
from scripts.compound_engine import SkillExecutor
from pathlib import Path

executor = SkillExecutor(Path('skills/ai-prompts/sentiment-analyzer'))
result = executor.execute("I love this product!")
```

**Output:**
```
# System Prompt
You are an expert sentiment analysis assistant...

TEXT: I love this product!
```

**Expected Analysis:**
- Sentiment: Positive
- Confidence: 90%

---

## Example 2: Negative Review
```python
result = executor.execute("Terrible quality, very disappointed")
```

**Use case:** Analyzing customer complaints

---

## Example 3: Batch Processing
```python
reviews = [
    "Great service!",
    "Could be better",
    "Worst experience ever"
]

for review in reviews:
    result = executor.execute(review)
    # Send to Claude API...
```

**Use case:** Processing multiple reviews at once
