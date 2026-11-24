import os

ENTRY = "Incident report 04:12: the spot was not on my map. The cat moved it there at 03:47 and denied everything. I have escalated the matter to the sock."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
