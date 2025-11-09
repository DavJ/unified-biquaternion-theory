import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
txt = (ROOT/"README.md").read_text(encoding="utf-8", errors="ignore").lower()

def test_readme_has_bq_vs_ct_section():
    assert "why biquaternionic time" in txt, "Add the 'Why biquaternionic time' section to README"

def test_readme_mentions_causality_limit():
    assert "psi->0" in txt or "ψ->0" in txt or r"\psi\to 0" in txt or "macroscopic causality" in txt, \
           "README should state that psi->0 restores standard QED and preserves causality"

def test_readme_states_necessity_for_alpha():
    need = "necessary technical device" in txt and ("alpha" in txt or "α" in txt)
    assert need, "README must state that T=t+iψ is a necessary technical device for a fit-free α derivation."
