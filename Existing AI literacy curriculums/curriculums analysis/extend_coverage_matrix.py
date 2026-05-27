#!/usr/bin/env python3
"""Add UNESCO, German_Standards, Developed_Curriculum columns to learning points coverage matrix."""

import csv
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent / "Learning_Points_Coverage_Matrix__validation_required.csv"
OUT = Path(__file__).resolve().parent / "Learning_Points_Coverage_Extended__validation_required.csv"

NEW_HEADER = (
    "Category,Subcategory,Specific Learning Point,Berlin,Day of AI,MIT DAILy,Common Sense,"
    "aiEDU,Georgia,ENARIS,MIT AI Ethics,AI4K12,AI Adapt,Duke,Harvard,Toddle,"
    "UNESCO,German_Standards,Developed_Curriculum"
)


def norm(s: str) -> str:
    return (s or "").lower()


def join_blocks(*parts: str) -> str:
    seen = []
    for p in parts:
        if not p:
            continue
        for x in re.split(r"[,;]\s*", p):
            x = x.strip()
            if x and x not in seen:
                seen.append(x)
    return "; ".join(seen) if seen else ""


def unesco_for_row(category: str, subcategory: str, slp: str) -> str:
    c, s, t = norm(category), norm(subcategory), norm(slp)

    # Pedagogy / delivery-only (no direct UNESCO student competency)
    if category == "Pedagogy & Activities":
        if "exit ticket" in t or "reflection prompt" in t:
            return "Yes - Human Agency/Accountability (reflective use of AI in learning)"
        if "explore ai journal" in t or "one word story" in t or "t-chart" in t:
            return "Yes - Application Skills (guided exploration of AI/LLM behavior)"
        if "worksheet" in t and "creative process" in t:
            return "Yes - Human Agency/Accountability (transparency in AI-assisted creation)"
        if "48-hour disconnect" in t:
            return "Yes - Human Agency/Accountability (digital well-being, intentional technology use)"
        if "debate" in s or "debate" in t:
            return "Yes - Citizenship; Embodied Ethics (structured discourse on AI benefits/risks)"
        if "unplugged" in s:
            if "coin game" in t or "reinforcement" in t:
                return "Yes - AI Foundations (reinforcement learning concepts)"
            if "classification" in t or "sl algorithm" in t or "semantic feature" in t:
                return "Yes - AI Foundations (supervised learning, data representation)"
            if "bubble sort" in t:
                return "Yes - AI Foundations (algorithms and stepwise procedures)"
            if "pasta" in t or "candy" in t or "decision tree" in t:
                return "Yes - AI Foundations (classification, algorithms)"
            return "Yes - AI Foundations (computational thinking linked to AI concepts)"
        if "project" in s:
            if "youtube" in t or "recommendation" in t:
                return "Yes - Citizenship; Ethics by Design (algorithmic systems and stakeholder values)"
            if "deepfake" in t or "psa" in t:
                return "Yes - Safe Use; Citizenship (misinformation, democratic discourse)"
            if "dream bot" in t or "robot" in t and "sensor" in t:
                return "Yes - AI Foundations; Problem Scoping (robotic systems design)"
            if "gan" in t or "story" in t:
                return "Yes - AI Foundations; Safe Use (generative AI and authorship)"
            if "chatgpt interview" in t or "interspecies" in t:
                return "Yes - Application Skills; Human Agency (designing with generative AI)"
            if "manifesto" in t or "zine" in t:
                return "Yes - Citizenship (critical stance on AI in society)"
            if "interview fictional" in t:
                return "Yes - Safe Use; Human Agency (evaluating AI-generated sources)"
            return "Yes - Application Skills; Citizenship (project-based AI literacy)"
        return "Yes - Application Skills; Human Agency (activity-based AI learning)"

    if category == "Literacy Meta-Skills":
        if "certificate" in t or "quiz" in t and "checking" in t:
            return "Yes - Iteration (assessment and feedback on learning)"
        if "digital literacy" in t:
            return "Yes - Safe Use; Citizenship (digital-AI literacy connections)"
        if "ai literacy" in t or "readiness" in t:
            return "Yes - AI Foundations; Embodied Ethics (core AI literacy outcomes)"
        if "future of jobs" in t or "wef" in t:
            return "Yes - Citizenship (future of work and skills)"
        return "Yes - Human Agency/Accountability (meta-competencies)"

    # Default by category
    cat_map = {
        "ai fundamentals": (
            "Yes - AI Foundations (AI definition, system components, ML types, neural networks as applicable)"
        ),
        "algorithms & data": (
            "Yes - AI Foundations (data, algorithms, AI lifecycle); Application Skills (data/ML practice)"
        ),
        "machine learning": (
            "Yes - AI Foundations (supervised/unsupervised learning); Application Skills (ML methods)"
        ),
        "neural networks": "Yes - AI Foundations (neural networks, training, representations)",
        "nlp & language": (
            "Yes - AI Foundations (AI for language); Application Skills (NLP/LLM use and limits)"
        ),
        "computer vision": "Yes - AI Foundations (perception); Application Skills (CV techniques)",
        "generative ai": (
            "Yes - AI Foundations (generative models); Safe Use (labeling, misuse risks where relevant)"
        ),
        "deepfakes & misinformation": (
            "Yes - Safe Use (misinformation, media integrity); Citizenship (societal harms)"
        ),
        "ethics & values": (
            "Yes - Embodied Ethics; Ethics by Design; Human Agency/Accountability (principles, dilemmas, oversight)"
        ),
        "bias & fairness": (
            "Yes - Embodied Ethics (bias, fairness); Architecture Design (anti-bias data and design)"
        ),
        "limitations & capabilities": (
            "Yes - Human Agency/Accountability (overreliance); Problem Scoping (limits of AI); AI Foundations (capabilities)"
        ),
        "prompt engineering": "Yes - Application Skills (effective use of AI tools); Iteration (testing prompts)",
        "system design": (
            "Yes - Ethics by Design (guardrails, transparency); Human Agency (stakeholder-aware design)"
        ),
        "reinforcement learning": "Yes - AI Foundations (reinforcement learning)",
        "societal impact": (
            "Yes - Citizenship (inequality, labor, governance, media); Embodied Ethics (rights, justice)"
        ),
        "environmental impact": (
            "Yes - Embodied Ethics (sustainability); Citizenship (climate); Architecture Design (energy-efficient AI)"
        ),
        "privacy & data": "Yes - Embodied Ethics (privacy, rights); Safe Use (data hygiene)",
        "ip & copyright": "Yes - Safe Use (copyright, marking AI content, responsible use)",
        "hands-on tools": (
            "Yes - Application Skills (tools, datasets, libraries); Creating Tools (building/adapting systems)"
        ),
        "programming & cs": "Yes - Application Skills (programming, CS concepts for AI)",
        "specific concepts": (
            "Yes - AI Foundations; Application Skills (technical depth aligned to competencies)"
        ),
        "real-world systems": (
            "Yes - Citizenship; AI Foundations (applied AI systems, ethics of deployment)"
        ),
        "ai & art": "Yes - Safe Use (authorship); Citizenship (culture, equity)",
        "social skills": (
            "Yes - Human Agency/Accountability; Iteration (collaboration, testing, communication about AI use)"
        ),
        "specialized topics": "Yes - Citizenship; Embodied Ethics (domain-specific risks and equity)",
        "advanced topics": "Yes - Application Skills; AI Foundations (advanced architectures and methods)",
        "metacognition": "Yes - Human Agency/Accountability (learning with/without AI)",
        "diverse perspectives": (
            "Yes - Embodied Ethics (fairness); Citizenship (representation, cultural context)"
        ),
        "real applications case studies": (
            "Yes - Citizenship; Human Agency/Accountability; Embodied Ethics (real-world consequences)"
        ),
    }

    base = cat_map.get(c)
    if not base:
        base = "Yes - AI Foundations; Citizenship (general AI literacy relevance)"

    # Refinements
    if "watermark" in t or ("labeling" in t and "ai-generated" in t):
        base = "Yes - Safe Use (labeling AI-generated content); Citizenship (regulation)"
    if "eu " in t or "gdpr" in t or "trustworthy ai" in t:
        base = "Yes - Citizenship (governance, regulation); Embodied Ethics (human rights, privacy)"
    if "trolley" in t or "moral machine" in t:
        base = "Yes - Embodied Ethics (ethical dilemmas); Human Agency (values in automation)"
    if "ghost work" in t or "labeling" in t and "moderation" in t:
        base = "Yes - Citizenship (labor, global inequality); Embodied Ethics (human rights)"
    if "lethal autonomous" in t or "weapons" in t:
        base = "Yes - Citizenship (governance); Human Agency (high-stakes decisions)"
    if "gan" in t and "generator" in t:
        base = "Yes - AI Foundations (generative models); Application Skills"

    return base


