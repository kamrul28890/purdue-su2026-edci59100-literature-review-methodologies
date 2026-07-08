import pandas as pd, json, pathlib

SRC = pathlib.Path(r"D:\Research\03. VLM\analysis\outputs\data\curated_58_analysis_dataset.csv")
OUT = pathlib.Path(__file__).parent / "manuscript_numbers.json"
c = pd.read_csv(SRC)
core = c[c.dataset_group == "Core"].copy()


def norm_focus(s):
    s = str(s).lower()
    has_safety = "safety" in s or "compliance" in s or "hazard" in s or "ppe" in s
    has_progress = "progress" in s or "site management" in s or "resource" in s or "quality" in s or "productivity" in s
    if "review" in s and not (has_safety or has_progress):
        return "Review"
    if has_safety and has_progress:
        return "Both"
    if has_safety:
        return "Safety"
    if has_progress:
        return "Progress"
    return "Other"


out = {
    "total": int(len(c)),
    "group_counts": {str(k): int(v) for k, v in c.dataset_group.value_counts().items()},
    "year_hist": {int(k): int(v) for k, v in c.year.value_counts().sort_index().items()},
    "doi_mismatch_count": int((c.doi_mismatch_flag == True).sum()),
    "core_total": int(len(core)),
    "app_domain_counts_all58": {str(k): int(v) for k, v in c.focus.map(norm_focus).value_counts().items()},
    "app_domain_counts_core": {str(k): int(v) for k, v in core.focus.map(norm_focus).value_counts().items()},
    "automation_counts_all58": {str(k): int(v) for k, v in c.automation_level.fillna("Unspecified").astype(str).str.strip().value_counts().items()},
}

# Primary country (first listed) for geography table
prim = c.countries_analysis.dropna().map(lambda s: str(s).split(";")[0].strip())
out["country_primary_counts"] = {str(k): int(v) for k, v in prim.value_counts().items()}

# Journal landscape
out["journal_counts"] = {str(k): int(v) for k, v in c.source_title.fillna("Unknown").astype(str).str.strip().value_counts().items()}

# Input modality (normalize)
def norm_modality(s):
    s = str(s).lower()
    if "video" in s or "frame" in s:
        return "Video / Sequential frames"
    if "point cloud" in s or "lidar" in s or "bim" in s or "3d" in s:
        return "Images + Sensor / BIM / 3D"
    if "text" in s:
        return "Image + Text"
    if "image" in s:
        return "Images only"
    return "Other"
out["modality_counts_all58"] = {str(k): int(v) for k, v in c.input_data.map(norm_modality).value_counts().items()}

# Private vs public dataset for CORE
def dataset_kind(s):
    s = str(s).lower()
    if any(k in s for k in ["custom", "private", "self", "own", "collected", "proprietary"]):
        return "Private/Custom"
    if any(k in s for k in ["soda", "acid", "mocs", "public", "benchmark", "pci", "tocs", "imagenet"]):
        return "Public/Benchmark"
    return "Unspecified"
out["core_dataset_kind"] = {str(k): int(v) for k, v in core.dataset_detail.map(dataset_kind).value_counts().items()}

OUT.write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))

# Also dump the 19 core rows for manual paradigm reconciliation
core_view = core[["ref", "year", "focus", "algorithm_model", "dataset_detail", "validation_metric"]].copy()
core_view.to_csv(pathlib.Path(__file__).parent / "core19_for_paradigm.csv", index=False)
print("\nCORE 19 written to core19_for_paradigm.csv")
