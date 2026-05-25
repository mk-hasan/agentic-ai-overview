#!/usr/bin/env python3
"""Generate Bangla (bn) translations for pattern and example documentation."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANG_BN = "> [English]({en}) | **বাংলা**\n\n"

PATTERN_READMES: dict[str, str] = {
    "01-react": """# ReAct (Reason + Act)

## এটি কী

এজেন্ট **যুক্তি** (পরবর্তী ধাপ পরিকল্পনা) ও **কাজ** (টুল/API) এর মধ্যে বদলায়, **পর্যবেক্ষণ** করে, লক্ষ্য না হওয়া পর্যন্ত পুনরাবৃত্তি।

## কখন ব্যবহার

- অনেক ধাপ, বাহ্যিক feedback (search, API)।
- ধাপে ধাপে ব্যাখ্যাযোগ্য আচরণ।
- টুল-ব্যবহারকারী এজেন্টের ডিফল্ট লুপ।

## কখন নয়

- এক-shot Q&A, টুল নেই।
- কঠোর latency — planning overhead বেশি।

## কাঠামো

```
Thought → Action → Observation → Thought → … → Final Answer
```

## সম্পর্কিত প্যাটার্ন

- [Tool Use](../02-tool-use/)
- [Planning](../03-planning/)
- [Evaluator–Optimizer](../08-evaluator-optimizer/)

## উদাহরণ

[`example/`](example/) — LangGraph ReAct (IT helpdesk: FAQ + ticket)।

`python patterns/01-react/example/main.py`

## বাস্তব use case

[`use-case.bn.md`](use-case.bn.md) — [IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md)।
""",
    "02-tool-use": """# Tool Use / Function Calling

## এটি কী

মডেল **ঘোষিত টুল** থেকে বেছে structured arguments দেয়; runtime টুল চালিয়ে ফল মডেলে ফেরত দেয়।

## কখন ব্যবহার

- লাইভ ডেটা (CRM, ticket)।
- side effect: email, ticket, query।
- ReAct/planner-এ structured action।

## কখন নয়

- শুধু টেক্সট জেনারেশন।
- unstable tool schema।

## সম্পর্কিত

- [ReAct](../01-react/), [Routing](../05-routing/), [Guardrails](../12-guardrails/)

## উদাহরণ

[`example/`](example/) — `python patterns/02-tool-use/example/main.py`

[`use-case.bn.md`](use-case.bn.md)
""",
    "03-planning": """# Planning & Task Decomposition

## এটি কী

কাজের **উপ-কাজে ভাঙা** (plan), ক্রমে execution — ব্যর্থ হলে replan।

## কখন ব্যবহার

- বহু-ধাপ প্রজেক্ট, dependency গুরুত্বপূর্ণ।
- wasted tool call কমাতে upfront structure।

## কখন নয়

- এক-টুল lookup।
- plan দ্রুত stale হয় এমন environment।

## সম্পর্কিত

- [ReAct](../01-react/), [Orchestrator–Workers](../07-orchestrator-workers/), [Map–Reduce](../14-map-reduce/)

## উদাহরণ

`python patterns/03-planning/example/main.py` — [`use-case.bn.md`](use-case.bn.md)
""",
    "04-prompt-chaining": """# Prompt Chaining

## এটি কী

**নির্দিষ্ট LLM ধাপের ধারা** — প্রতিটি output পরের input; dynamic branching নেই।

## কখন ব্যবহার

- extract → transform → summarize।
- প্রতি stage আলাদা prompt, সহজ test/observe।

## কখন নয়

- intermediate result অনুযায়ী path ([Routing](../05-routing/))।
- parallel speed ([Parallelization](../06-parallelization/))।

## উদাহরণ

`python patterns/04-prompt-chaining/example/main.py`
""",
    "05-routing": """# Routing

## এটি কী

**রাউটার/ক্লাসifier** intent/metadata অনুযায়ে handler, prompt, বা টুল সেটে পাঠায়।

## কখন ব্যবহার

- এক entry, বিভিন্ন request type।
- route অনুযায়ী model/SLA।
- capability separation।

## উদাহরণ

`python patterns/05-routing/example/main.py` — VPN / identity / email handlers।
""",
    "06-parallelization": """# Parallelization

## এটি কী

**স্বাধীন উপ-কাজ সমান্তরাল**, তারপর merge — latency কমায় parallel কাজে।

