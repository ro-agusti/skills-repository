import sys
from pathlib import Path

# Add scripts directory to Python path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

# Now import
from compound_engine import SkillExecutor

def test_sentiment():
    print("\n" + "="*70)
    print("SENTIMENT ANALYZER TEST")
    print("="*70)
    
    # Create executor
    skill_path = Path('skills/ai-prompts/sentiment-analyzer')
    
    if not skill_path.exists():
        print("\n❌ ERROR: Skill not found!")
        print("\nPlease create it first:")
        print("  python scripts/skill-manager.py create --name sentiment-analyzer --type ai-prompts")
        print("\nThen edit: skills/ai-prompts/sentiment-analyzer/prompt.txt")
        return
    
    executor = SkillExecutor(skill_path)
    
    # Test texts
    texts = [
        "I absolutely love this! Best experience ever!",
        "This is terrible. Very disappointed.",
        "It's okay, nothing special."
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n{'='*70}")
        print(f"Test {i}: {text}")
        print('='*70)
        
        try:
            result = executor.execute(text)
            
            print("\n📝 Generated Prompt:")
            print("-" * 70)
            print(result['prompt'])
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\nMake sure you edited the prompt.txt file!")
    
    print("\n" + "="*70)
    print("✅ Test completed!")
    print("\n💡 This prompt is ready to send to Claude API")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_sentiment()