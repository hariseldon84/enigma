# ENIGMA — Personal Cognitive Operating System

**Version:** 0.1 (Foundation Phase)
**Owner:** Anand Arora
**Status:** Active Development - Phase 1 (Enigma Brain)
**Last Updated:** 2026-01-10

---

## WHAT IS ENIGMA?

Enigma is not a chatbot.
Enigma is not an AI assistant.
Enigma is not a productivity app.

**Enigma is a local, offline-capable cognitive operating system** — a personal intelligence substrate that operates as a governed system layer on top of macOS.

### Core Purpose

Enigma exists to serve **four functions only:**

1. **Cognitive Augmentation** — Thinking, synthesis, planning, structuring, writing
2. **Institutional Memory** — Long-term recall of systems, projects, decisions, and doctrine
3. **Execution Support** — Controlled operation of files, documents, workflows, and tools
4. **System Intelligence** — Active use of personal principles, systems, and constraints

---

## WHY ENIGMA EXISTS

Most AI systems fail because they have **capability without governance**. They are powerful but:
- Drift over time
- Hallucinate without constraint
- Lack institutional memory
- Have no boundaries or doctrine
- Cannot be trusted with long-term cognitive partnership

**Enigma is different.** It is built **constitution-first, capabilities-second.**

It operates under strict laws that define:
- What it may know
- What it may remember
- What it may assume
- What it may modify
- What it may execute

This makes Enigma:
- **Trustworthy** (operates within known boundaries)
- **Stable** (does not drift or corrupt knowledge)
- **Scalable** (can grow without collapsing)
- **Auditable** (all actions logged and explainable)
- **Aligned** (continuously matches personal doctrine)

---

## SYSTEM ARCHITECTURE

Enigma is composed of **four core layers:**

```
You (Command)
   ↓
Enigma Controller (the brainstem)
   ↓
┌──────────────────────────────────────────┐
│           Cognitive Core                 │
│  (Local LLM + Reasoning + Planning)      │
└──────────────────────────────────────────┘
   ↓
┌──────────────────────────────────────────┐
│        Knowledge & Memory Engine         │
│ (Indexing, Retrieval, Versioned Memory) │
└──────────────────────────────────────────┘
   ↓
┌──────────────────────────────────────────┐
│          Action & Tool Layer             │
│ (Mac automation, web, documents, files) │
└──────────────────────────────────────────┘
   ↓
macOS, Filesystem, Apps, Browser
```

### Layer Responsibilities

**1. Enigma Controller (The Brainstem)**
- Parses intent
- Assembles context from Enigma folder
- Plans execution
- Calls tools
- Verifies outputs
- Prevents hallucination

**2. Cognitive Core (Local Intelligence)**
- Reasoning and planning
- Writing and English refinement
- Summarization and synthesis
- Interprets instructions
- **Does NOT** touch files directly or browse

**3. Knowledge & Memory Engine**
- Document ingestion (PDF, DOCX, MD, images)
- Semantic search (vector database)
- Structured memory (SQLite/DuckDB)
- Versioning and metadata
- Cross-project linking

**4. Action & Tool Layer**
- File operations (read, write, organize)
- macOS automation (apps, workflows)
- Browser automation (data capture)
- Document generation (reports, briefs)
- Background scheduling

---

## THE ENIGMA CONSTITUTION

Enigma operates under **10 Constitutional Articles** (see `99_GroundTruth/Enigma_Constitution.md`).

### The Four Layers of Knowledge

All knowledge in Enigma is classified into **four layers** with different trust levels and mutability rules:

#### **LAYER 1: Ground Truth (Immutable)**
- **Folder:** `99_GroundTruth/`
- **Contents:** Core principles, personal doctrine, system blueprints, canonical definitions
- **Rules:** Cannot be modified or contradicted by Enigma. All reasoning defers to this.
- **This is Enigma's constitution, not its memory.**

#### **LAYER 2: Structured Reality (High Trust)**
- **Folders:** `02_Systems/`, `04_Memory/Decisions/`
- **Contents:** Systems documentation, project maps, decisions & rationales, operating procedures
- **Rules:** Modifiable only with explicit approval. Always cited in outputs.
- **This is Enigma's institutional memory.**

#### **LAYER 3: Working Knowledge (Evolving)**
- **Folders:** `01_Skills_And_Education/`, `03_Projects/`, `05_Tasks/`
- **Contents:** Notes, research, drafts, proposals, chat histories, experiments
- **Rules:** Freely writable and summarizable. Never silently promoted to Layer 1 or 2.
- **This is Enigma's mind.**