## কখন ব্যবহার

- অনেক document summarize, একসাথে API।
- fan-out research।

## কখন নয়

- sequential dependency।
- strict token budget — cost গুণ হয়।

## সম্পর্কিত

- [Map–Reduce](../14-map-reduce/), [Orchestrator–Workers](../07-orchestrator-workers/)

## উদাহরণ

`python patterns/06-parallelization/example/main.py`
""",
    "07-orchestrator-workers": """# Orchestrator–Workers (Multi-Agent)

## এটি কী

**কেন্দ্রীয় orchestrator** কাজ ভেঙে **বিশেষজ্ঞ worker**-দের দেয়; synthesize করে unified output।

## কখন ব্যবহার

- legal + finance + engineering একসাথে।
- role boundary ও audit trail।
- monolithic prompt-এ ধরা যায় না এমন কাজ।

## সম্পর্কিত

- [Planning](../03-planning/), [Handoff](../13-handoff/), [Parallelization](../06-parallelization/)

## উদাহরণ

`python patterns/07-orchestrator-workers/example/main.py` — supervisor + VPN/identity/email specialists।
""",
    "08-evaluator-optimizer": """# Evaluator–Optimizer (Reflection)

## এটি কী

Draft → **evaluate** (criteria/rules) → **revise** loop — threshold বা max iteration পর্যন্ত।

## কখন ব্যবহার

- উচ্চ মানের writing/code।
- measurable rubric।
- human ছাড়া self-correction।

## সম্পর্কিত

- [HITL](../09-human-in-the-loop/), [Guardrails](../12-guardrails/), [ReAct](../01-react/)

## উদাহরণ

`python patterns/08-evaluator-optimizer/example/main.py`
""",
    "09-human-in-the-loop": """# Human-in-the-Loop (HITL)

## এটি কী

অপরিবর্তনীয়/ঝুঁকিপূর্ণ কাজের **আগে মানুষের approve/input/correction** — checkpoint-এ pause।

## কখন ব্যবহার

- financial, medical, production deploy।
- regulatory, low model trust।

## সম্পর্কিত

- [Guardrails](../12-guardrails/), [Evaluator–Optimizer](../08-evaluator-optimizer/), [Tool Use](../02-tool-use/)

## উদাহরণ

`python patterns/09-human-in-the-loop/example/main.py` — `--auto-approve`, `--time-travel`
""",
    "10-memory": """# Memory & Context Management

## এটি কী

**কথোপকথন, preference, session state** persist/retrieve — turn ও session জুড়ে coherent।

## কখন ব্যবহার

- multi-turn assistant, ongoing project।
- personalization, prior decision recall।

## সম্পর্কিত

- [RAG](../11-rag/), [Planning](../03-planning/)

## উদাহরণ

`python patterns/10-memory/example/main.py` — SQLite checkpoint + `thread_id`
""",
    "11-rag": """# Retrieval-Augmented Generation (RAG)

## এটি কী

Generate-এর **আগে KB থেকে relevant document** — domain fact-এ hallucination কমায়।

## কখন ব্যবহার

- internal docs, policies, catalog।
- citation/traceability।

## সম্পর্কিত

- [Memory](../10-memory/), [Tool Use](../02-tool-use/), [Parallelization](../06-parallelization/)

## উদাহরণ

`python patterns/11-rag/example/main.py` — markdown KB retrieve
""",
    "12-guardrails": """# Guardrails & Safety

## এটি কী

input/output/tool-এ **স্বয়ংক্রিয় policy**: PII redaction, schema validation, allowlist, refusal।

## কখন ব্যবহার

- regulated, customer-facing, side-effecting tools।

## সম্পর্কিত

- [HITL](../09-human-in-the-loop/), [Tool Use](../02-tool-use/), [Routing](../05-routing/)

## উদাহরণ

`python patterns/12-guardrails/example/main.py` — PII block
""",
    "13-handoff": """# Handoff / Delegation

## এটি কী

**এক এজেন্ট থেকে অন্যটিতে** mid-task control transfer — scope/expertise বদল।

## কখন ব্যবহার

- sales → support, tier escalation।
- modular team, clear ownership handover।

## সম্পর্কিত

- [Routing](../05-routing/), [Orchestrator–Workers](../07-orchestrator-workers/)

## উদাহরণ

`python patterns/13-handoff/example/main.py` — Tier-1 → Tier-2
""",
    "14-map-reduce": """# Map–Reduce

