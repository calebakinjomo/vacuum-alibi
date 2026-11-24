"""The Vacuum's Alibi — one-line bounty entry.

Writes a single 146-character alibi line (within the 200-character limit)
to entry.txt: a robot vacuum's deadpan incident report blaming the cat
for a spot that was not on its map, escalated to the sock.
"""
import os

ENTRY = "Incident report 04:12: the spot was not on my map. The cat moved it there at 03:47 and denied everything. I have escalated the matter to the sock."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
