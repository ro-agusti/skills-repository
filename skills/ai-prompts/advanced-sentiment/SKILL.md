# advanced-sentiment

## Description

Enterprise-grade sentiment analysis skill designed for businesses that need deep, context-aware sentiment insights. This skill goes beyond basic positive/negative classification to provide actionable intelligence including emotional indicators, risk assessment, routing recommendations, and priority scoring.

Ideal for customer service platforms, CRM systems, social media monitoring, and any business application requiring nuanced understanding of customer feedback with full context awareness.

## Type

AI Prompt Skill - Advanced (Multi-variable, Context-aware)

## Variables

| Variable | Type | Description | Required | Default |
|----------|------|-------------|----------|---------|
| `input` | string | The text content to analyze | ✅ Yes | - |
| `industry` | string | Business industry (e.g., "e-commerce", "healthcare", "finance") | ✅ Yes | - |
| `language` | string | Language of the content | ✅ Yes | - |
| `business_type` | string | Type of business (e.g., "retail", "B2B", "SaaS") | ✅ Yes | - |
| `content_type` | string | Type of content (e.g., "email complaint", "review", "survey") | ✅ Yes | - |
| `customer_segment` | string | Customer segment (e.g., "premium", "regular", "enterprise") | ✅ Yes | - |
| `interaction_history` | string | Previous interaction context | ❌ No | "" |
| `customer_tier` | string | Customer loyalty tier (e.g., "Gold", "Silver", "Bronze") | ❌ No | "" |
| `product_name` | string | Product/service being discussed | ❌ No | "" |
| `purchase_date` | string | Date of purchase/transaction | ❌ No | "" |
| `departments` | string | Comma-separated list of relevant departments | ❌ No | "" |
| `output_format` | string | Desired output format (e.g., "JSON", "brief summary", "CSV") | ❌ No | "detailed" |

## Usage

### Basic Usage

```python
from scripts.compound_engine import SkillExecutor
from pathlib import Path

executor = SkillExecutor(Path('skills/ai-prompts/advanced-sentiment'))

result = executor.execute(
    "The delivery was 3 days late and product arrived damaged. Very frustrated.",
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="email complaint",
    customer_segment="premium"
)

print(result['prompt'])
```

### Full Context Analysis

```python
result = executor.execute(
    "Package arrived damaged and customer service was unhelpful.",
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="email complaint",
    customer_segment="premium",
    interaction_history="3 previous purchases, 1 resolved complaint",
    customer_tier="Gold",
    product_name="Laptop Stand Pro",
    purchase_date="2024-01-15",
    departments="Customer Service, Logistics, Quality Control",
    output_format="JSON"
)
```

### CRM Integration Example

```python
# Process support ticket with full CRM context
def analyze_support_ticket(ticket_data):
    executor = SkillExecutor(Path('skills/ai-prompts/advanced-sentiment'))
    
    result = executor.execute(
        ticket_data['message'],
        industry="software",
        language=ticket_data['language'],
        business_type="SaaS",
        content_type="support ticket",
        customer_segment=ticket_data['account_type'],
        interaction_history=ticket_data['previous_tickets'],
        customer_tier=ticket_data['subscription_level'],
        product_name=ticket_data['product'],
        purchase_date=ticket_data['signup_date'],
        departments="Support, Engineering, Success",
        output_format="JSON"
    )
    
    return result
```

### Batch Processing with Different Contexts

```python
feedback_items = [
    {
        'text': "Great product but shipping was slow",
        'context': {
            'industry': 'e-commerce',
            'customer_tier': 'Silver',
            'content_type': 'review'
        }
    },
    {
        'text': "System keeps crashing, need urgent help!",
        'context': {
            'industry': 'software',
            'customer_tier': 'Enterprise',
            'content_type': 'support ticket'
        }
    }
]

for item in feedback_items:
    result = executor.execute(
        item['text'],
        language="English",
        business_type="B2B",
        customer_segment="business",
        **item['context']
    )
    # Process results...
```

## Output Format

The generated prompt requests comprehensive analysis including:

### 1. Sentiment Score
- Overall sentiment classification
- Confidence percentage
- Intensity level (mild/moderate/strong)

### 2. Key Insights
- Main concerns or praises identified
- Specific product/service mentions
- Urgency assessment

### 3. Emotional Indicators
- Primary emotion detected
- Communication tone
- Emotional intensity

### 4. Actionable Recommendations
- Suggested response approach
- Priority level for handling
- Department routing suggestions

### 5. Risk Assessment
- Customer churn risk evaluation
- Likelihood of public negative review
- Escalation recommendations