## এটি কী

**Map:** chunk-এ split, parallel process। **Reduce:** partial merge → final output।

## কখন ব্যবহার

- long document/log summarize।
- token limit — chunking দরকার।

## সম্পর্কিত

- [Parallelization](../06-parallelization/), [Prompt Chaining](../04-prompt-chaining/)

## উদাহরণ

`python patterns/14-map-reduce/example/main.py` — incident batch → executive report
""",
    "15-event-driven": """# Event-Driven Agents

## এটি কী

**ইভেন্ট** (webhook, queue, schedule) — শুধু sync chat নয়; async, long-running workflow।

## কখন ব্যবহার

- monitoring, nightly jobs, Slack/email/CI integration।

## সম্পর্কিত

- [Orchestrator–Workers](../07-orchestrator-workers/), [HITL](../09-human-in-the-loop/), [Routing](../05-routing/)

## উদাহরণ

`python patterns/15-event-driven/example/main.py` — inbound support email
""",
}

PATTERN_USE_CASES: dict[str, tuple[str, str, list[str], str]] = {
    # slug: (title_bn, why_bn, flow_steps, out_of_scope)
    "01-react": (
        "ReAct",
        "Helpdesk triage এক shot নয় — symptom নিয়ে চিন্তা, FAQ/status টুল, observe, escalate সিদ্ধান্ত। ReAct think→act→observe fixed pipeline ছাড়াই iterative troubleshoot-এ মানায়।",
        [
            'User: "VPN disconnect; restart করেছি।"',
            "Agent: FAQ-এ VPN steps খুঁজব।",
            "`search_faq` → reset steps observe।",
            "Gateway status check।",
            "outage/blocked হলে `create_ticket`।",
            "Actionable steps + ticket ID।",
        ],
        "Bulk incident, multi-agent routing, human approval (অন্য প্যাটার্ন)।",
    ),
    "02-tool-use": (
        "Tool Use",
        "Helpdesk live ticket system, VPN status, employee directory — structured tool call ছাড়া reliable integration কঠিন।",
        [
            "User password reset চায়।",
            "`lookup_employee` → account status।",
            "`search_faq` → reset policy।",
            "`check_vpn_status` → gateway OK।",
            "Policy-compliant steps + optional ticket tool।",
        ],
        "শুধু static FAQ text, টুল schema ছাড়া।",
    ),
    "03-planning": (
        "Planning",
        "VPN + Outlook একসাথে fail — dependency সহ ordered troubleshoot plan দরকার, random tool call নয়।",
        [
            "User: VPN + Outlook issue।",
            "Plan: network → auth → mail client।",
            "Step 1: VPN FAQ + status।",
            "Step 2: password/MFA verify।",
            "Step 3: Outlook cache steps।",
            "Plan complete → unified reply।",
        ],
        "Single FAQ lookup, static chain only।",
    ),
    "04-prompt-chaining": (
        "Prompt Chaining",
        "Support reply: extract facts → classify intent → draft → format — fixed stages, predictable pipeline।",
        [
            "Raw user message।",
            "Extract: symptoms, urgency।",
            "Classify: vpn/password/email।",
            "Draft internal reply।",
            "Format customer-facing tone।",
        ],
        "Dynamic routing mid-pipeline ([Routing](../05-routing/))।",
    ),
    "05-routing": (
        "Routing",
        "এক chat entry — VPN, password, email intents; প্রতিটির আলাদা handler ও tool set।",
        [
            "User mixed intent message।",
            "Router classifies primary intent।",
            "VPN handler OR identity OR email path।",
            "Specialist tools + prompt।",
            "Single coherent reply।",
        ],
        "Monolithic one-size-fits-all agent।",
    ),
    "06-parallelization": (
        "Parallelization",
        "VPN issue — FAQ, gateway status, user email status একসাথে; latency কম, merge reply।",
        [
            "User VPN disconnect।",
            "Parallel: FAQ search + VPN status + account email status।",
            "Merge non-conflicting facts।",
            "Single troubleshooting reply।",
        ],
        "Strict sequential dependency only workflows।",
    ),
    "07-orchestrator-workers": (
        "Orchestrator–Workers",
        "VPN + identity + email — এক agent সব subsystem own করবে না; supervisor delegate করে specialist workers-এ।",
        [
            "User: VPN fail after password reset; Outlook sync fail।",
            "VPN worker → client reset steps।",
            "Identity worker → SSO token refresh।",
            "Email worker → Outlook cache clear।",
            "Orchestrator merge, dedupe, priority।",
            "One coordinated plan।",
        ],
        "Simple single-domain FAQ।",
    ),
    "08-evaluator-optimizer": (
        "Evaluator–Optimizer",
        "Customer reply tone, completeness, policy — draft score করে revise until quality pass।",
        [
            "Draft support reply।",
            "Evaluator: clarity, policy, empathy score।",
            "Below threshold → revise prompt।",
            "Re-draft until pass or max iterations।",
            "Send final reply।",
        ],
        "Instant one-shot answers, no quality loop।",
    ),
    "09-human-in-the-loop": (
        "Human-in-the-Loop",
        "Ticket creation, privileged actions — irreversible side effect-এর আগে manager approve।",
        [
            "Agent decides ticket needed।",
            "Graph interrupt before `create_ticket`।",
            "Human approve/reject/edit।",
            "Resume with `Command(resume=...)`।",
            "Ticket created or alternative path।",
        ],
        "Fully automated low-risk FAQ only flows।",
    ),
    "10-memory": (
        "Memory",
        "Follow-up: *VPN worked briefly, now Outlook fails* — prior context recall without re-explaining।",
        [
            "Turn 1: VPN issue troubleshoot।",
            "Checkpoint saves thread state।",
            "Turn 2: new symptom, same thread_id।",
            "Agent recalls prior VPN steps।",
            "Extended plan including Outlook।",
        ],
        "Stateless one-shot transforms।",
    ),
    "11-rag": (
        "RAG",
        "Policy/playbook markdown KB — hard-coded dict-এর বদলে retrieve + cite grounded answers।",
        [
            "User VPN policy question।",
            "Retrieve relevant KB chunks।",
            "Agent answers with retrieved context।",
            "Optional tools for status/ticket।",
            "Grounded reply with KB reference।",
        ],
        "All knowledge fits in static prompt reliably।",
    ),
    "12-guardrails": (
        "Guardrails",
        "SSN/phone in ticket — input/output PII block before agent or side effects।",
        [
            "User message with sensitive patterns।",
            "Guardrail pre-check blocks/redacts।",
            "Agent runs on safe content only।",
            "Post-check before ticket/email tools।",
            "Refusal or redacted safe reply।",
        ],
        "Trusted internal-only with zero policy (still risky)।",
    ),
    "13-handoff": (
        "Handoff",
        "Tier-1 FAQ exhausted — Tier-2 VPN specialist-এ context সহ transfer।",
        [
            "Tier-1 initial triage।",
            "Determines escalation needed।",
            "Handoff state to Tier-2 agent।",
            "Tier-2 collects VPN logs, deep steps।",
            "Unified thread, new specialist owner।",
        ],
        "Single generalist, no escalation path।",
    ),
    "14-map-reduce": (
        "Map–Reduce",
        "অনেক incident log — parallel summarize per chunk, reduce executive report।",
        [
            "Batch incident JSON input।",
            "Map: summarize each incident/chunk।",
            "Reduce: themes, counts, priorities।",
            "Executive summary for manager।",
        ],
        "Single short message needing full global context in one pass।",
    ),
    "15-event-driven": (
        "Event-Driven",
        "Inbound support email webhook — async process, reply generation, optional ticket।",
        [
            "Email event payload arrives।",
            "Event handler subgraph triggered।",
            "Classify + retrieve + draft reply।",
            "Optional HITL/ticket side effects।",
            "Async completion / notification।",
        ],
        "Sync chat-only, no external events।",
    ),
}

PATTERN_META = {
    "01-react": ("ReAct", "01", "ReAct লুপ: চিন্তা → কাজ → পর্যবেক্ষণ।"),
    "02-tool-use": ("Tool Use", "02", "স্পষ্ট টুল রেজিস্ট্রি সহ এজেন্ট।"),
    "03-planning": ("Planning", "03", "পরিকল্পনা তৈরি করে ধাপে ধাপে কাজ সম্পন্ন।"),
    "04-prompt-chaining": ("Prompt Chaining", "04", "নির্দিষ্ট LLM ধাপের ধারা।"),
    "05-routing": ("Routing", "05", "ইনটেন্ট অনুযায়ী হ্যান্ডলারে রাউট।"),
    "06-parallelization": ("Parallelization", "06", "সমান্তরাল টুল/LLM কল, তারপর মার্জ।"),
    "07-orchestrator-workers": ("Orchestrator–Workers", "07", "সুপারভাইজার + বিশেষজ্ঞ ওয়ার্কার।"),
    "08-evaluator-optimizer": ("Evaluator–Optimizer", "08", "খসড়া → মূল্যায়ন → সংশোধন লুপ।"),
    "09-human-in-the-loop": ("Human-in-the-Loop", "09", "ঝুঁকিপূর্ণ কাজের আগে মানুষের অনুমোদন।"),
    "10-memory": ("Memory", "10", "SQLite চেকপয়েন্ট সহ মাল্টি-টার্ন স্মৃতি।"),
    "11-rag": ("RAG", "11", "KB থেকে রিট্রিভ করে উত্তর দেয়।"),
    "12-guardrails": ("Guardrails", "12", "PII ও নীতি যাচাই।"),
    "13-handoff": ("Handoff", "13", "Tier-1 থেকে Tier-2 হস্তান্তর।"),
    "14-map-reduce": ("Map–Reduce", "14", "ব্যাচ লগ সারসংক্ষেপ।"),
    "15-event-driven": ("Event-Driven", "15", "ইনবাউন্ড ইভেন্ট/ইমেইল প্রক্রিয়া।"),
}

SCENARIOS = [
    ("helpdesk", "IT হেল্পডেস্ক"),
    ("ecommerce", "ই-কমার্স"),
    ("demand-forecast", "চাহিদা পূর্বাভাস (ML)"),
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


def use_case_bn(slug: str) -> str:
    title, why, steps, oos = PATTERN_USE_CASES[slug]
    flow = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    return LANG_BN.format(en="use-case.md") + f"""# Use Case: {title} — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন {title} মানায়

