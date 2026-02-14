#!/usr/bin/env python3
"""
Test Advanced Sentiment Analyzer

Shows the power of multiple variables in a skill.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
from compound_engine import SkillExecutor

def test_advanced_sentiment():
    print("\n" + "="*70)
    print("ADVANCED SENTIMENT ANALYZER - Multi-Variable Example")
    print("="*70)
    
    # Create executor
    skill_path = Path('skills/ai-prompts/advanced-sentiment')
    
    if not skill_path.exists():
        print("\n❌ Skill not found!")
        print("\nCreate it first:")
        print("  python3 scripts/skill-manager.py create --name advanced-sentiment --type ai-prompts")
        print("\nThen edit: skills/ai-prompts/advanced-sentiment/prompt.txt")
        print("(Copy the template from WHY_SKILLS_MATTER.md)")
        return
    
    executor = SkillExecutor(skill_path)
    
    # Test case 1: Angry customer
    print("\n" + "="*70)
    print("TEST 1: ANGRY CUSTOMER")
    print("="*70)
    
    result1 = executor.execute(
        "The delivery was 3 days late and the product arrived damaged. Very frustrated.",  # ← input_data as first argument
        industry="e-commerce",
        language="English",
        business_type="retail",
        content_type="email complaint",
        customer_segment="premium",
        interaction_history="2 previous purchases, 1 complaint resolved",
        customer_tier="Gold",
        product_name="Laptop Stand Pro",
        purchase_date="2024-01-15",
        departments="Customer Service, Logistics, Quality Control",
        output_format="JSON"
    )
    
    print("\n📋 GENERATED PROMPT:")
    print("-" * 70)
    print(result1['prompt'])
    
    # Test case 2: Happy customer
    print("\n" + "="*70)
    print("TEST 2: HAPPY CUSTOMER")
    print("="*70)
    
    result2 = executor.execute(
        "Amazing product! Exceeded my expectations. Will definitely buy again!",
        industry="e-commerce",
        language="English",
        business_type="retail",
        content_type="product review",
        customer_segment="regular",
        interaction_history="First purchase",
        customer_tier="Silver",
        product_name="Wireless Headphones",
        purchase_date="2024-02-10",
        departments="Marketing, Product Team",
        output_format="brief summary"
    )
    
    print("\n📋 GENERATED PROMPT:")
    print("-" * 70)
    print(result2['prompt'])
    
    # Test case 3: Neutral feedback
    print("\n" + "="*70)
    print("TEST 3: NEUTRAL FEEDBACK")
    print("="*70)
    
    result3 = executor.execute(
        "The product works as described. Shipping was on time.",
        industry="e-commerce",
        language="English",
        business_type="retail",
        content_type="follow-up survey",
        customer_segment="regular",
        interaction_history="3 purchases in last year",
        customer_tier="Bronze",
        product_name="Phone Case",
        purchase_date="2024-02-12",
        departments="Quality Assurance",
        output_format="CSV row"
    )
    
    print("\n📋 GENERATED PROMPT:")
    print("-" * 70)
    print(result3['prompt'])
    
    print("\n" + "="*70)
    print("✅ Tests completed!")
    print("\n💡 Notice how:")
    print("   - Each prompt is CUSTOMIZED with all the context")
    print("   - Same skill, different use cases")
    print("   - The {variables} were all replaced automatically")
    print("   - You wrote the template ONCE, used it 3 times")
    print("\n🎯 This is the power of skills!")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_advanced_sentiment()