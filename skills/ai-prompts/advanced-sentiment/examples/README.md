# Examples - advanced-sentiment

Complete examples showing real-world usage of the advanced-sentiment skill.

---

## Example 1: E-commerce Customer Complaint

### Scenario
A Gold tier customer reports a damaged product delivery.

### Code

```python
from scripts.compound_engine import SkillExecutor
from pathlib import Path

executor = SkillExecutor(Path('skills/ai-prompts/advanced-sentiment'))

result = executor.execute(
    "The delivery was 3 days late and the product arrived damaged. Very frustrated with this experience.",
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="email complaint",
    customer_segment="premium",
    interaction_history="2 previous purchases, 1 complaint resolved satisfactorily",
    customer_tier="Gold",
    product_name="Laptop Stand Pro",
    purchase_date="2024-01-15",
    departments="Customer Service, Logistics, Quality Control",
    output_format="JSON"
)

print(result['prompt'])
```

### Expected Analysis (from LLM)
```json
{
  "sentiment_score": {
    "overall": "negative",
    "confidence": 92,
    "intensity": "strong"
  },
  "key_insights": {
    "main_concerns": ["late delivery", "damaged product"],
    "urgency": "high",
    "product_mentions": ["Laptop Stand Pro"]
  },
  "recommendations": {
    "response_approach": "Immediate replacement with expedited shipping + discount code",
    "priority": "high",
    "route_to": ["Customer Service", "Logistics"]
  },
  "risk_assessment": {
    "churn_risk": "high",
    "review_likelihood": "high"
  }
}
```

### Use Case
- Auto-route to senior customer service rep
- Flag for retention team follow-up
- Trigger automatic replacement process

---

## Example 2: SaaS Support Ticket - Critical Bug

### Scenario
Enterprise customer reports system outage affecting their business.

### Code

```python
result = executor.execute(
    "Our entire team can't access the platform for the last 2 hours. This is costing us thousands in lost productivity. Need immediate help!",
    industry="software",
    language="English",
    business_type="SaaS",
    content_type="support ticket",
    customer_segment="enterprise",
    interaction_history="12 months customer, 3 previous tickets (all resolved quickly)",
    customer_tier="Enterprise",
    product_name="Project Management Suite",
    purchase_date="2023-02-10",
    departments="Support, Engineering, Customer Success",
    output_format="JSON"
)
```

### Expected Analysis
```json
{
  "sentiment_score": {
    "overall": "negative",
    "confidence": 95,
    "intensity": "strong"
  },
  "emotional_indicators": {
    "primary_emotion": "frustration",
    "urgency_indicators": ["can't access", "2 hours", "costing us thousands", "immediate help"]
  },
  "recommendations": {
    "priority": "critical",
    "route_to": ["Engineering", "Customer Success"],
    "suggested_sla": "< 15 minutes"
  },
  "risk_assessment": {
    "churn_risk": "high",
    "escalation_needed": true
  }
}
```

### Actions Triggered
- Immediate escalation to engineering
- Customer success manager notified
- Auto-create incident report
- Priority SLA: 15 minutes

---

## Example 3: Positive Product Review

### Scenario
Regular customer leaves enthusiastic product review.

### Code

```python
result = executor.execute(
    "Amazing product! Exceeded my expectations. The quality is outstanding and shipping was super fast. Will definitely buy again!",
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="product review",
    customer_segment="regular",
    interaction_history="First purchase",
    customer_tier="Silver",
    product_name="Wireless Headphones Pro",
    purchase_date="2024-02-10",
    departments="Marketing, Product Team",
    output_format="brief summary"
)
```

### Expected Analysis
```
Sentiment: Strongly Positive (95% confidence)

Key highlights:
- "Amazing", "exceeded expectations", "outstanding quality"
- Fast shipping specifically praised
- High repurchase intent

Recommendations:
- Feature in marketing materials
- Send loyalty program invitation
- Request permission to use as testimonial
- Product team: Continue current quality standards

Risk: None (retention likely, advocacy potential high)
```