{why}

## উদাহরণ ফ্লো

{flow}

## এই সিনারিওতে নয়

{oos}
"""


def scenario_readme_bn(pattern_num: str, pattern_slug: str, scenario: str, scenario_bn: str) -> str:
    en = f"README.md"
    rel = f"{scenario}/README.md" if scenario != "main" else "README.md"
    if scenario != "main":
        en = f"{scenario}/README.md"
    return LANG_BN.format(en=en) + f"""# {pattern_num} — {scenario_bn}

**{scenario_bn}** সিনারিও দিয়ে এই প্যাটার্ন চালান।

```bash
# রিপো রুট থেকে
python patterns/{pattern_slug}/example/{scenario}/main.py --provider openai
python patterns/{pattern_slug}/example/main.py --scenario {scenario}
```
"""


def main_readme_bn(pattern_num: str, pattern_slug: str, title_bn: str, desc_bn: str) -> str:
    return LANG_BN.format(en="README.md") + f"""# {title_bn} উদাহরণ (LangGraph)

{desc_bn}

## চালান

```bash
python patterns/{pattern_slug}/example/main.py --scenario helpdesk --provider deepseek
python patterns/{pattern_slug}/example/main.py --scenario ecommerce
python patterns/{pattern_slug}/example/main.py --scenario demand-forecast --no-mlflow
```

সাধারণ CLI: `--provider`, `--scenario`, `--use-mcp`, `--no-mlflow` — [`README.bn.md`](../README.bn.md)।
"""


def generate_pattern_docs() -> None:
    print("Pattern README.bn.md & use-case.bn.md:")
    for slug, body in PATTERN_READMES.items():
        pattern_dir = ROOT / "patterns" / slug
        write(pattern_dir / "README.bn.md", LANG_BN.format(en="README.md") + body)
        write(pattern_dir / "use-case.bn.md", use_case_bn(slug))


def generate_example_readmes() -> None:
    print("Example README.bn.md files:")
    for slug, (title, num, desc) in PATTERN_META.items():
        example_dir = ROOT / "patterns" / slug / "example"
        if not example_dir.is_dir():
            continue
        write(example_dir / "README.bn.md", main_readme_bn(num, slug, title, desc))
        for scenario, scenario_bn in SCENARIOS:
            scenario_dir = example_dir / scenario
            if scenario_dir.is_dir():
                write(
                    scenario_dir / "README.bn.md",
                    scenario_readme_bn(num, slug, scenario, scenario_bn),
                )


if __name__ == "__main__":
    generate_pattern_docs()
    generate_example_readmes()
    print("Done.")