def german_for_row(category: str, subcategory: str, slp: str) -> str:
    c, s, t = norm(category), norm(subcategory), norm(slp)

    yes = lambda *areas: "Yes - " + "; ".join(areas)

    # Strong No: very narrow AI research / journalism / proprietary tools without NwT hook
    narrow_no = (
        "bert:", "gpt-3 and language", "sigmoid, relu", "degrees of freedom",
        "von neumann architecture", "receptive field", "viola-jones",
        "hexapawn", "q-learning:", "alphastar",
    )
    if any(x in t for x in narrow_no) and "sensor" not in t and "privacy" not in t:
        return "No"

    # Algorithms / logic / CS structures
    if any(
        k in t
        for k in (
            "algorithm",
            "breadth-first",
            "graph coloring",
            "decision tree",
            "sorting",
            "bubble sort",
            "graph:",
            "trees:",
            "abstraction:",
            "decompos",
            "boolean logic",
            "and (need both)",
            "or (need either)",
            "neuron sandbox",
            "scratch",
            "blockly",
            "variables",
            "loops",
            "conditional",
            "programming",
            "hardware vs software",
        )
    ):
        return yes(
            "Algorithms (logic, sequences, branches, loops)",
            "Information processing (conditions, loops, branching)",
        )

    # Microcontrollers / embedded
    if any(k in t for k in ("microcontroller", "arduino", "nano", "c++")):
        return yes("Microcontrollers and programming", "Systems and processes (technical systems)")

    # Sensors / actuators / robotics / control
    if any(
        k in t
        for k in (
            "sensor",
            "actuator",
            "lidar",
            "radar",
            "sonar",
            "robot",
            "autonomous vehicle",
            "self-driving",
            "collision",
            "perception, localization",
            "warehouse",
            "industrial robot",
        )
    ):
        return yes(
            "Sensors (types, functioning, comparison with sensory organs)",
            "Controls with sensors/actuators",
            "Systems and processes (system boundaries, energy and information flows)",
        )

    # Privacy / data / tracking / information society
    if any(
        k in t
        for k in (
            "privacy",
            "personal data",
            "pii",
            "gdpr",
            "tracking",
            "data collection",
            "surveillance",
            "facial recognition",
            "social media data",
            "chatbot memory",
            "web scraping",
        )
    ):
        return yes(
            "Data security & information society (personal data, tracking, privacy)",
            "Ethics (privacy, data protection, youth protection, responsibility)",
        )

    # Media / misinformation / youth
    if any(
        k in t
        for k in (
            "misinformation",
            "disinformation",
            "deepfake",
            "echo chamber",
            "recommendation algorithm",
            "tiktok",
            "filter bubble",
            "social media manipulation",
        )
    ):
        return yes(
            "Ethics (media influence, privacy, data protection, responsibility)",
            "Data security & information society",
        )

    # Sustainability / environment / resources / product lifecycle
    if any(
        k in t
        for k in (
            "sustainability",
            "climate",
            "energy",
            "water use",
            "emissions",
            "carbon",
            "environmental",
            "digital footprint",
            "resource-saving",
            "lifecycle",
            "repair devices",
        )
    ):
        return yes(
            "Human-nature-technology (sustainability, effects of technology)",
            "Product development (lifecycle, resource-saving orientation)",
            "Systems and processes (energy/resource flows)",
        )

    # Ethics (general) — German ethics strand
    if category in ("Ethics & Values", "Bias & Fairness") or "ethical" in t or "stakeholder" in t:
        return yes(
            "Ethics (media influence, privacy, data protection, youth protection, responsibility)",
            "Human-nature-technology (freedom & responsibility)",
        )

    # Societal / citizenship — partial overlap with ethics strand
    if category == "Societal Impact" and any(
        k in t for k in ("job", "labor", "economy", "access", "divide", "policy", "government")
    ):
        return yes(
            "Ethics (responsibility in technology society)",
            "Human-nature-technology (technology effects)",
        )

    # Hands-on: general programming tools — information processing
    if category == "Hands-on Tools" and any(
        k in t for k in ("scratch", "python", "pandas", "tensorflow", "javascript")
    ):
        return yes("Information processing (programming elements)", "Algorithms")

    # Default for pure AI theory without CS/ethics/sensors hook
    if c in (
        "ai fundamentals",
        "machine learning",
        "neural networks",
        "nlp & language",
        "computer vision",
        "generative ai",
        "reinforcement learning",
        "specific concepts",
        "advanced topics",
    ):
        return "No"

    if c == "algorithms & data":
        return yes("Algorithms", "Information processing (structured problem solving)")

    if c == "programming & cs":
        return yes("Algorithms", "Information processing")

    if c == "privacy & data":
        return yes(
            "Data security & information society",
            "Ethics (privacy, data protection)",
        )

    if c == "environmental impact":
        return yes(
            "Human-nature-technology (sustainability)",
            "Systems and processes (energy flows)",
        )

    if c == "ip & copyright":
        return yes("Ethics (responsibility, legal/ethical norms in digital society)")

    if c == "limitations & capabilities":
        return yes("Ethics (critical media and technology use)", "Human-nature-technology")

    if c == "prompt engineering" or c == "system design":
        return yes("Information processing (structured tasks)", "Ethics (responsible design)")

    if c == "deepfakes & misinformation":
        return yes("Ethics (media influence)", "Data security & information society")

    if c == "hands-on tools":
        return "No"

    if c == "pedagogy & activities":
        if "unplugged" in s or "bubble" in t or "sort" in t:
            return yes("Algorithms", "Information processing")
        return "No"

    if c == "social skills":
        return yes("Ethics (responsibility, collaboration in digital contexts)")

    if c == "literacy meta-skills":
        return yes("Ethics; Human-nature-technology (reflective technology use)")

    if c == "metacognition":
        return yes("Ethics (responsibility for own learning)", "Human-nature-technology")

    if c == "diverse perspectives":
        return yes("Ethics (equity, responsibility)", "Human-nature-technology")

    if c == "real applications case studies":
        if any(k in t for k in ("tesla", "autopilot", "vehicle", "driving")):
            return yes("Sensors and controls", "Ethics (safety, responsibility)")
        return yes("Ethics", "Human-nature-technology")

    if c == "specialized topics":
        return "No"

    if c == "ai & art":
        return yes("Ethics (media, authorship)", "Human-nature-technology")

    if c == "real-world systems":
        if any(k in t for k in ("robot", "sensor", "vehicle", "farm", "iot")):
            return german_for_row("Real-world Systems", "Industry", "sensors IoT")
        return "No"

    return "No"


