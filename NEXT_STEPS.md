# NEXT STEPS — Post Model Download Tasks

**Created:** 2026-01-10
**Status:** Waiting for qwen3:30b download to complete
**Purpose:** Step-by-step guide for building Enigma Phase 1

---

## IMMEDIATE: Once Model Download Completes

### ✅ Checkpoint 1: Verify Model Installation
**Time:** 2-3 minutes

```bash
# Verify model is installed
ollama list

# Should show qwen3:30b in the list
```

**Expected Output:**
```
NAME            ID              SIZE      MODIFIED
qwen3:30b       abc123...       17.3 GB   X seconds ago
```

---

### ✅ Checkpoint 2: Test Model with Basic Prompt
**Time:** 3-5 minutes

```bash
# Run the model interactively
ollama run qwen3:30b
```

**Test Prompt:**
```
You are Enigma, a personal cognitive operating system. Your purpose is cognitive augmentation, institutional memory, execution support, and system intelligence.

Respond to this principle: "Quality is non-negotiable. Good enough is not a POC - it is finished work."

How would you approach editing a draft document based on this principle?
```

**What to Look For:**
- Does it understand the constraint?
- Is the response structured and clear?
- Does it match "Professional + Casual" tone?
- Is there any hallucination or vague fluff?

**Exit the test:**
Type `/bye` and press Enter

---

### ✅ Checkpoint 3: Verify Ollama API is Running
**Time:** 1 minute

```bash
# Check if Ollama API is accessible
curl http://localhost:11434/api/tags
```

**Expected Output:**
JSON response listing installed models including qwen3:30b

---

## PHASE 1A: Basic Python Integration (30-45 minutes)

### Task 1: Install Python Dependencies
**Time:** 5-10 minutes

```bash
# Navigate to Enigma folder
cd ~/Enigma

# Install required packages
pip3 install ollama chromadb llama-index python-docx pymupdf pdfplumber openpyxl watchdog pydantic langchain
```

**Verify Installation:**
```bash
python3 -c "import ollama; print('Ollama: OK')"
python3 -c "import chromadb; print('ChromaDB: OK')"
python3 -c "import llama_index; print('LlamaIndex: OK')"
```

---

### Task 2: Create Simple Query Script
**Time:** 10-15 minutes
**File:** `scripts/simple_query.py`

**Purpose:** Test basic interaction with Ollama using Enigma's doctrine.

**What Claude Code Should Do:**
1. Create `scripts/` folder in Enigma root
2. Create `simple_query.py` that:
   - Connects to Ollama
   - Loads Personal_Doctrine.md
   - Sends a query with doctrine as context
   - Returns structured response

**Test Query:**
"What are my core principles regarding quality and building?"

**Expected Behavior:**
Should cite Personal_Doctrine.md and quote specific principles.

---

### Task 3: Test Ground Truth Document Reading
**Time:** 10-15 minutes

**Purpose:** Verify Enigma can read and use Ground Truth documents.

**Test Queries to Run:**
1. "What is my decision-making hierarchy?"
2. "How should Enigma handle uncertainty?"
3. "What are my non-negotiables?"
4. "What is my relationship with AI?"

**Expected Behavior:**
- Each answer should cite specific sections from Personal_Doctrine.md or Enigma_Constitution.md
- No hallucination or invention
- If information not found, should say "Not found in Enigma knowledge"

---

## PHASE 1B: Document Ingestion Pipeline (1-2 hours)

### Task 4: Build Document Loader
**Time:** 20-30 minutes
**File:** `scripts/document_loader.py`

**Purpose:** Read all document types in Enigma folder.

**Requirements:**
- Read .md, .txt files (native)
- Read .docx files (python-docx)
- Read .pdf files (pymupdf)
- Extract text with metadata (filename, path, layer classification)

**Test:**
Load all documents from `99_GroundTruth/` and count:
- How many documents found?
- Total word count across all documents
- Any read errors?

---

### Task 5: Implement Semantic Indexing
**Time:** 30-45 minutes
**File:** `scripts/indexer.py`

**Purpose:** Create vector embeddings for semantic search.