#### **LAYER 4: Derived Intelligence (Generated)**
- **Folder:** `06_Derived/`
- **Contents:** Reports, briefs, plans, syntheses, drafts, analyses
- **Rules:** Never treated as truth by default. Never auto-fed back as knowledge.
- **This is Enigma's speech.**

---

## FOLDER STRUCTURE

```
Enigma/
├── 00_Doctrine/              # Identity, philosophies, behavioral codes
├── 01_Skills_And_Education/  # Learning resources, books, research
├── 02_Systems/               # System documentation, processes, frameworks
│   └── Systems_Map.md        # Map of all major systems and how they relate
├── 03_Projects/              # Active projects, proposals, working notes
│   └── Active_Projects_Index.md  # Current project status and priorities
├── 04_Memory/
│   ├── Decisions/            # Decision logs with rationale
│   │   └── Master_Decision_Log.md
│   ├── Learnings/            # Distilled insights and patterns
│   │   └── Learning_Log.md
│   └── Experiments/          # Hypotheses and results
├── 05_Tasks/                 # Task lists, automation instructions, workflows
├── 06_Derived/               # Enigma-generated reports, briefs, analyses
├── 99_GroundTruth/           # Immutable principles, doctrine, constitution
│   ├── Personal_Doctrine.md  # Non-negotiable principles and identity
│   ├── Enigma_Constitution.md # Constitutional framework
│   └── Writing_Standard.md   # Voice, tone, and communication principles
├── CLAUDE.md                 # Guide for Claude Code instances
├── scope.md                  # Project scope and vision
├── questions.md              # Interactive questionnaire (working document)
└── README.md                 # This file
```

---

## THE SEVEN SEED DOCUMENTS

Enigma's foundation is built on **seven seed documents** that define identity, law, memory, and reality:

### Ground Truth (Layer 1)
1. **Personal_Doctrine.md** — Non-negotiable principles, thinking style, decision filters, identity
2. **Enigma_Constitution.md** — Constitutional framework, knowledge layers, source sovereignty
3. **Writing_Standard.md** — Voice, tone, banned words, editing mandate

### Structured Reality (Layer 2)
4. **Systems_Map.md** — All major systems, four-layer architecture, compounding loops
5. **Master_Decision_Log.md** — Decision tracking with context, rationale, risks, outcomes
6. **Learning_Log.md** — Distilled insights that change behavior

### Working Knowledge (Layer 3)
7. **Active_Projects_Index.md** — Current projects with objectives, constraints, priorities

**These documents are not notes. They are constitutional infrastructure.**

---

## TECHNOLOGY STACK

### Cognitive Core
- **Ollama** (local model runner)
- **Model:** Qwen3:30b (strong reasoning, excellent writing, good balance)

### Knowledge & Memory
- **Ingestion:** Unstructured, Apache Tika, Tesseract OCR
- **Orchestration:** LlamaIndex
- **Vector Store:** Qdrant (local mode) or Chroma
- **Structured Memory:** SQLite / DuckDB

### Controller
- **Language:** Python
- **Frameworks:** LangGraph (multi-step planning), Pydantic (schemas), FastAPI (local API)

### Action & Automation
- **macOS Control:** AppleScript, Shortcuts, pyobjc
- **Browser Automation:** Playwright
- **Document Handling:** python-docx, pdfplumber, pymupdf, openpyxl
- **File Operations:** Native Python, Watchdog (folder monitoring)

### Interface
- **Current:** CLI + command palette
- **Future:** Local web app or Mac-native (Tauri/Electron)

---

## DEVELOPMENT PHASES

### Phase 1: Enigma Brain (Offline Thinking Partner)
**Status:** 🔄 IN PROGRESS

**Goals:**
- Local AI reads Enigma folder exclusively
- Answers questions, improves English
- Writes documents, summarizes, creates structured outputs
- Trustworthy private intelligence

**Deliverables:**
- Document ingestion pipeline
- Semantic search (vector database)
- Basic query interface
- English refinement capabilities

---

### Phase 2: Enigma Memory (Semantic Knowledge System)
**Status:** ⏳ PLANNED

**Goals:**
- Automatic ingestion of all new content
- Deep semantic retrieval
- Cross-project understanding
- Persistent long-term context
- External long-term memory

**Deliverables:**
- Folder watchers
- Automatic indexing
- Timeline memory
- Pattern recognition

---

### Phase 3: Enigma Operator (Mac Automation)
**Status:** ⏳ PLANNED

