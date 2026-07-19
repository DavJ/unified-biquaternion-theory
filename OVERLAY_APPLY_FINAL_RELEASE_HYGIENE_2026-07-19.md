# Apply final release hygiene overlay

Run from the repository root:

```bash
unzip -o UBT_FINAL_RELEASE_HYGIENE_EXACT_ROOT_OVERLAY_2026-07-19.zip

while IFS= read -r path; do
  [ -n "$path" ] && rm -f -- "$path"
done < DELETE_PATHS_FINAL_RELEASE_HYGIENE_2026-07-19.txt

sha256sum -c OVERLAY_MANIFEST_FINAL_RELEASE_HYGIENE_2026-07-19.sha256
```

The explicit deletion step is required because ZIP extraction cannot remove an
already existing file.
