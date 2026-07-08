"""Encode author-reviewed paradigm membership (Week 5 master table, Bui removed)
and emit derived cross-tabs + cleaned distributions. Reads curated_58."""
import pandas as pd, json, pathlib

SRC = pathlib.Path(r"D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv")
HERE = pathlib.Path(__file__).parent
c = pd.read_csv(SRC)

# Paradigm membership by ref (Week 5 master table, author-reviewed; Bui/ref102 excluded as it is not in curated_58)
PARADIGM = {
    # A: Zero/Few-Shot retrieval (6)
    43: "A", 66: "A", 62: "A", 100: "A", 98: "A", 101: "A",
    # B: Domain fine-tuned generative (6)
    96: "B", 74: "B", 92: "B", 93: "B", 94: "B", 88: "B",
    # C: Hybrid agentic / geometric-semantic (7)
    91: "C", 2: "C", 24: "C", 97: "C", 99: "C", 11: "C", 56: "C",
}
core = c[c.dataset_group == "Core"].copy()
core["paradigm"] = core.ref.map(PARADIGM)
assert core.paradigm.notna().all(), core[core.paradigm.isna()][["ref", "title"]]
assert core.paradigm.value_counts().to_dict() == {"C": 7, "A": 6, "B": 6}, core.paradigm.value_counts().to_dict()


def app2(s):
    s = str(s).lower()
    hs = any(k in s for k in ["safety", "compliance", "hazard", "ppe"])
    hp = any(k in s for k in ["progress", "site management", "resource", "quality", "productivity"])
    if hs and hp:
        return "Both"
    if hs:
        return "Safety"
    if hp:
        return "Progress"
    return "Other"


core["app"] = core.focus.map(app2)


def dataset_uses_public(s):
    s = str(s).lower()
    return any(k in s for k in ["soda", "acid", "tocs", "mocs", "public", "benchmark", "imagenet", "pci"])


core["uses_public"] = core.dataset_detail.map(dataset_uses_public)

out = {
    "core_paradigm_counts": core.paradigm.value_counts().to_dict(),
    "paradigm_by_year": {
        p: {int(y): int(n) for y, n in core[core.paradigm == p].year.value_counts().sort_index().items()}
        for p in ["A", "B", "C"]
    },
    "paradigm_by_application": (
        pd.crosstab(core.paradigm, core.app).reindex(index=["A", "B", "C"]).fillna(0).astype(int).to_dict("index")
    ),
    "core_dataset_public_vs_private": {
        "private_only": int((~core.uses_public).sum()),
        "uses_public": int(core.uses_public.sum()),
        "public_refs": [int(r) for r in core[core.uses_public].ref.tolist()],
        "pct_private": round(100 * (~core.uses_public).sum() / len(core), 1),
    },
}

# Clean journal counts (case/whitespace normalize)
jn = c.source_title.fillna("Unknown").astype(str).str.strip()
jn = jn.str.replace("List of Issues", "", regex=False).str.strip()
jn = jn.str.title().str.replace("Asce", "ASCE", regex=False)
norm = {
    "Automation In Construction": "Automation in Construction",
    "Computer-Aided Civil And Infrastructure Engineering": "Computer-Aided Civil and Infrastructure Engineering",
    "Journal Of Construction Engineering And Management": "Journal of Construction Engineering and Management",
    "Journal Of Computing In Civil Engineering": "Journal of Computing in Civil Engineering",
    "Journal Of Building Engineering": "Journal of Building Engineering",
    "Expert Systems With Applications": "Expert Systems with Applications",
    "Advanced Engineering Informatics": "Advanced Engineering Informatics",
    "Engineering, Construction And Architectural Management": "Engineering, Construction and Architectural Management",
}
jn = jn.map(lambda x: norm.get(x, x))
out["journal_counts_clean"] = {str(k): int(v) for k, v in jn.value_counts().items()}

# Clean automation buckets (all 58)
def auto_bucket(s):
    s = str(s).lower()
    if "review" in s or "n/a" in s:
        return "Review / N.A."
    if "assistive" in s or "manual review" in s or "crowdsourc" in s or "query" in s or "assistant" in s:
        return "Assistive (Human-in-loop)"
    if "manual" in s:
        return "Manual"
    if "automated" in s or "autonomous" in s or "analytical" in s:
        return "Fully Automated"
    return "Unspecified"
out["automation_buckets_all58"] = {str(k): int(v) for k, v in c.automation_level.fillna("").map(auto_bucket).value_counts().items()}

# Geography grouped (primary/first country)
prim = c.countries_analysis.dropna().map(lambda s: str(s).split(";")[0].strip())
out["country_primary_counts"] = {str(k): int(v) for k, v in prim.value_counts().items()}

(HERE / "manuscript_derived.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
core[["ref", "year", "paradigm", "app", "focus", "uses_public", "algorithm_model", "validation_metric"]].to_csv(
    HERE / "core19_paradigm_assigned.csv", index=False
)
print("\nWrote manuscript_derived.json + core19_paradigm_assigned.csv")
