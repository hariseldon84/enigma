#!/usr/bin/env python3
"""
Simple Query Script for Enigma
Connects to local Ollama and queries using Ground Truth documents as context.

Usage:
    python3 scripts/simple_query.py "What are my core principles?"
"""

import sys
import os
from pathlib import Path
import ollama

# Add Enigma root to path
ENIGMA_ROOT = Path(__file__).parent.parent
GROUND_TRUTH_DIR = ENIGMA_ROOT / "99_GroundTruth"

def load_ground_truth_documents():
    """Load all documents from Ground Truth folder."""
    documents = {}

    if not GROUND_TRUTH_DIR.exists():
        print(f"❌ Error: Ground Truth directory not found at {GROUND_TRUTH_DIR}")
        return documents

    # Read all markdown files in Ground Truth
    for file_path in GROUND_TRUTH_DIR.glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                documents[file_path.name] = content
                print(f"✅ Loaded: {file_path.name} ({len(content)} chars)")
        except Exception as e:
            print(f"⚠️  Warning: Could not read {file_path.name}: {e}")

    return documents

def build_context(documents):
    """Build context string from documents."""
    context_parts = []

    for filename, content in documents.items():
        context_parts.append(f"## Document: {filename}\n\n{content}\n\n")

    return "\n---\n\n".join(context_parts)

def query_enigma(question, context, model="gemma2:2b"):
    """Send query to Ollama with context."""

    system_prompt = """You are Enigma, a personal cognitive operating system.

Your constitutional rules:
1. ONLY use information from the provided documents
2. If information is not found, say "Not found in Enigma knowledge"
3. Always cite which document you're referencing
4. No hallucination - stick to facts in the documents
5. Voice: Professional + Casual (direct, no buzzwords, no fluff)
6. Structure responses clearly (use headings, bullets where appropriate)

When answering, cite sources like this: (from Personal_Doctrine.md) or (from Enigma_Constitution.md)
"""

    user_prompt = f"""Based ONLY on the following documents, answer this question:

{question}

---

DOCUMENTS:

{context}

---

Remember: Only use information from these documents. Cite your sources. Be clear and direct."""

    print(f"\n🤔 Querying Enigma (model: {model})...")
    print(f"📄 Context: {len(context)} characters from {len(context.split('## Document:'))-1} documents\n")

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ],
            options={
                'temperature': 0.3,  # Lower = faster, more focused
                'num_predict': 800   # Limit response length for speed
            }
        )

        return response['message']['content']

    except Exception as e:
        return f"❌ Error querying Ollama: {e}\n\nMake sure Ollama is running: ollama serve"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/simple_query.py \"Your question here\"")
        print("\nExample queries:")
        print('  python3 scripts/simple_query.py "What are my core principles?"')
        print('  python3 scripts/simple_query.py "How should Enigma handle uncertainty?"')
        print('  python3 scripts/simple_query.py "What is my writing style?"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    print("="*80)
    print("ENIGMA QUERY INTERFACE")
    print("="*80)
    print(f"\n❓ Question: {question}\n")

    # Load Ground Truth documents
    print("📚 Loading Ground Truth documents...\n")
    documents = load_ground_truth_documents()

    if not documents:
        print("\n❌ No documents found in Ground Truth folder.")
        print(f"   Expected location: {GROUND_TRUTH_DIR}")
        sys.exit(1)

    print(f"\n✅ Loaded {len(documents)} document(s)\n")

    # Build context
    context = build_context(documents)

    # Query Enigma
    answer = query_enigma(question, context)

    # Display answer
    print("="*80)
    print("ENIGMA RESPONSE")
    print("="*80)
    print(f"\n{answer}\n")
    print("="*80)

if __name__ == "__main__":
    main()
