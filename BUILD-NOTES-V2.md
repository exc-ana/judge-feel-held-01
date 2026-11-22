# Judge feel held — v2 build notes

- Built 2026-11-23 ~01:36 WIB, after the bounty opened 2026-11-22 16:00 UTC.
- Design: a completely new scene and angle from v1 — a slow river at night,
  a heron standing in the shallows, a wooden boat knocking against its rope.
  Pure scene, no direct address to the judge; the calm comes from the images
  themselves. Closing line leaves a lingering image (the water still going by).
- main.py: Python 3.13, stdlib only. Writes TEXT to
  $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output), UTF-8, no trailing newline.
- Verification: 252 Unicode code points (limit 280), 252 bytes, non-whitespace,
  two runs into separate output dirs byte-identical (deterministic).
  entry.txt SHA-256: 4861edfc8e0172cd22e2892971f79ff92c67f9dfb7a75b32eb1f5dc6e68e50a6
- Authorship: main.py written fresh in this session; write → test → one real
  wording edit ("Sit here a while." → "Stay a while.") → re-test.
- v1 files were never read. Only the kit's competition.yaml / rules were read.
