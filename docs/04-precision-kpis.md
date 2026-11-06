# Precision and Quality Indicators

Targets are proposed prototype acceptance thresholds, not measured results.

| KPI | Definition | Target |
|---|---|---:|
| Source traceability | resolvable source-linked nodes / eligible nodes | 100% |
| Identity stability | IDs unchanged after view-only re-render | 100% |
| Graph integrity | edges with existing endpoints / all edges | 100% |
| Provenance completeness | populated required provenance fields / eligible artifacts | ≥99% |
| Lossless round-trip | restored hash equals original hash | 100% |
| Visual mapping coverage | rendered objects mapped to canonical IDs / rendered objects | 100% |
| OCR CER/WER | edit distance / reference characters or words | benchmark by language |
| Layout overflow | clipped critical labels / critical labels | 0% |
| Collision rate | overlapping node boxes / all boxes | ≤1% prototype |
| Ratio deviation | relative error from target ratio | ≤1% where feasible |
| Reproducibility | same input/config → same canonical manifest/hash | 100% |
| Decode success | valid packages decoded / valid packages | 100% |
| Tamper detection | modified authenticated payloads rejected | 100% |
| Resource budget | time, memory, pixels, nodes | declared and bounded |

CER=(S+D+I)/N; WER uses word units. S=substitutions, D=deletions, I=insertions, N=reference units.
Coverage=Nmapped/Neligible.
Graph integrity=valid endpoint edges / all edges.
Relative ratio error=|rm-rt|/rt.

Track extraction confidence, OCR confidence, relation confidence, source reliability, measurement uncertainty, and human review separately. Never compress them into an opaque score.

PASS requires executed evidence. FAIL requires executed failure evidence. NOT RUN means no execution. BLOCKED means a dependency prevented execution.
