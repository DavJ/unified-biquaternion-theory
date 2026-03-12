<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Track A: Purely Associative SU(3) Research Strategy

**Status:** Open research question — no claim of result yet.

## Central Question

> Can SU(3) emerge as a symmetry of the internal Θ-sector without octonions,
> i.e., purely from the associative structure ℂ⊗ℍ?

## Sub-questions

1. **Invariant subspace:** Does ℂ⊗ℍ admit a 3-dimensional invariant subspace
   under its natural automorphism action?

2. **Decomposition:** Can Θ decompose into 3 complex components under minimal
   coupling without requiring non-associative extension?

3. **Automorphism algebra:** Does Aut(ℂ⊗ℍ) contain an SU(3) subgroup?
   Known: Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂, whose maximal compact subgroup
   is U(2)×U(2). Preliminary analysis suggests no SU(3) subgroup — to be
   confirmed computationally.

4. **Stabilizer:** Can SU(3) appear as the stabilizer of a rank-3 tensor built
   from biquaternionic structure constants?

## Computational Approach

Run `tools/scan_associative_su3_candidates.py` to:
- Analyze the automorphism algebra of ℂ⊗ℍ
- Search for su(3)-like subalgebras in gl(2,ℂ)⊕gl(2,ℂ)
- Check whether any natural 8-dimensional representation decomposes as required

Output is written to `reports/associative_su3_scan.md`.

## Current Preliminary Assessment

Based on the known isomorphism ℂ⊗ℍ ≅ Mat(2,ℂ), the automorphism group is
[GL(2,ℂ)×GL(2,ℂ)]/ℤ₂. Its Lie algebra is gl(2,ℂ)⊕gl(2,ℂ) (real dimension 16),
which does **not** contain su(3) (real dimension 8) as a subalgebra in any
obvious embedding. This is consistent with the expectation that SU(3) requires
the non-associative octonionic extension.

**This assessment is provisional.** The computational scan (Track A script) must
confirm or refute it before any conclusion is stated as a result.

## Outcome Classification

| Result | Implication |
|--------|-------------|
| SU(3) ⊄ Aut(ℂ⊗ℍ) confirmed | Octonions are necessary for SU(3); supports Track B |
| SU(3) ⊂ Aut(ℂ⊗ℍ) found | Major result; eliminates need for Track B hypothesis |
| Stabilizer SU(3) found | Partial result; requires further physical interpretation |

## References

- `consolidation_project/appendix_E2_SM_geometry.tex` — full mathematical framework
- `research_tracks/octonionic_completion/hypothesis.md` — Track B
- `tools/scan_associative_su3_candidates.py` — computational scan
- `reports/associative_su3_scan.md` — scan results
