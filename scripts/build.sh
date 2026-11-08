#!/usr/bin/env bash
# Build the whole site in three parts:
#
# 1) Build the data outputs themselves
# 2) Build the Widoco documentation
# 3) Build the Zensical documentation site
#
# Steps 1 and 2 generate their outputs into the zensical source 
# folder (docs/) - step 3 then builds the final site into site/.

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
uv run scripts/build_data.py
scripts/build_widoco.sh
uv run zensical build --clean --strict
