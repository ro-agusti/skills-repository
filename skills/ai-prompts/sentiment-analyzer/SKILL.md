# sentiment-analyzer

## Description

Analyzes the sentiment (positive, negative, or neutral) of any text input. This skill generates a structured prompt for sentiment analysis that can be used with Claude or other LLMs to get consistent, detailed sentiment evaluations.

Perfect for analyzing customer reviews, social media posts, feedback, emails, or any text where understanding emotional tone is important.

## Type

AI Prompt Skill (requires LLM API or manual use)

## Variables

| Variable | Type | Description | Required | Default |
|----------|------|-------------|----------|---------|
| `input` | string | The text to analyze for sentiment | ✅ Yes | - |

## Usage

### Basic Usage

```python
from scripts.compound_engine import SkillExecutor
from pathlib import Path

# Create executor
executor = SkillExecutor(Path('skills/ai-prompts/sentiment-analyzer'))

# Analyze a text
text = "I absolutely love this product! Best purchase ever!"
result = executor.execute(text)

# The result contains a formatted prompt ready for an LLM
print(result['prompt'])
```

### Manual Usage (Free - No API needed)

```python
# Generate prompt
result = executor.execute("This is terrible. Very disappointed.")

# Copy the prompt
prompt = result['prompt']

# Paste into claude.ai and get analysis
```

### With Claude API (Automated)

```python
from anthropic import Anthropic
import os

# Setup
executor = SkillExecutor(Path('skills/ai-prompts/sentiment-analyzer'))
client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Analyze
text = "The service was okay, nothing special."
prompt_result = executor.execute(text)

# Send to Claude
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt_result['prompt']}]
)

# Get analysis
analysis = message.content[0].text
print(analysis)
```

### Batch Processing

```python
# Analyze multiple texts
reviews = [
    "Amazing product! Highly recommend!",
    "Not worth the money. Poor quality.",
    "It's fine, does what it says."
]

for review in reviews:
    result = executor.execute(review)
    # Process each result...
```

## Output Format

The generated prompt asks the LLM to provide:

- **Sentiment**: positive, negative, or neutral
- **Confidence**: Percentage (0-100%)
- **Key phrases**: Words/phrases that indicate the sentiment
- **Brief explanation**: Why this sentiment was determined

### Example Output (from LLM)

```
- Sentiment: Positive
- Confidence: 95%
- Key phrases: "absolutely love", "Best purchase ever"
- Brief explanation: Strong positive language with enthusiastic 
  expressions and superlatives indicating high satisfaction.
```

## Examples

See `examples/README.md` for detailed use cases.

## Use Cases

### Customer Service
- Analyze support tickets to prioritize urgent/negative cases
- Track customer satisfaction over time
- Auto-route complaints to appropriate teams

### Marketing
- Analyze social media mentions
- Evaluate campaign reception
- Monitor brand sentiment

### Product Development
- Analyze product reviews
- Identify pain points from user feedback
- Track feature reception

### Research
- Analyze survey responses
- Study public opinion
- Sentiment trends over time

## Best Practices

### Input Tips
- ✅ Keep texts focused (1-3 sentences work best)
- ✅ Use complete sentences when possible
- ✅ Include context if analyzing fragments
- ❌ Avoid very long texts (>500 words)

### For Accurate Results
1. **Be specific**: Shorter, focused texts give better results
2. **Provide context**: If analyzing a fragment, add context
3. **Batch similar content**: Process similar text types together
4. **Validate edge cases**: Test with neutral/mixed sentiment

### Integration Tips
```python
# Add error handling
try:
    result = executor.execute(user_input)
    # Process result...
except Exception as e:
    print(f"Analysis failed: {e}")

# Validate input
if len(text.strip()) < 3:
    print("Text too short for analysis")
else:
    result = executor.execute(text)
```

## Performance

- **Prompt generation**: Instant (<1ms)
- **LLM analysis** (with API): 1-3 seconds per text
- **Batch processing**: Can handle 100+ texts/minute (with proper rate limiting)
- **Cost** (Claude API): ~$0.0001 per analysis (~1000 analyses per $1)

## Limitations

- ❌ Does not actually analyze sentiment (generates prompt only)
- ❌ Requires LLM (Claude, GPT, etc.) for actual analysis
- ⚠️ Works best with English text (can work with other languages if specified)
- ⚠️ May struggle with very sarcastic or context-heavy text
- ⚠️ Short texts (<10 words) may need additional context

## Troubleshooting

### Problem: "Skill not found"
```bash
# Make sure you created it:
python3 scripts/skill-manager.py create --name "sentiment-analyzer" --type ai-prompts
```

### Problem: "{input} not replaced in prompt"
Check that you're passing the text as the first argument:
```python
# ✅ Correct
result = executor.execute("your text here")

# ❌ Wrong
result = executor.execute(input="your text here")
```

### Problem: "Inconsistent results"
The skill generates the same prompt every time. Inconsistency comes from the LLM. Consider:
- Using temperature=0 for consistent API results
- Adding more specific instructions in prompt.txt
- Providing more context in the input

## Extending This Skill

### Add Language Support
Edit `prompt.txt` and add a language variable:
```
Analyze the sentiment in {language}: {input}
```

Then use:
```python
result = executor.execute(text, language="Spanish")
```

### Add Custom Output Format
Edit `prompt.txt` to request JSON, CSV, or other formats.

### Combine with Other Skills
```python
from scripts.compound_engine import SkillChain

# Analyze then summarize
chain = SkillChain([
    'skills/ai-prompts/sentiment-analyzer',
    'skills/ai-prompts/text-summarizer'
])
```

## Version History

### v1.0.0 - 2024-02-15
- Initial version
- Basic sentiment analysis prompt
- Support for positive/negative/neutral classification
- Confidence scoring
- Key phrase extraction

## Author

Created for the skills-repository framework.

## License

MIT License - Free to use and modify

## Related Skills

- `text-summarizer` - Summarizes long texts
- `keyword-extractor` - Extracts key terms
- `emotion-detector` - Detects specific emotions (joy, anger, etc.)

## Support

- 📖 Full documentation: See repository README.md
- 🐛 Issues: Open an issue on GitHub
- 💬 Questions: Check examples/ folder or ask in discussions

---

**Quick Start**: Just edit `prompt.txt` and run `executor.execute("your text")`! 🚀
