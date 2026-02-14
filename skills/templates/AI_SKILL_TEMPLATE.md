# {{SKILL_NAME}}

## Description
[Brief description of this skill's purpose]

## Type
AI Prompt / LLM Skill

## Use Cases
- Use case 1
- Use case 2
- Use case 3

## Prompt Template

### System Prompt
```
[Your system prompt here. This defines the assistant's behavior and personality]

Example:
You are an expert data analyst. Your job is to analyze datasets and provide
actionable insights. Always provide concrete examples and specific numbers.
```

### User Prompt
```
[User prompt template. Use {{variables}} for dynamic parts]

Example:
Analyze the following dataset: {{dataset}}

Focus on: {{focus_areas}}

Provide:
1. Executive summary
2. Key findings (top {{top_n}})
3. Recommendations
```

## Variables

| Variable | Type | Description | Required | Default |
|----------|------|-------------|-----------|---------|
| `dataset` | string | Data to analyze | ✅ | - |
| `focus_areas` | string | Focus areas | ❌ | "general" |
| `top_n` | int | Number of findings | ❌ | 5 |

## Examples

### Example 1: Basic Usage
```python
from scripts.compound_engine import SkillExecutor

executor = SkillExecutor('skills/ai-prompts/{{skill_name}}')
result = executor.execute(
    input_data="[data]",
    focus_areas="sales, trends",
    top_n=3
)
```

### Example 2: In a Chain
```python
from scripts.compound_engine import SkillChain

chain = SkillChain([
    'skills/code/data-loader',
    'skills/ai-prompts/{{skill_name}}',
    'skills/code/report-generator'
])

result = chain.execute(data_source)
```

## Expected Output

```json
{
  "summary": "Analysis summary...",
  "findings": [
    {
      "title": "Finding 1",
      "description": "...",
      "impact": "high"
    }
  ],
  "recommendations": [...]
}
```

## Best Practices

1. **Pre-processing**: Clean the data before passinf it
2. **Context Window**: Consider the token limit
3. **Iteration**: Use multiple calls for large datasets
4. **Validation**: Validate the output against the expected schema

## Dependencies

- None (standalone skill)
- Or: `skills/code/data-validator`

## Testing

```bash
pytest tests/test_{{skill_name}}.py
```

## Performance Metrics

- Average latency: ~2s
- Success rate: 95%
- Token usage: ~500-1000 tokens

## Limitations

- Maximum 10,000 input tokens
- Works best with structured data
- Requires context in Spanish or English

## Changelog

### v1.0.0 - YYYY-MM-DD
- Initial version

## Autor
[Your name]

## Licencia
MIT