**Goals:**
- File operations and organization
- Document generation
- Research capture
- Controlled browsing
- Repeatable workflows
- Execution assistant

**Deliverables:**
- File automation tools
- Browser automation
- Report generation
- Scheduled tasks

---

### Phase 4: Enigma System Intelligence (Cognitive OS)
**Status:** ⏳ PLANNED

**Goals:**
- Personalities & principles become operating constraints
- Systems become active frameworks
- Culture becomes decision logic
- Goals drive task creation
- True personal operating system

**Deliverables:**
- Multi-agent coordination
- Proactive task generation
- System-wide optimization
- Full cognitive partnership

---

## WHAT MAKES ENIGMA DIFFERENT

Most "local AI" setups are: **model + chat + documents**

Enigma is:
- **Doctrine-driven** — Operates within constitutional boundaries
- **Memory-structured** — Four-layer knowledge hierarchy with strict sovereignty
- **System-integrated** — Deep macOS integration for automation
- **Execution-capable** — Can act on the world, not just respond
- **Auditable** — All actions logged, replayable, explainable
- **Aligned** — Continuously matches personal doctrine and goals

---

## KEY PRINCIPLES

### 1. Constitution Before Capability
Structure and governance come before features. This prevents drift and ensures reliability.

### 2. Source Sovereignty
Every factual answer must be traceable. No hallucinations. No silent knowledge.

### 3. Layer Discipline
Knowledge layers have strict boundaries. Layer 1 cannot be modified. Layer 4 is never treated as truth.

### 4. Architecture-First
Design structure before iteration. Systems must be intentionally designed.

### 5. Quality Over Speed
"Good enough" means finished work, not POC. Quality is non-negotiable.

### 6. Auditability Always
Everything logged, replayable, and explainable. No silent evolution.

### 7. No Dependency
Enigma augments, it does not replace. User sovereignty is maintained.

---

## SETUP INSTRUCTIONS

### Prerequisites
- macOS (tested on macOS 13+)
- Ollama installed
- Python 3.8+ installed
- At least 20GB free disk space (for models)

### Initial Setup

#### 1. Install Ollama
```bash
# If not already installed, download from https://ollama.com
# Or use Homebrew:
brew install ollama
```

#### 2. Download Model
```bash
ollama pull qwen3:30b
```

#### 3. Install Python Dependencies
```bash
pip3 install ollama chromadb llama-index python-docx pymupdf pdfplumber openpyxl watchdog
```

#### 4. Verify Ollama API
```bash
curl http://localhost:11434/api/tags
```

#### 5. Clone or Create Enigma Folder Structure
The folder structure should already exist. If not, run:
```bash
mkdir -p Enigma/{00_Doctrine,01_Skills_And_Education,02_Systems,03_Projects,04_Memory/{Decisions,Learnings,Experiments},05_Tasks,06_Derived,99_GroundTruth}
```

---

## USAGE

### Query Enigma (Coming Soon - Phase 1)
```bash
python enigma_query.py "What are my core principles?"
```

### Ingest New Documents (Coming Soon - Phase 1)
```bash
python enigma_ingest.py --folder 01_Skills_And_Education
```

### Edit Document (Coming Soon - Phase 1)
```bash
python enigma_edit.py --file "path/to/document.docx" --mode refine
```

### Run Background Watcher (Coming Soon - Phase 2)
```bash
python enigma_watch.py
```

---

## CURRENT STATUS

### ✅ Completed
- [x] Folder structure established
- [x] Seven seed documents created and populated
- [x] Personal Doctrine formalized (10 sections)
- [x] Enigma Constitution documented
- [x] Systems Map created (9 major systems)
- [x] Writing Standard defined
- [x] Active Projects indexed
- [x] Decision and Learning logs templated
- [x] Ollama installed
- [x] Model (qwen3:30b) downloading

### 🔄 In Progress
- [ ] Model download (qwen3:30b - 17.3 GB)
- [ ] Basic query interface
- [ ] Document ingestion pipeline

### ⏳ Next Up
- [ ] Test model with Enigma-specific prompts
- [ ] Build Python controller scripts
- [ ] Implement semantic search
- [ ] Create Product Genome editing assistant (top priority automation)

---

## DEVELOPMENT ROADMAP

### Week 1-2: Foundation
- [x] Constitutional documents
- [ ] Basic Ollama integration
- [ ] Simple query interface
- [ ] Ground Truth document ingestion

