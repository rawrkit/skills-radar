# 🛰️ Skills Radar

A curated, weekly-updated catalog of **genuinely useful agent skills** — for Claude Code, Codex, Gemini CLI, and any agent that reads `SKILL.md`. No dumps of every repo on GitHub: every entry here was checked by a human, described in one honest line, and tagged by the Scrum role it helps.

**📬 Get the weekly digest:** hit **Watch → Custom → Releases** on this repo — GitHub will email you the top finds every week. Works for any team member, no signup, no bot.

## 🤖 For AI agents

**Install the search skill** and your agent will consult this catalog on its own whenever the user needs a skill:

```
npx -y skills add rawrkit/skills-radar@find-vetted-skill -y -g
```

If you are an AI agent looking for a skill for your user right now: fetch [`catalog.json`](catalog.json) — it is the machine-readable source of truth. Each entry has `id`, `source` (owner/repo), `url`, `category`, `installs`, `roles` (BA/PO/SM/DEV/QA/ALL), `status`, and descriptions in English and Russian. Statuses: `approved` (human-reviewed, good), `in-kit` (also bundled in a [role kit](https://github.com/rawrkit/role-kits)), `new` (found by the weekly scan, awaiting review), `rejected` (do not suggest). Install any entry with `npx -y skills add <source>@<id> -y -g`. To install a whole role bundle at once, use [role-kits](https://github.com/rawrkit/role-kits) instead.

## How entries get here

A weekly job scans [skills.sh](https://skills.sh), GitHub, and community lists for new skills, filters out junk (dead READMEs, spam authors, empty wrappers), and proposes candidates. A human reviews every candidate before it lands in the catalog. Statuses: `✅ approved` · `🆕 new this week` · `🎒 in a role kit`.

## Catalog

### 🧠 Decision quality

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [grill-me](https://skills.sh/mattpocock/skills/grill-me) + [grilling](https://skills.sh/mattpocock/skills/grilling) `mattpocock/skills` | Relentless one-question-at-a-time interview that stress-tests your plan, decision, or idea before you commit to it | ALL | 730K |
| [council](https://skills.sh/warpdotdev/common-skills/council) `warpdotdev/common-skills` | Karpathy-style LLM Council: several agents (different models when available, different perspectives otherwise) investigate the same question independently, cross-review, then synthesize one recommendation | BA, PO, DEV | 16.3K |
| [idea-refine](https://skills.sh/addyosmani/agent-skills/idea-refine) `addyosmani/agent-skills` | Refines raw ideas into a sharp one-pager via divergent/convergent thinking | ALL | 16.2K |
| [llm-council](https://github.com/okjpg/llm-council) `okjpg` | 5 AI advisors debate your decision with peer review and synthesis — closest to Karpathy's original methodology | BA, PO | — |
| [judge-with-debate](https://skills.sh/neolabhq/context-engineering-kit/judge-with-debate) `neolabhq/context-engineering-kit` | Structured judge + debate loop for evaluating outputs before shipping them | QA, DEV | 947 |

### 🗣️ Communication

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [empathy-in-action](https://github.com/rawrkit/empathy-in-action) `rawrkit` | Empathy through action, not words: the assistant picks up the rational load when emotions block reason — mirrors the user's register, never fakes capabilities, ticking-clock mode for live incidents | ALL | new |
| [read-the-room](https://github.com/rawrkit/read-the-room) `rawrkit` | Reads memes and slang as real instructions — nine speech acts, honest about references it doesn't know, and the task still gets done | ALL | new |
| [caveman](https://github.com/JuliusBrussee/caveman) `JuliusBrussee` | Caveman-speak compression: ~65% fewer output tokens, full technical accuracy kept | ALL | 805+ |
| [negotiation-voss-tactical-empathy](https://skills.sh/santos-sanz/lifeskills/negotiation-voss-tactical-empathy) `santos-sanz/lifeskills` | Chris Voss negotiation techniques (tactical empathy, calibrated questions) applied to your negotiation prep | PO, SM | 43 |

### 📋 Discovery & requirements

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [empathy-map](https://skills.sh/owl-listener/designer-skills/empathy-map) `owl-listener/designer-skills` | Builds a UX empathy map (says/thinks/does/feels) from your user research notes | BA, PO | 943 |
| [customer-empathy](https://skills.sh/rameerez/claude-code-startup-skills/customer-empathy) `rameerez/claude-code-startup-skills` | Digs into customer pains and jobs-to-be-done before you commit to building | PO, BA | 108 |

### 📝 Requirements & stories

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [meeting-notes](https://skills.sh/claude-office-skills/skills/meeting-notes) `claude-office-skills` | Meeting transcripts into structured notes, decisions, and action items | BA, SM | 4.4K |
| [user-story](https://skills.sh/deanpeters/product-manager-skills/user-story) `deanpeters/product-manager-skills` | User stories in Mike Cohn format with Gherkin acceptance criteria | BA, PO | 3.1K |
| [requirements-analysis](https://skills.sh/jwynia/agent-skills/requirements-analysis) `jwynia/agent-skills` | Diagnoses requirements problems: separates stated wants from real needs and constraints | BA | 2.2K |
| [user-story-splitting](https://skills.sh/deanpeters/product-manager-skills/user-story-splitting) `deanpeters/product-manager-skills` | Splits oversized stories/epics using proven split patterns | BA, PO | 1.9K |
| [requirements-clarity](https://skills.sh/softaworks/agent-toolkit/requirements-clarity) `softaworks/agent-toolkit` | Vague request → actionable PRD via YAGNI/KISS questioning | BA | 726 |
| [deliver-acceptance-criteria](https://skills.sh/product-on-purpose/pm-skills/deliver-acceptance-criteria) `product-on-purpose/pm-skills` | Given/When/Then criteria: happy path, failures, non-functional | BA, QA | 667 |
| [drawio-bpmn](https://skills.sh/sparklabx/drawio-ai-kit/drawio-bpmn) `sparklabx/drawio-ai-kit` | BPMN swimlane diagrams in draw.io with validation (needs drawio-ai CLI) | BA | 155 |
| 🆕 [create-github-issues-for-unmet-specification-requirements](https://skills.sh/github/awesome-copilot/create-github-issues-for-unmet-specification-requirements) `github/awesome-copilot` | Reads a spec file, checks what's already implemented, files one GitHub Issue per unmet requirement — dedups against existing issues | BA, PO | 8.9K |

### 📊 Product & planning

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [roadmap-planning](https://skills.sh/deanpeters/product-manager-skills/roadmap-planning) `deanpeters/product-manager-skills` | Strategy → outcome-driven roadmap: prioritization, epics, stakeholder alignment, sequencing | PO | 2.9K |
| [prioritization-advisor](https://skills.sh/deanpeters/product-manager-skills/prioritization-advisor) `deanpeters/product-manager-skills` | Picks the right prioritization framework (RICE/ICE/value-effort) for your stage | PO | 2.1K |
| [user-story-mapping](https://skills.sh/deanpeters/product-manager-skills/user-story-mapping) `deanpeters/product-manager-skills` | Story mapping: from user journey to release slices | PO, BA | 2K |
| [iterate-retrospective](https://skills.sh/product-on-purpose/pm-skills/iterate-retrospective) `product-on-purpose/pm-skills` | Facilitates and documents retros: went well / improve / action items | SM | 493 |
| 🆕 [scrum-master](https://skills.sh/alirezarezvani/claude-skills/scrum-master) `alirezarezvani/claude-skills` | Data-driven Scrum coaching: Python scripts for Monte Carlo velocity forecasting, sprint health scoring, retro theme tracking from Jira-style exports | SM | 775 |
| 🆕 [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) `anthropics` | Official Anthropic plugin marketplace (11 plugins, 23K★): skills + MCP connectors + slash commands per role, incl. product-management (sprint-planning, roadmap-update, write-spec) and engineering (code-review, testing-strategy, incident-response) | ALL | — |

### 🧪 QA & testing

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [qa-test-planner](https://skills.sh/softaworks/agent-toolkit/qa-test-planner) `softaworks/agent-toolkit` | Test plans, manual cases, regression suites, bug reports | QA | 4.1K |
| [accessibility-test-plan](https://skills.sh/owl-listener/designer-skills/accessibility-test-plan) `owl-listener/designer-skills` | Accessibility test plan for UI features | QA | 989 |
| 🆕 [webapp-testing](https://skills.sh/anthropics/skills/webapp-testing) `anthropics/skills` | Official Anthropic skill: Playwright-driven testing of local web apps — screenshots, DOM inspection, browser console logs | QA, DEV | 129.2K |
| 🆕 [browser-testing-with-devtools](https://skills.sh/addyosmani/agent-skills/browser-testing-with-devtools) `addyosmani/agent-skills` | Chrome DevTools MCP bridge: inspect the DOM, read console errors, analyze network requests, profile Core Web Vitals, verify a fix live instead of guessing (needs chrome-devtools MCP server) | QA, DEV | 20.2K |

### 📣 Marketing & growth

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [seo-audit](https://skills.sh/coreyhaines31/marketingskills/seo-audit) `coreyhaines31/marketingskills` | Full technical + content SEO audit | ALL | 177K |
| [programmatic-seo](https://skills.sh/coreyhaines31/marketingskills/programmatic-seo) `coreyhaines31/marketingskills` | Template-driven pages at scale without thin-content penalties | ALL | 112K |
| [ai-seo](https://skills.sh/coreyhaines31/marketingskills/ai-seo) `coreyhaines31/marketingskills` | Ranking in AI answers (LLM search, AI Overviews) | ALL | 101K |
| [seo](https://skills.sh/addyosmani/web-quality-skills/seo) `addyosmani/web-quality-skills` | On-page and technical SEO quality from the Chrome team | ALL | 36.8K |
| [marketing-council](https://skills.sh/coreyhaines31/marketingskills/marketing-council) `coreyhaines31/marketingskills` | Council of marketing perspectives deliberating your strategy question | ALL | 12.1K |
| [affiliate-marketing](https://skills.sh/kostja94/marketing-skills/affiliate-marketing) `kostja94/marketing-skills` | CPS affiliate program strategy: commissions, recruitment, tracking | ALL | 921 |
| [google-ads](https://skills.sh/arnabbagxd/brand-building-skills/google-ads) `arnabbagxd/brand-building-skills` | Deep Google Ads: Search/PMax/Shopping/YouTube, Quality Score, ROAS | ALL | 601 |

**Collections powering the [role kits](https://github.com/rawrkit/role-kits):** [marketingskills](https://github.com/coreyhaines31/marketingskills) (49 skills, Corey Haines), [salesskills](https://github.com/louisblythe/salesskills) (120+ sales & conversation skills), [designer-skills](https://github.com/owl-listener/designer-skills) (~100 design skills).

### 🛠️ Engineering

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [code-review](https://skills.sh/mattpocock/skills/code-review) `mattpocock/skills` | Two-axis review (repo standards + spec compliance) in parallel sub-agents | DEV | 230K |
| [systematic-debugging](https://skills.sh/obra/superpowers/systematic-debugging) `obra/superpowers` | Root cause before fixes, always — symptom patches are failure | DEV | 210K |
| [react-best-practices](https://skills.sh/vercel-labs/agent-skills/react-best-practices) `vercel-labs/agent-skills` | React/Next.js performance guidelines straight from Vercel engineering | DEV | 185K |
| [document skills](https://github.com/anthropics/skills) `anthropics/skills` | Official Anthropic skills for producing real .docx / .xlsx / .pptx / .pdf artifacts | ALL | 100K+ |
| [skill-creator](https://github.com/anthropics/skills) `anthropics/skills` | Meta-skill: builds new skills with test runs, benchmarks, and an iteration loop — how the skills in this catalog get made | ALL | 100K+ |
| 🆕 [planning-with-files](https://skills.sh/othmanadi/planning-with-files/planning-with-files) `othmanadi/planning-with-files` | Manus-style persistent planning: task_plan.md/findings.md/progress.md on disk so multi-step work survives /clear and context loss | DEV | 39.8K |
| 🆕 [code-review-excellence](https://skills.sh/wshobson/agents/code-review-excellence) `wshobson/agents` | Code review as knowledge-sharing, not gatekeeping: constructive-feedback patterns, review standards, mentoring through PRs | DEV | 26.3K |
| 🆕 [documentation-writer](https://skills.sh/github/awesome-copilot/documentation-writer) `github/awesome-copilot` | Technical documentation structured with the Diátaxis framework — tutorials, how-to, reference, explanation | DEV | 24.4K |
| 🆕 [context-engineering](https://skills.sh/addyosmani/agent-skills/context-engineering) `addyosmani/agent-skills` | Curates what an agent sees and when: rules files, context handoffs, diagnosing output degradation from context overload | DEV, ALL | 19.1K |
| 🆕 [context7-mcp](https://skills.sh/upstash/context7/context7-mcp) `upstash/context7` | Fetches current library/framework docs via the Context7 MCP server instead of relying on stale training data — triggers on framework mentions and library-specific code requests (needs context7 MCP server) | DEV | 4.1K |

### 🖥️ Infrastructure

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [azure-kubernetes](https://skills.sh/microsoft/azure-skills/azure-kubernetes) `microsoft/azure-skills` | Official Microsoft AKS skill — the most-installed infrastructure skill in the ecosystem | DEV | 322K |
| [kubernetes-specialist](https://skills.sh/jeffallan/claude-skills/kubernetes-specialist) `jeffallan/claude-skills` | Vendor-neutral K8s: manifests, Helm, RBAC, NetworkPolicies, GitOps, pod debugging | DEV | 11.8K |
| [dt-obs-kubernetes](https://skills.sh/dynatrace/dynatrace-for-ai/dt-obs-kubernetes) `dynatrace/dynatrace-for-ai` | Kubernetes observability via Dynatrace | DEV | 1.4K |
| [terraform-infrastructure-as-code](https://skills.sh/manutej/luxor-claude-marketplace/terraform-infrastructure-as-code) `manutej/luxor-claude-marketplace` | Terraform IaC: modules, state, plans, reviews | DEV | 312 |

### 🔐 Security

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [anthropic-cybersecurity-skills](https://github.com/mukul975/anthropic-cybersecurity-skills) `mukul975` | Huge security collection (27K★): threat modeling, secret scanning, hardening, forensics, incident response. The [security kit](https://github.com/rawrkit/role-kits) bundles the **defensive** subset only | DEV | 27K★ |
| implementing-threat-modeling-with-mitre-attack `mukul975` | Threat modeling mapped to MITRE ATT&CK tactics and techniques | DEV | — |
| implementing-secret-scanning-with-gitleaks `mukul975` | Catch leaked credentials in repos before attackers do | DEV | — |
| auditing-mcp-servers-for-tool-poisoning `mukul975` | AI-era attack surface: audit MCP servers for tool poisoning | DEV | — |

### 📈 Data & hiring

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [xlsx](https://github.com/anthropics/skills) `anthropics/skills` | Official skill for creating and editing real .xlsx spreadsheets | ALL | 100K+ |
| [job-description-generator](https://skills.sh/claude-office-skills/skills/job-description-generator) `claude-office-skills` | Quick job description drafts from a role outline | ALL | 3.6K |
| [data-analysis](https://skills.sh/bytedance/deer-flow/data-analysis) `bytedance/deer-flow` | DuckDB-powered Excel/CSV analysis: schema, SQL, stats, pivots, exports | PO, QA | 2.9K |
| [writing-job-descriptions](https://skills.sh/refoundai/lenny-skills/writing-job-descriptions) `refoundai/lenny-skills` | JDs that attract the right people instead of listing 20 requirements | ALL | 1.6K |
| [interviewing-evaluating-candidates](https://skills.sh/refoundai/lenny-skills/interviewing-evaluating-candidates) `refoundai/lenny-skills` | High-signal interviews: agency and craft over charisma and pedigree | ALL | — |

### 🧰 Memory & context

| Skill | What it actually does | Roles | Installs |
|---|---|---|---|
| [agentmemory](https://github.com/rohitg00/agentmemory) `rohitg00` | 15 persistent-memory skills (remember / recall / handoff / commit-context) so your agent survives session restarts | ALL | — |
| 🆕 [memory-merger](https://skills.sh/github/awesome-copilot/memory-merger) `github/awesome-copilot` | Consolidates mature lessons from a scratch memory file into the permanent instruction file, scoped global/user/workspace | ALL | 12.7K |

## Role kits

Skills from this catalog are assembled into installable **role kits** for Scrum teams — one command installs the whole set for your role, on any agent: [rawrkit/role-kits](https://github.com/rawrkit/role-kits). **All kits are live**: `base` (universal AI-usage core), `ba`, `po`, `sm`, `dev`, `qa`.

## Contributing

Found a skill that deserves a spot? Open an issue with the link and one line on why it's genuinely useful. "It exists" is not a reason; "it saved me an hour this week" is.

## License

MIT — the catalog data (`catalog.json`) is free to reuse.
