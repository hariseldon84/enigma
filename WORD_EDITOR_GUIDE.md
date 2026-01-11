# Word Document Editor - Usage Guide

**Created:** 2026-01-10
**Purpose:** Automate editing of Word documents using your Writing Standard and Personal Doctrine

---

## WHAT IT DOES

Enigma's Word Document Editor analyzes and refines your documents based on:
- ✅ Your Writing Standard (Professional + Casual tone, no buzzwords, clear structure)
- ✅ Your Personal Doctrine (quality obsession, architecture-first, clarity over cleverness)

**Primary use case:** Product Genome chapter editing

---

## THREE MODES

### Mode 1: CHECK (Analysis Only)
**What it does:** Identifies problems without changing anything

**Use when:** You want to see what's wrong before deciding what to fix

**Command:**
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode check
```

**Output:** List of issues found:
- Buzzwords and banned phrases
- Passive voice instances
- Vague statements
- Poor structure
- Tone mismatches

---

### Mode 2: SUGGEST (Recommendations)
**What it does:** Provides specific improvement suggestions paragraph by paragraph

**Use when:** You want detailed guidance on how to improve

**Command:**
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode suggest
```

**Output:** For each issue:
- Original text (quoted)
- What's wrong and why
- Suggested revision
- Why the revision is better

---

### Mode 3: REFINE (Auto-Rewrite)
**What it does:** Creates a fully rewritten version matching your Writing Standard

**Use when:** You want Enigma to handle the heavy lifting

**Command:**
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode refine
```

**Output:**
- Analysis printed to screen
- NEW file saved to: `06_Derived/[filename]_REFINED.docx`
- Original file untouched (safe)

**Then:** Review refined version, manually apply changes you approve

---

## TYPICAL WORKFLOW

### Step 1: Quick Check
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode check
```

**Review output:** Get overview of issues

---

### Step 2: Get Suggestions
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode suggest
```

**Review output:** See specific improvements recommended

---

### Step 3: Generate Refined Version
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode refine
```

**Opens:** `06_Derived/Chapter_01_REFINED.docx`

**Compare:** Original vs Refined side-by-side

**Apply:** Copy good changes to original document

---

## WHAT IT CHECKS

Based on your Writing_Standard.md:

### ❌ BANNED WORDS (Automatically Flagged)
- "Synergy"
- "Paradigm shift"
- "Best-in-class"
- "World-class"
- "Cutting-edge"
- "Revolutionary"
- "Game-changing"
- "Leverage" (as vague verb)
- "Circle back"
- "Touch base"
- "Move the needle"

### ⚠️ PATTERNS TO AVOID
- Passive voice ("It was decided" → "We decided")
- Vague modifiers ("significantly improved" → "improved by 35%")
- Hedging ("We might possibly" → "We will")
- Long intros before getting to point

### ✅ ENFORCES YOUR STANDARDS
- Professional + Casual tone
- Direct, no fluff
- Structured (headings, bullets)
- Concrete over abstract
- Clarity over cleverness

---

## EXAMPLES

### Example 1: Check Mode

**Input:**
```bash
python3 scripts/edit_document.py --file my_chapter.docx --mode check
```

**Sample Output:**
```
ISSUES FOUND:

1. Buzzword in paragraph 2:
   "Our revolutionary approach leverages cutting-edge technology..."
   Problem: Uses banned words "revolutionary", "leverages", "cutting-edge"

2. Passive voice in paragraph 5:
   "It was discovered that users prefer..."
   Problem: Passive voice. Should be: "We discovered users prefer..."

3. Vague statement in paragraph 8:
   "This significantly improved performance..."
   Problem: "Significantly" without numbers. Should specify: "improved by X%"
```

---

### Example 2: Suggest Mode

**Input:**
```bash
python3 scripts/edit_document.py --file my_chapter.docx --mode suggest
```