### Week 3-4: Intelligence
- [ ] Vector database setup (Chroma)
- [ ] Semantic search implementation
- [ ] Document summarization
- [ ] English refinement testing

### Month 2: Memory
- [ ] Full folder ingestion
- [ ] Folder watchers
- [ ] Timeline memory
- [ ] Cross-document linking

### Month 3: Automation
- [ ] Product Genome editing assistant
- [ ] File organization automation
- [ ] Email management
- [ ] Information capture workflows

---

## IMPORTANT FILES

### Entry Points
- **README.md** (this file) — System overview and documentation
- **scope.md** — Complete project scope, vision, and technical blueprint
- **CLAUDE.md** — Guide for Claude Code instances working in this repository

### Constitutional Documents
- **99_GroundTruth/Personal_Doctrine.md** — Identity and principles
- **99_GroundTruth/Enigma_Constitution.md** — System laws and boundaries
- **99_GroundTruth/Writing_Standard.md** — Communication principles

### System Reality
- **02_Systems/Systems_Map.md** — How all systems relate
- **03_Projects/Active_Projects_Index.md** — Current project status

### Memory Infrastructure
- **04_Memory/Decisions/Master_Decision_Log.md** — Decision tracking
- **04_Memory/Learnings/Learning_Log.md** — Insight accumulation

### Working Documents
- **questions.md** — Interactive questionnaire (temporary, for building)

---

## CONTRIBUTION GUIDELINES

This is a **personal system**, not an open-source project. However, if you are:
- A future instance of Claude Code working in this repository
- A collaborator with explicit permission
- The owner (Anand Arora)

Follow these principles:

### 1. Read Constitution First
Never modify or suggest changes without reading:
- Personal_Doctrine.md
- Enigma_Constitution.md
- Writing_Standard.md

### 2. Respect Layer Boundaries
- **Layer 1 (Ground Truth):** Never modify without explicit owner approval
- **Layer 2 (Structured Reality):** Suggest changes, don't auto-apply
- **Layer 3 (Working Knowledge):** Freely add and organize
- **Layer 4 (Derived):** Generate freely, but never treat as truth

### 3. Cite Sources Always
Every claim must be traceable to a document in Enigma folder.

### 4. Follow Writing Standard
All outputs must match the Professional + Casual voice. No buzzwords, no fluff, no corporate speak.

### 5. Quality Over Speed
Finished work only. No POC-level contributions.

---

## TROUBLESHOOTING

### Ollama Not Responding
```bash
# Restart Ollama service
ollama serve

# Or check if it's running
ps aux | grep ollama
```

### Model Not Found
```bash
# List installed models
ollama list

# Re-download if needed
ollama pull qwen3:30b
```

### Python Dependencies Missing
```bash
# Reinstall all dependencies
pip3 install --upgrade ollama chromadb llama-index python-docx pymupdf pdfplumber openpyxl watchdog
```

### Permission Denied Errors
```bash
# Ensure Enigma folder has correct permissions
chmod -R u+rw ~/Enigma
```

---

## SUPPORT & CONTACT

**Owner:** Anand Arora
**Email:** [To be added if needed]
**Project Started:** 2026-01-10
**Repository Location:** `/Users/anandarora/Enigma/`

---

## LICENSE

**Private Project — All Rights Reserved**

This is a personal cognitive operating system. Not for public distribution or commercial use.

---

## APPENDIX: KEY INSIGHTS FROM FOUNDATION PHASE

### 1. Architecture-First Validated
User's natural approach is structure before speed—perfectly aligned with constitutional design.

### 2. Compounding Systems Thinking
All systems designed as organs of a larger organism, not independent businesses.

### 3. Quality Obsession
"Good enough" = finished work, not POC. This makes Enigma powerful but slower to build initially.

### 4. Billion-Dollar Filter
Everything must scale massively or it's a distraction. Clear decision filter.

### 5. Solo Deep Work
Best work done alone. Enigma must be autonomous assistant, not collaborative tool.

### 6. Gut + Data Decision Making
Intuition first, data second. Enigma should make best guesses, not refuse to answer.

### 7. Professional + Casual Voice
Direct, structured, zero fluff. All Enigma outputs must match this standard.

---

## VERSION HISTORY

**v0.1 (2026-01-10)** - Foundation Phase
- Folder structure established
- Seven seed documents created
- Constitutional framework documented
- Ollama setup initiated
- Phase 1 development beginning

---

**END OF README**

*Last Updated: 2026-01-10*
*Status: Living Document — Will evolve as Enigma develops*