### Example Output (from LLM)

```json
{
  "sentiment_score": {
    "overall": "negative",
    "confidence": 88,
    "intensity": "strong"
  },
  "key_insights": {
    "main_concerns": ["late delivery", "damaged product"],
    "product_mentions": ["Laptop Stand Pro"],
    "urgency": "high"
  },
  "emotional_indicators": {
    "primary_emotion": "frustration",
    "tone": "formal",
    "intensity": "high"
  },
  "recommendations": {
    "response_approach": "immediate apology with replacement offer",
    "priority": "high",
    "route_to": ["Customer Service", "Logistics"]
  },
  "risk_assessment": {
    "churn_risk": "high",
    "review_likelihood": "high"
  }
}
```

## Use Cases

### E-commerce Platform
```python
# Analyze product review with purchase context
result = executor.execute(
    review_text,
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="product review",
    customer_segment="regular",
    product_name=product_info['name'],
    purchase_date=order_date,
    customer_tier=loyalty_level,
    output_format="JSON"
)
```

### SaaS Customer Support
```python
# Prioritize support tickets
result = executor.execute(
    ticket_message,
    industry="software",
    language="English",
    business_type="SaaS",
    content_type="support ticket",
    customer_segment="enterprise",
    interaction_history=ticket_history,
    customer_tier=subscription_plan,
    departments="Support, Engineering",
    output_format="brief summary"
)
```

### Social Media Monitoring
```python
# Analyze social mention
result = executor.execute(
    social_post,
    industry="consumer goods",
    language="English",
    business_type="retail",
    content_type="social media post",
    customer_segment="public",
    output_format="brief summary"
)
```

### Healthcare Patient Feedback
```python
# Analyze patient survey
result = executor.execute(
    feedback_text,
    industry="healthcare",
    language="English",
    business_type="medical services",
    content_type="patient survey",
    customer_segment="patient",
    interaction_history=visit_history,
    departments="Patient Relations, Quality",
    output_format="detailed"
)
```

## Best Practices

### Industry-Specific Configuration

**E-commerce:**
```python
industry="e-commerce"
content_type="product review" | "complaint" | "inquiry"
departments="Customer Service, Logistics, Returns"
```

**SaaS/Software:**
```python
industry="software"
content_type="bug report" | "feature request" | "support ticket"
departments="Support, Engineering, Product"
```

**Healthcare:**
```python
industry="healthcare"
content_type="patient feedback" | "complaint" | "survey"
departments="Patient Relations, Quality Assurance, Clinical"
```

**Financial Services:**
```python
industry="finance"
content_type="complaint" | "inquiry" | "feedback"
departments="Customer Service, Compliance, Risk"
```

### Context Optimization

1. **Always provide industry**: Ensures domain-specific language understanding
2. **Include interaction history**: Enables trend analysis
3. **Specify customer tier**: Helps with prioritization
4. **Use appropriate output format**: 
   - JSON for automation
   - Brief summary for dashboards
   - Detailed for manual review

### Variable Tips

```python
# ✅ GOOD: Specific, informative
interaction_history="3 purchases in 6 months, 1 resolved shipping delay"
customer_tier="Platinum (top 5% spenders)"
departments="Support, Logistics, Customer Success"

# ❌ BAD: Vague, unhelpful
interaction_history="some history"
customer_tier="good"
departments="various"
```

## Integration Patterns

### Pattern 1: Automated Routing

```python
def route_customer_feedback(feedback):
    result = executor.execute(
        feedback['message'],
        industry=config.INDUSTRY,
        language=feedback['detected_language'],
        business_type=config.BUSINESS_TYPE,
        content_type=feedback['type'],
        customer_segment=feedback['segment'],
        customer_tier=feedback['tier'],
        departments=config.ALL_DEPARTMENTS,
        output_format="JSON"
    )
    
    # Parse LLM response
    analysis = parse_llm_response(result)
    
    # Route based on analysis
    if analysis['risk_assessment']['churn_risk'] == 'high':
        route_to_retention_team(feedback, analysis)
    elif analysis['recommendations']['priority'] == 'high':
        escalate_to_manager(feedback, analysis)
    else:
        route_to_department(analysis['recommendations']['route_to'])
```

### Pattern 2: Dashboard Metrics

```python
def analyze_feedback_batch(feedback_list):
    sentiments = {'positive': 0, 'negative': 0, 'neutral': 0}
    high_risk = []
    
    for feedback in feedback_list:
        result = executor.execute(
            feedback['text'],
            industry=feedback['industry'],
            language="English",
            business_type="retail",
            content_type="review",
            customer_segment=feedback['segment'],
            output_format="brief summary"
        )
        
        # Aggregate metrics
        # ... process results
    
    return {
        'sentiment_distribution': sentiments,
        'high_risk_customers': high_risk
    }
```