**Sample Output:**
```
SUGGESTIONS:

Paragraph 2:
ORIGINAL: "Our revolutionary approach leverages cutting-edge technology to create synergies."
PROBLEM: Buzzwords, vague, corporate speak
SUGGESTED: "Our approach uses AI and automation to reduce processing time by 40%."
WHY BETTER: Specific, concrete, no buzzwords, quantified benefit

Paragraph 5:
ORIGINAL: "It was discovered that users prefer simple interfaces."
PROBLEM: Passive voice, weak
SUGGESTED: "We found users prefer simple interfaces."
WHY BETTER: Active voice, direct, stronger
```

---

### Example 3: Refine Mode

**Input:**
```bash
python3 scripts/edit_document.py --file my_chapter.docx --mode refine
```

**Sample Output:**
```
Saved to: 06_Derived/my_chapter_REFINED.docx

BEFORE: "In today's fast-paced business environment, organizations are increasingly leveraging innovative solutions to drive transformational change and create unprecedented value."

AFTER: "Companies now use AI and automation to improve operations. This reduces costs by 30-50% and speeds decision-making."
```

---

## TIPS FOR BEST RESULTS

### 1. Start with CHECK Mode
Get overview before diving into details.

### 2. Use SUGGEST for Learning
See patterns in your writing, improve over time.

### 3. Use REFINE for Speed
When you need quick cleanup of heavily flawed drafts.

### 4. Always Review Refined Output
Don't blindly accept. Enigma suggests, you decide.

### 5. Iterate
- Run check → fix major issues manually → run suggest → refine remaining
- Multiple passes better than one big rewrite

---

## TESTING IT

### Quick Test with Sample Text

Create a test file with common issues:

**test_document.docx:**
```
Our revolutionary platform leverages cutting-edge AI to transform the way organizations approach strategic initiatives, creating unprecedented synergies across multiple stakeholder touchpoints.

It was discovered that users significantly prefer innovative solutions that can drive meaningful change in today's fast-paced environment.
```

**Run check:**
```bash
python3 scripts/edit_document.py --file test_document.docx --mode check
```

**Expected:** Flags "revolutionary", "leverages", "cutting-edge", "synergies", passive voice, vague words

---

## WHAT TO EXPECT

### ✅ GOOD RESULTS
- Clear identification of buzzwords
- Passive voice detected
- Vague statements flagged
- Concrete suggestions
- Improved clarity

### ⚠️ LIMITATIONS
- May miss subtle issues
- Context-dependent suggestions (review needed)
- Won't understand domain-specific jargon perfectly
- Can't judge factual accuracy (only style)

### 🎯 BEST FOR
- Product Genome chapters (your #1 use case)
- Strategy documents
- Proposals
- Business writing
- Anything matching your Writing Standard

---

## TROUBLESHOOTING

### "File not found"
```bash
# Use full path or ensure you're in Enigma root
cd ~/Enigma
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode check
```

### "Ollama connection error"
```bash
# Make sure Ollama is running
ollama serve
```

### "Takes too long"
- gemma2:2b should respond in 20-45 seconds
- If slower, check system memory
- Try shorter documents first

### "Suggestions not helpful"
- Mode CHECK for quick overview
- Mode SUGGEST for detailed help
- Mode REFINE may need manual review and selective copying

---

## NEXT STEPS AFTER EDITING

### 1. Review Refined Version
Open: `06_Derived/[filename]_REFINED.docx`

### 2. Compare Side-by-Side
- Original in one window
- Refined in another
- Cherry-pick good changes

### 3. Update Original
Manually apply approved improvements to your original file

### 4. Re-index (Optional)
```bash
python3 scripts/index_documents.py
```

Makes updated version searchable in Enigma

---

## AUTOMATED WORKFLOW (FUTURE)

**Coming soon:**
- Batch mode (edit multiple chapters at once)
- Direct in-place editing (with backup)
- Integration with Product Genome project tracker
- Track which suggestions you typically accept/reject

---

**Ready to test? Pick a Product Genome chapter and try CHECK mode first!**