**Requirements:**
- Use ChromaDB (local persistent storage)
- Create embeddings using Ollama's embedding model
- Store with metadata (layer, filename, section)
- Support incremental updates (don't re-index unchanged files)

**Test:**
Index all `99_GroundTruth/` documents, then query:
- "What are principles about building?"
- Should return relevant chunks from Personal_Doctrine.md

---

### Task 6: Build Query Interface
**Time:** 20-30 minutes
**File:** `scripts/enigma_query.py`

**Purpose:** Simple CLI to query Enigma knowledge.

**Usage:**
```bash
python3 scripts/enigma_query.py "What are my decision filters for saying yes to opportunities?"
```

**Requirements:**
- Accept query as command-line argument
- Retrieve relevant documents from vector DB
- Send to Ollama with context
- Return structured answer with sources cited

**Test with These Queries:**
1. "What is my writing style?"
2. "List my top 3 active projects"
3. "What are my non-negotiables?"
4. "How should Enigma handle conflicts between instructions?"

---

## PHASE 1C: First Automation - Product Genome Editor (2-3 hours)

### Task 7: Word Document Reader
**Time:** 20-30 minutes
**File:** `scripts/word_editor.py`

**Purpose:** Read and analyze Word documents.

**Requirements:**
- Read .docx files paragraph by paragraph
- Preserve formatting structure
- Extract sections (headings, body, bullets)

**Test:**
Read any existing Word document and output structure.

---

### Task 8: Writing Standard Enforcer
**Time:** 30-45 minutes
**File:** `scripts/writing_enforcer.py`

**Purpose:** Analyze text against Writing_Standard.md.

**Requirements:**
- Load Writing_Standard.md as reference
- Check for banned words/phrases
- Flag passive voice
- Flag vague modifiers
- Check structure (headings, bullets, clarity)
- Suggest improvements

**Test Text:**
"Our innovative platform leverages cutting-edge AI to revolutionize workflows and create synergies."

**Expected Output:**
- Flag: "innovative", "leverages", "cutting-edge", "revolutionize", "synergies"
- Suggest: Be specific about what the platform does
- Suggest: Replace buzzwords with concrete descriptions

---

### Task 9: Document Refinement Tool
**Time:** 45-60 minutes
**File:** `scripts/refine_document.py`

**Purpose:** Full automation for editing documents per Personal Doctrine + Writing Standard.

**Usage:**
```bash
python3 scripts/refine_document.py --file "path/to/document.docx" --mode full
```

**Modes:**
- `check` — Analyze only, no changes
- `suggest` — Provide suggestions
- `full` — Apply improvements automatically

**Requirements:**
1. Read document
2. Load Personal_Doctrine.md + Writing_Standard.md as context
3. For each paragraph:
   - Check against writing standards
   - Improve clarity
   - Remove fluff
   - Ensure professional + casual tone
   - Cite which standard it's applying
4. Generate refined version
5. Show diff (what changed and why)

**Test:**
Create a sample document with common issues:
- Buzzwords
- Passive voice
- Vague statements
- Poor structure

Run refinement and verify improvements align with Writing Standard.

---

## PHASE 1D: Integration & Polish (1-2 hours)

### Task 10: Create Unified CLI Interface
**Time:** 30-45 minutes
**File:** `enigma.py` (root level)

**Purpose:** Single entry point for all Enigma operations.

**Usage:**
```bash
# Query knowledge
python3 enigma.py query "What are my principles?"

# Ingest new documents
python3 enigma.py ingest --folder 01_Skills_And_Education

# Edit document
python3 enigma.py edit --file document.docx --mode suggest

# Show status
python3 enigma.py status
```

**Requirements:**
- Subcommands: query, ingest, edit, status
- Proper error handling
- Progress indicators
- Logging to `logs/enigma.log`

---

### Task 11: Configuration File
**Time:** 15-20 minutes
**File:** `config/enigma_config.yaml`

**Purpose:** Centralize all settings.

**Settings:**
```yaml
ollama:
  base_url: http://localhost:11434
  model: qwen3:30b
  temperature: 0.7

chromadb:
  persist_directory: ./data/chromadb
  collection_name: enigma_knowledge

folders:
  ground_truth: 99_GroundTruth
  systems: 02_Systems
  projects: 03_Projects
  memory: 04_Memory
  derived: 06_Derived

logging:
  level: INFO
  file: logs/enigma.log
```

---

### Task 12: Documentation & Testing
**Time:** 20-30 minutes

**Create:**
1. `scripts/README.md` — Explains each script
2. `tests/test_basic.py` — Basic functionality tests
3. `logs/` folder for logging

**Test Suite Should Cover:**
- Document loading (all formats)
- Vector search (retrieval accuracy)
- Query interface (citation correctness)
- Word editing (improvement quality)

---

## VALIDATION CHECKLIST

Before considering Phase 1 complete, verify:

### Functional Tests
- [ ] Can query Ground Truth documents accurately
- [ ] Citations are correct (file:line_number format)
- [ ] No hallucinations (only uses Enigma folder content)
- [ ] Semantic search returns relevant results
- [ ] Word document editing works end-to-end
- [ ] Writing Standard enforcement catches issues
- [ ] All file formats readable (MD, TXT, DOCX, PDF)

### Quality Tests
- [ ] Responses match "Professional + Casual" tone
- [ ] No buzzwords in generated content
- [ ] Structure is always clear (headings, bullets)
- [ ] Uncertainty is explicitly stated
- [ ] Sources always cited

### Performance Tests
- [ ] Query response < 10 seconds
- [ ] Document ingestion reasonable (< 1 min for 10 docs)
- [ ] Editing a 5-page Word doc < 30 seconds

---

## PRIORITIES: What to Build First

Based on your top needs from questions.md Section 8:

### Priority 1: Product Genome Editor ⭐⭐⭐
**Why:** Your #1 project, biggest time sink
**Tasks:** 7, 8, 9 (Word editing automation)

### Priority 2: Query Interface ⭐⭐
**Why:** Foundation for everything else
**Tasks:** 2, 3, 6 (Basic query capabilities)

### Priority 3: Full Document Ingestion ⭐
**Why:** Enables institutional memory
**Tasks:** 4, 5 (Document loading + indexing)

### Priority 4: Unified CLI ⭐
**Why:** Better user experience
**Tasks:** 10, 11 (Integration + config)

---

## TIME ESTIMATES

**Minimum Viable Phase 1:**
- Checkpoints 1-3: 10 minutes
- Tasks 1-3: 1 hour
- Tasks 4-6: 2 hours
- **Total: ~3 hours for basic working system**

**Complete Phase 1 (with automation):**
- Above + Tasks 7-9: 3 hours
- Above + Tasks 10-12: 2 hours
- **Total: ~8 hours for full Phase 1**

---

## RECOMMENDED SEQUENCE

### Session 1 (Today, after download): Verify & Test
1. ✅ Checkpoint 1: Verify model
2. ✅ Checkpoint 2: Test model
3. ✅ Checkpoint 3: Verify API
4. Task 1: Install dependencies
5. Task 2: Simple query script
6. Task 3: Test Ground Truth reading

**Goal:** Confirm Enigma can read and use your doctrine.

---

### Session 2: Build Query Interface
1. Task 4: Document loader
2. Task 5: Semantic indexing
3. Task 6: Query interface

**Goal:** "Ask Enigma" works end-to-end.

---

### Session 3: Build Editor Automation
1. Task 7: Word document reader
2. Task 8: Writing standard enforcer
3. Task 9: Document refinement tool

**Goal:** Automate Product Genome editing (your #1 need).

---

### Session 4: Polish & Integration
1. Task 10: Unified CLI
2. Task 11: Configuration
3. Task 12: Documentation & testing

**Goal:** Production-ready Phase 1.

---

## SUCCESS CRITERIA

**Phase 1 is complete when:**

1. ✅ You can ask Enigma questions about your doctrine and get accurate, cited answers
2. ✅ Enigma only uses information from your Enigma folder (no hallucination)
3. ✅ You can point Enigma at a Word document and get it refined per your Writing Standard
4. ✅ All Ground Truth, Systems, and Project documents are indexed and searchable
5. ✅ Response tone matches "Professional + Casual" consistently
6. ✅ You use Enigma daily for Product Genome editing

---

## NEXT SESSION PREP

**Before starting Task 2 (Simple Query Script), have ready:**
1. Model download completed ✅
2. Python dependencies installed
3. Text editor open to Enigma folder
4. Terminal window ready

**Claude Code should:**
- Create `scripts/` folder
- Write initial Python scripts
- Test each component incrementally
- Show working examples

---

## NOTES & REMINDERS

- **No rushing:** Quality over speed (per your doctrine)
- **Test incrementally:** Verify each component before moving to next
- **Cite sources:** Every claim traceable to Enigma documents
- **Log everything:** All operations should be auditable
- **Ask if stuck:** Better to clarify than guess

---

**Status:** Ready to begin once model download completes
**Next Action:** Run Checkpoint 1 (Verify Model Installation)

---

**END OF NEXT STEPS**