### Actions Triggered
- Add to testimonials database
- Send thank you email with discount
- Invite to loyalty program
- Share with product team

---

## Example 4: Neutral Feedback

### Scenario
Customer provides balanced feedback on product.

### Code

```python
result = executor.execute(
    "The product works as described. Shipping was on time. Price is a bit high but quality seems good so far.",
    industry="e-commerce",
    language="English",
    business_type="retail",
    content_type="follow-up survey",
    customer_segment="regular",
    interaction_history="3 purchases in last year",
    customer_tier="Bronze",
    product_name="USB Cable 6ft",
    purchase_date="2024-02-12",
    departments="Product, Marketing",
    output_format="CSV row"
)
```

### Expected Analysis (CSV format)
```
"neutral", "75", "moderate", "price concern", "low", "medium", "Product, Marketing", "Consider price-match guarantee"
```

### Use Case
- Aggregate with similar feedback
- Product team: Review pricing strategy
- Marketing: Emphasize value proposition

---

## Example 5: Batch Processing - Daily Reviews

### Scenario
Process all daily product reviews for dashboard.

### Code

```python
daily_reviews = [
    {
        'text': "Great product, fast delivery!",
        'tier': "Silver",
        'product': "Widget A"
    },
    {
        'text': "Not worth the price. Disappointed.",
        'tier': "Gold",
        'product': "Widget B"
    },
    {
        'text': "Decent quality, arrived on time.",
        'tier': "Bronze",
        'product': "Widget C"
    }
]

results = []
for review in daily_reviews:
    result = executor.execute(
        review['text'],
        industry="e-commerce",
        language="English",
        business_type="retail",
        content_type="product review",
        customer_segment="regular",
        customer_tier=review['tier'],
        product_name=review['product'],
        output_format="JSON"
    )
    results.append(result)

# Aggregate results for dashboard
positive_count = sum(1 for r in results if 'positive' in str(r))
negative_count = sum(1 for r in results if 'negative' in str(r))

print(f"Daily Summary: {positive_count} positive, {negative_count} negative")
```

---

## Example 6: Multi-Language Support

### Scenario
Analyze international customer feedback.

### Code

```python
# Spanish feedback
result_es = executor.execute(
    "El producto llegó tarde y está dañado. Muy decepcionado.",
    industry="e-commerce",
    language="Spanish",
    business_type="retail",
    content_type="email complaint",
    customer_segment="international",
    customer_tier="Silver",
    departments="Customer Service, International",
    output_format="JSON"
)

# French feedback
result_fr = executor.execute(
    "Excellent produit! Livraison rapide et qualité superbe!",
    industry="e-commerce",
    language="French",
    business_type="retail",
    content_type="product review",
    customer_segment="international",
    customer_tier="Gold",
    departments="Marketing, International",
    output_format="brief summary"
)
```

---

## Example 7: Healthcare Patient Feedback

### Scenario
Analyze patient satisfaction survey.

### Code

```python
result = executor.execute(
    "The doctor was very attentive and explained everything clearly. However, the wait time was too long - over 45 minutes past my appointment.",
    industry="healthcare",
    language="English",
    business_type="medical services",
    content_type="patient survey",
    customer_segment="patient",
    interaction_history="3 visits in past year, all positive",
    departments="Patient Relations, Operations, Clinical",
    output_format="detailed"
)
```

### Expected Analysis
```
Mixed Sentiment: Positive (doctor interaction) + Negative (wait time)

Positive aspects:
- Doctor attentiveness: Highly praised
- Clear communication: Valued by patient

Concerns:
- Wait time: 45+ minutes delay
- Operational efficiency issue

Recommendations:
- Thank doctor (maintain quality)
- Operations: Review scheduling
- Patient Relations: Follow-up on wait time
- Priority: Medium (address scheduling, retain patient satisfaction with care)

Risk Assessment:
- Churn risk: Low (satisfied with care quality)
- Improvement opportunity: Operations
```

