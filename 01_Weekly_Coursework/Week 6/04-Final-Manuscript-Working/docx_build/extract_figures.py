import re, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT.parent / "Final_Literature_Review_Manuscript_Summer26_Kamrul_MdKamruzzaman.tex"
FIGSRC = ROOT / "fig_src"
text = SRC.read_text(encoding="utf8")

PREAMBLE = r"""\documentclass[border=4pt]{standalone}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.17}
\usepackage[table]{xcolor}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit, calc}
\definecolor{headingblue}{HTML}{1F4E79}
\definecolor{lightblue}{HTML}{D9EAF7}
\definecolor{softgray}{HTML}{F4F6F8}
\definecolor{darkgray}{HTML}{404040}
\definecolor{prismagreen}{HTML}{E8F5E9}
\definecolor{prismabox}{HTML}{1565C0}
\definecolor{chartblue}{HTML}{2196F3}
\definecolor{chartorange}{HTML}{FF9800}
\definecolor{chartgreen}{HTML}{4CAF50}
\definecolor{chartred}{HTML}{F44336}
\definecolor{chartpurple}{HTML}{9C27B0}
\definecolor{chartgray}{HTML}{9E9E9E}
\begin{document}
"""
POSTAMBLE = r"""
\end{document}
"""

labels = ["fig:prisma", "fig:pubyear", "fig:framework", "fig:paradigmyear"]
for label in labels:
    lbl_idx = text.index(f"\\label{{{label}}}")
    tikz_start = text.index(r"\begin{tikzpicture}", lbl_idx)
    tikz_end = text.index(r"\end{tikzpicture}", tikz_start) + len(r"\end{tikzpicture}")
    block = text[tikz_start:tikz_end]
    out = PREAMBLE + block + POSTAMBLE
    name = label.split(":")[1]
    (FIGSRC / f"{name}.tex").write_text(out, encoding="utf8")
    print(f"wrote {name}.tex ({len(block)} chars)")
