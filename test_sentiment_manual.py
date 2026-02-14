#!/usr/bin/env python3
"""
Sentiment Analyzer - Manual Version (No API needed)

This version generates prompts that you can copy/paste into Claude.ai
Perfect for testing without API credits!

USAGE:
1. Run: python3 test_sentiment_manual.py
2. Copy the generated prompts
3. Paste them into claude.ai chat
4. See the results!
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
from compound_engine import SkillExecutor

def analyze_manually(text: str) -> dict:
    """Generate prompt for manual analysis"""
    
    # Create executor for our skill
    executor = SkillExecutor(Path('skills/ai-prompts/sentiment-analyzer'))
    
    # Generate the prompt using our skill
    prompt_result = executor.execute(text)
    
    return {
        'input': text,
        'prompt': prompt_result['prompt']
    }

def main():
    print("\n" + "="*70)
    print("SENTIMENT ANALYZER - MANUAL MODE (No API needed!)")
    print("="*70)
    print("\nHow to use:")
    print("1. Run this script")
    print("2. Copy each prompt below")
    print("3. Paste into claude.ai")
    print("4. Get your analysis!")
    print("\n" + "="*70)
    
    # Test texts
    texts = [
        "I absolutely love this! Best experience ever!",
        "This is terrible. Very disappointed.",
        "It's okay, nothing special."
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n{'='*70}")
        print(f"📝 TEST {i}: \"{text}\"")
        print('='*70)
        
        result = analyze_manually(text)
        
        print("\n📋 COPY THIS PROMPT AND PASTE IN CLAUDE.AI:")
        print("-" * 70)
        print(result['prompt'])
        print("-" * 70)
        
        print("\n💡 Instructions:")
        print("   1. Select all the text above (between the lines)")
        print("   2. Copy it (Cmd+C or Ctrl+C)")
        print("   3. Go to claude.ai")
        print("   4. Paste and send")
        print("   5. Claude will analyze the sentiment!")
        
        if i < len(texts):
            print("\n⏸️  Press Enter for next example...")
            input()
    
    print("\n" + "="*70)
    print("✅ All prompts generated!")
    print("\n🎓 What you learned:")
    print("   - Your skill generates PERFECT prompts")
    print("   - You can use them manually (free)")
    print("   - Or send via API (costs money)")
    print("   - Either way, the skill does the same job!")
    print("="*70 + "\n")

if __name__ == "__main__":
    # Check if skill exists
    skill_path = Path('skills/ai-prompts/sentiment-analyzer')
    if not skill_path.exists():
        print("\n❌ Skill not found!")
        print("Create it first with:")
        print("  python scripts/skill-manager.py create --name sentiment-analyzer --type ai-prompts")
        sys.exit(1)
    
    main()