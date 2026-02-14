import sys
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded .env file")
except ImportError:
    print("⚠️  python-dotenv not installed, using environment variables")

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
from compound_engine import SkillExecutor

def analyze_with_claude(text: str) -> dict:
    """Analyze sentiment using Claude API"""
    
    # Check if anthropic is installed
    try:
        from anthropic import Anthropic
    except ImportError:
        print("\n❌ Anthropic SDK not installed!")
        print("Install it with: pip install anthropic")
        return None
    
    # Check for API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("\n❌ ANTHROPIC_API_KEY not found!")
        print("\nSet it with:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        print("\nGet your key at: https://console.anthropic.com/")
        return None
    
    # Create executor for our skill
    executor = SkillExecutor(Path('skills/ai-prompts/sentiment-analyzer'))
    
    # Generate the prompt using our skill
    prompt_result = executor.execute(text)
    prompt = prompt_result['prompt']
    
    print(f"\n📤 Sending to Claude API...")
    
    # Call Claude API
    client = Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract response
    response_text = message.content[0].text
    
    return {
        'input': text,
        'prompt': prompt,
        'analysis': response_text,
        'model': message.model,
        'tokens_used': message.usage.input_tokens + message.usage.output_tokens
    }

def main():
    print("\n" + "="*70)
    print("SENTIMENT ANALYZER - WITH REAL CLAUDE API")
    print("="*70)
    
    # Test texts
    texts = [
        "I absolutely love this! Best experience ever!",
        "This is terrible. Very disappointed.",
        "It's okay, nothing special."
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n{'='*70}")
        print(f"Test {i}: \"{text}\"")
        print('='*70)
        
        result = analyze_with_claude(text)
        
        if result:
            print(f"\n📊 REAL SENTIMENT ANALYSIS FROM CLAUDE:")
            print("-" * 70)
            print(result['analysis'])
            print("-" * 70)
            print(f"Model: {result['model']}")
            print(f"Tokens used: {result['tokens_used']}")
        else:
            print("\n⚠️  Skipping (API not configured)")
            break
    
    print("\n" + "="*70)
    print("✅ Analysis completed!")
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