### Pattern 3: Multi-Language Support

```python
LANGUAGE_MAP = {
    'es': 'Spanish',
    'en': 'English',
    'fr': 'French',
    'de': 'German'
}

def analyze_multilingual(text, lang_code):
    result = executor.execute(
        text,
        industry="e-commerce",
        language=LANGUAGE_MAP[lang_code],
        business_type="retail",
        content_type="review",
        customer_segment="international",
        output_format="JSON"
    )
    return result
```

## Performance

- **Prompt generation**: <1ms (instant)
- **LLM processing**: 2-4 seconds per analysis
- **Recommended batch size**: 50-100 items per batch
- **Rate limiting**: Respect LLM API limits (typically 50-100 req/min)
- **Cost per analysis** (Claude Sonnet): ~$0.0003 (~3,300 analyses per $1)

## Advanced Features

### Custom Department Routing

Edit `prompt.txt` to customize department options:
```
Department options: {departments}
```

Then provide relevant departments:
```python
departments="Tier 1 Support, Tier 2 Support, Engineering, Product Management"
```

### Industry-Specific Keywords

The skill automatically adapts to industry:
- **E-commerce**: shipping, delivery, quality, packaging
- **SaaS**: features, bugs, performance, integrations
- **Healthcare**: care quality, wait times, staff interaction
- **Finance**: security, fees, service, response time

### Dynamic Output Formats

```python
# For API integration
output_format="JSON"

# For email summaries
output_format="brief summary"

# For detailed reports
output_format="detailed markdown"

# For data export
output_format="CSV row"
```

## Limitations

- ⚠️ Requires LLM API for actual analysis (generates prompt only)
- ⚠️ More expensive than basic sentiment due to longer prompts (~3x cost)
- ⚠️ Requires more input data (more variables to fill)
- ⚠️ Best with English; other languages need testing
- ⚠️ Context quality affects output quality (garbage in, garbage out)

## Troubleshooting

### Problem: Too many variables to fill

**Solution**: Create wrapper functions for common use cases:

```python
def analyze_ecommerce_review(review_text, customer_data):
    return executor.execute(
        review_text,
        industry="e-commerce",
        language="English",
        business_type="retail",
        content_type="product review",
        customer_segment=customer_data['segment'],
        customer_tier=customer_data['tier'],
        product_name=customer_data['product'],
        output_format="JSON"
    )

# Now just call:
result = analyze_ecommerce_review(review, customer)
```

### Problem: Inconsistent outputs

**Solution**: 
- Use structured output format (JSON)
- Add output schema to prompt.txt
- Use temperature=0 in API calls
- Validate LLM responses

### Problem: High costs

**Solution**:
- Use basic sentiment-analyzer for simple cases
- Batch process similar items
- Cache results for duplicate inputs
- Use Claude Haiku for lower priority items

## Comparison: Basic vs Advanced

| Feature | sentiment-analyzer | advanced-sentiment |
|---------|-------------------|-------------------|
| Variables | 1 (input only) | 12+ variables |
| Context awareness | None | Full business context |
| Output depth | Basic | Comprehensive |
| Use case | Simple classification | Enterprise CRM integration |
| Cost per call | ~$0.0001 | ~$0.0003 |
| Setup complexity | Very simple | Moderate |
| Best for | Quick checks | Production systems |

**When to use which:**
- Use **sentiment-analyzer** for: Quick tests, simple apps, learning
- Use **advanced-sentiment** for: CRM integration, customer service, analytics

## Version History

### v1.0.0 - 2024-02-15
- Initial version
- Support for 12 context variables
- Industry-specific analysis
- Multi-department routing
- Risk assessment features
- Flexible output formats

## Related Skills

- `sentiment-analyzer` - Simpler version for basic use cases
- `emotion-detector` - Focuses on specific emotions
- `urgency-classifier` - Classifies urgency level
- `customer-churn-predictor` - Predicts churn risk

## Resources

- **Industry templates**: See `examples/industry-templates/`
- **Integration guides**: See `docs/integration/`
- **API examples**: See `examples/api-integration/`

## Support

- 📖 Documentation: Full repo README
- 🐛 Issues: GitHub issues
- 💬 Questions: Discussions forum
- 📧 Enterprise support: Contact repository maintainer

---

**Pro Tip**: Start with basic `sentiment-analyzer`, then upgrade to `advanced-sentiment` when you need context-aware enterprise features! 🚀
