import re, pathlib
from collections import Counter

SRC = pathlib.Path(__file__).parent.parent / "Final_Literature_Review_Manuscript_Summer26_Kamrul_MdKamruzzaman.tex"
t = SRC.read_text(encoding="utf8")
idx = t.find(r"\begin{document}")
print("idx", idx, "total len", len(t))
body = t[idx:]
print("body len", len(body))

seqs = re.findall(r"\\[a-zA-Z]+\*?", body)
print("num seqs found", len(seqs))
c = Counter(seqs)
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(f"{v:5d}  {k}")
