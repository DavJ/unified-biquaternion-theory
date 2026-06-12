# Patch notes — strict speculative placement

This patch corrects the placement of the prime-resonance material.

Earlier safe patch variants still had some generated tables under
`experiments/prime_resonance_channels/` and included an optional alpha-audit
verification note. To avoid mixing speculative cycle work with canonical or
research-track alpha material, this stricter patch puts everything related to
cycles, `139`, and `N0 = 137 * 139` under:

```text
speculative_extensions/prime_resonance_channels/
```

The script is also located there and writes its outputs into the local `data/`
subfolder.

Use:

```bash
unzip ubt_prime_resonance_strict_speculative_patch.zip -d .
python speculative_extensions/prime_resonance_channels/generate_prime_resonance_table.py
```

If an earlier patch was applied, optionally run:

```bash
bash scripts/cleanup_misplaced_prime_resonance_outputs.sh
```

This removes:

```text
experiments/prime_resonance_channels/
docs/reports/alpha_audit/alpha_layer2_kernel_repo64_verification.md
```

It does not touch canonical alpha files.