def marty_for_row(category: str, subcategory: str, slp: str) -> str:
    c, s, t = norm(category), norm(subcategory), norm(slp)

    def w(n: int, desc: str) -> str:
        return f"Yes - Week {n}: {desc}"

    # Week-targeted keywords first
    if any(
        k in t
        for k in (
            "social robot",
            "types of robot",
            "robot components",
            "motors, sensors",
            "autonomous behavior",
            "characteristics, autonomous",
        )
    ) or (c == "ai fundamentals" and "robot" in t):
        return w(1, "social robots, types, components (motors, sensors)")

    if any(
        k in t
        for k in (
            "ai definition",
            "ai vs non-ai",
            "narrow ai vs general",
            "three basic components",
            "map of ai:",
            "supervised learning:",
            "unsupervised",
            "classification vs regression",
            "prompt engineering",
            "llm",
            "large language",
            "chatgpt",
            "temperature parameter",
            "next token",
            "three training layers",
        )
    ):
        return w(2, "AI definition, AI vs non-AI, ML types, LLM intro/limitations/uses, prompt engineering")

    if any(
        k in t
        for k in (
            "transformer",
            "llm architecture",
            "word embeddings",
            "semantic feature space",
            "lithium",
            "recycling",
            "cultural bias",
            "social equity",
            "inequality",
            "feedback loop",
            "sustainability",
            "materials",
        )
    ) or ("equity" in t and "access" in t):
        return w(3, "LLM architecture, sustainability (materials/recycling/lithium), equity, cultural bias, feedback loops")

    if any(
        k in t
        for k in (
            "hallucination",
            "when not to use ai",
            "algorithmic bias:",
            "mitigation",
            "libraries",
            "marty",
            "infrared",
            "color sensor",
            "motor function",
            "commands, variables, functions",
            "blockly",
        )
    ) or (s == "scratch/blocks" and "variable" in t):
        return w(4, "biases/hallucinations, when not to use AI, programming basics, libraries, Marty architecture, sensors, motors")

    if any(
        k in t
        for k in (
            "choreograph",
            "sensor types",
            "sensor input",
            "how sensors work",
            "blockly programming",
        )
    ) or (c == "hands-on tools" and "scratch" in t and "cognimates" in t):
        return w(5, "Blockly, sensor types/Marty sensors, sensor programming, choreography")

    if any(
        k in t
        for k in (
            "microcontroller",
            "arduino",
            "c++",
            "alignment",
            "mental health",
            "overreliance",
            "manipulation",
            "misinformation",
            "energy, water",
            "llm safeguard",
            "jailbreak",
            "adversarial prompting",
        )
    ):
        return w(6, "microcontrollers/Arduino/C++, AI ethics, mental health, over-reliance, misinformation, sustainability, safeguards")

    if any(
        k in t
        for k in (
            "scaffolded",
            "unscaffolded",
            "interaction design",
            "educational application",
            "responsible ai use",
            "academic integrity",
            "communicating ai use",
            "essential agreements",
            "certificate of completion",
        )
    ):
        return w(7, "LLM interaction design, educational use, responsible AI, safeguards review, disclosure norms")

    # Category-based Marty coverage
    if c == "ai fundamentals":
        if "robot" in t:
            return w(1, "robots in society and components")
        return w(2, "AI definitions, AI vs non-AI, applications map to intro units")

    if c == "algorithms & data":
        return w(4, "algorithms/data links to programming basics and ML context in Marty sequence")

    if c == "machine learning":
        return w(2, "supervised learning and ML types introduced")

    if c == "neural networks":
        return w(2, "neural networks tied to LLM/deep learning intro at high level") if "llm" in t or "language" in t else w(3, "neural networks in LLM architecture week")

    if c == "nlp & language":
        return w(2, "LLM/NLP basics, limitations, chatbots") if "llm" in t or "chatbot" in t or "token" in t else w(3, "language models, embeddings/architecture themes")

    if c == "computer vision":
        return w(4, "sensors/perception bridge; computer vision only partially—robot sensors")

    if c == "generative ai":
        return w(2, "generative AI/LLMs and prompts") if "llm" in t or "generative" in t else w(3, "generative AI impacts, bias in outputs")

    if c == "deepfakes & misinformation":
        return w(6, "misinformation, verification, critical use of AI outputs")

    if c == "ethics & values":
        return w(6, "AI ethics themes; dilemmas partially via responsible use weeks")

    if c == "bias & fairness":
        return w(3, "equity/cultural bias") if "cultural" in t or "equity" in t else w(4, "biases in AI and fairness")

    if c == "limitations & capabilities":
        return w(4, "when not to use AI, limitations; Week 6 over-reliance") if "not to use" in t or "overreliance" in t else w(2, "AI capabilities vs limits (LLM)")

    if c == "prompt engineering":
        return w(2, "prompt engineering") if "prompt" in t else w(7, "advanced prompting and interaction design")

    if c == "system design":
        return w(7, "LLM system/guardrails and responsible design")

    if c == "reinforcement learning":
        return w(2, "ML types include RL at overview level (not primary Marty focus)")

    if c == "societal impact":
        return w(3, "social equity/sustainability framing") if any(
            k in t for k in ("equity", "access", "divide", "labor", "job")
        ) else w(6, "broader societal impacts and ethics")

    if c == "environmental impact":
        return w(3, "sustainability (materials)") if "material" in t or "lithium" in t else w(6, "energy/water impacts of AI")

    if c == "privacy & data":
        return w(6, "privacy, data protection in AI ethics week")

    if c == "ip & copyright":
        return w(7, "responsible use, citation, academic integrity with AI")

    if c == "hands-on tools":
        if "teachable" in t or "scratch" in t or "blockly" in t.lower():
            return w(4, "hands-on ML/block programming stack")
        if "chatgpt" in t or "gemini" in t:
            return w(2, "generative AI tools in classroom")
        return "No"

    if c == "programming & cs":
        return w(4, "programming basics") if "scratch" not in t or "cognimates" in t else w(5, "blocks-based programming")

    if c == "specific concepts":
        if "transformer" in t or "cnn" in t:
            return w(3, "LLM/transformer architecture context")
        return "No"

    if c == "real-world systems":
        if any(k in t for k in ("robot", "siri", "alexa", "assistant")):
            return w(1, "robots and intelligent assistants")
        if "vehicle" in t or "autonomous" in t:
            return w(1, "automation/sensors as systems (partial)")
        return w(2, "everyday AI systems at intro level")

    if c == "ai & art":
        return w(3, "bias/stereotypes in generative outputs; cultural harm")

    if c == "social skills":
        return w(7, "collaboration, communication, and norms for AI use (Harvard-style lessons mirrored in W7 themes)")

    if c == "pedagogy & activities":
        return "No"

    if c == "specialized topics":
        return "No"

    if c == "literacy meta-skills":
        return w(7, "course-level AI literacy goals and assessment")

    if c == "advanced topics":
        return w(3, "advanced NLP tied to LLM architecture where covered")

    if c == "metacognition":
        return w(7, "learning with AI, scaffolded interactions")

    if c == "diverse perspectives":
        return w(3, "cultural bias, equity")

    if c == "real applications case studies":
        return w(6, "case-based discussion of risks/ethics") if "chatgpt" in t or "limitation" in t else w(2, "applied LLM examples")

    return "No"