---

## Example 8: Financial Services Complaint

### Scenario
Customer complaint about service fees.

### Code

```python
result = executor.execute(
    "I was charged an unexpected fee that wasn't disclosed. When I called support, I was on hold for 30 minutes. Very unhappy with this treatment.",
    industry="finance",
    language="English",
    business_type="banking",
    content_type="complaint",
    customer_segment="premium",
    interaction_history="5 years, no previous complaints",
    customer_tier="Premium",
    departments="Customer Service, Compliance, Retention",
    output_format="JSON"
)
```

### Actions Triggered
- Compliance review (fee disclosure issue)
- Customer retention contact within 24h
- Service quality review (long hold time)
- Account credit consideration

---

## Example 9: Integration with CRM

### Scenario
Automatic analysis when ticket is created.

### Code

```python
def analyze_new_ticket(ticket_data):
    """
    Called automatically when new support ticket is created
    """
    executor = SkillExecutor(Path('skills/ai-prompts/advanced-sentiment'))
    
    result = executor.execute(
        ticket_data['message'],
        industry=COMPANY_INDUSTRY,
        language=ticket_data['language'],
        business_type=BUSINESS_TYPE,
        content_type="support ticket",
        customer_segment=ticket_data['customer']['segment'],
        interaction_history=get_customer_history(ticket_data['customer_id']),
        customer_tier=ticket_data['customer']['tier'],
        product_name=ticket_data['product'],
        purchase_date=ticket_data['customer']['signup_date'],
        departments=",".join(AVAILABLE_DEPARTMENTS),
        output_format="JSON"
    )
    
    # Parse LLM response
    analysis = call_llm_api(result['prompt'])
    
    # Take actions based on analysis
    if analysis['risk_assessment']['churn_risk'] == 'high':
        create_retention_alert(ticket_data['customer_id'])
    
    if analysis['recommendations']['priority'] == 'critical':
        escalate_ticket(ticket_data['ticket_id'])
    
    route_to_department(
        ticket_data['ticket_id'],
        analysis['recommendations']['route_to']
    )
    
    return analysis
```

---

## Example 10: Dashboard Analytics

### Scenario
Weekly sentiment analysis report.

### Code

```python
def generate_weekly_report(feedback_list):
    """
    Generate weekly sentiment analytics
    """
    executor = SkillExecutor(Path('skills/ai-prompts/advanced-sentiment'))
    
    metrics = {
        'total': len(feedback_list),
        'positive': 0,
        'negative': 0,
        'neutral': 0,
        'high_risk': [],
        'by_department': {}
    }
    
    for feedback in feedback_list:
        result = executor.execute(
            feedback['text'],
            industry=feedback['industry'],
            language="English",
            business_type="retail",
            content_type=feedback['type'],
            customer_segment=feedback['segment'],
            customer_tier=feedback['tier'],
            output_format="JSON"
        )
        
        # Call LLM and aggregate
        analysis = call_llm_api(result['prompt'])
        
        # Update metrics
        sentiment = analysis['sentiment_score']['overall']
        metrics[sentiment] += 1
        
        if analysis['risk_assessment']['churn_risk'] == 'high':
            metrics['high_risk'].append(feedback['customer_id'])
    
    return metrics
```

---

## Tips for Each Example

### E-commerce (Examples 1, 3, 4)
- Always include product name
- Track delivery/shipping mentions
- Monitor tier for prioritization

### SaaS (Example 2)
- Enterprise = high priority
- Include interaction history
- Route critical issues fast

### Multi-language (Example 6)
- Specify language explicitly
- Consider cultural context
- May need language-specific prompts

### Healthcare (Example 7)
- Balance clinical + operational feedback
- Privacy considerations
- Patient satisfaction focus

### Integration (Examples 9, 10)
- Automate common workflows
- Build analytics over time
- Use structured outputs (JSON)

---

**Need more examples?** Check the main SKILL.md or create your own based on these templates!
