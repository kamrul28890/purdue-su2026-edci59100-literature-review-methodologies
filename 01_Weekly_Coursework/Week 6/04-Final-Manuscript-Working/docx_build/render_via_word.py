import sys
import pathlib
import pythoncom
import win32com.client

DOCX = pathlib.Path(sys.argv[1]).resolve()
PDF = DOCX.parent / "docx_build" / "docx_verify_render.pdf"

pythoncom.CoInitialize()
app = win32com.client.Dispatch("Word.Application")
app.Visible = False
try:
    doc = app.Documents.Open(str(DOCX))
    doc.Repaginate()
    pages = doc.ComputeStatistics(2)  # wdStatisticPages
    words = doc.ComputeStatistics(0)  # wdStatisticWords
    print(f"Pages: {pages}  Words: {words}")
    doc.SaveAs(str(PDF), FileFormat=17)  # wdFormatPDF
    doc.Close(False)
finally:
    app.Quit()
    pythoncom.CoUninitialize()

print(f"PDF written: {PDF}")