def refine_german_after_marty(category: str, subcategory: str, slp: str, marty: str) -> str:
    """If Marty covers sensors/programming strongly, ensure German reflects NwT sensors/programming when applicable."""
    t = norm(slp)
    if marty.startswith("Yes - Week 4") and "sensor" in t:
        return "Yes - Sensors (types, functioning); Controls with sensors/actuators; Information processing"
    if marty.startswith("Yes - Week 5"):
        return "Yes - Sensors; Controls with sensors/actuators; Information processing (Blockly)"
    if marty.startswith("Yes - Week 6") and "microcontroller" in marty.lower():
        return "Yes - Microcontrollers and programming; Systems and processes; Ethics (privacy, responsibility)"
    return german_for_row(category, subcategory, slp)


def main() -> None:
    rows_out = []
    with SRC.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header[:3] == ["Category", "Subcategory", "Specific Learning Point"]
        for row in reader:
            if len(row) < 3:
                continue
            cat, sub, slp = row[0], row[1], row[2]
            rest = row[3:]
            u = unesco_for_row(cat, sub, slp)
            m = marty_for_row(cat, sub, slp)
            g = refine_german_after_marty(cat, sub, slp, m)
            rows_out.append([cat, sub, slp, *rest, u, g, m])

    with OUT.open("w", newline="", encoding="utf-8") as f:
        f.write(NEW_HEADER + "\n")
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        for row in rows_out:
            w.writerow(row)

    print(f"Wrote {len(rows_out)} rows to {OUT}")


if __name__ == "__main__":
    main()
