#!/usr/bin/env bash
# Build the whole site into site/: generate the inputs into docs/ (the RDF downloads via
# build_data.py, the WIDOCO documentation via build_widoco.sh, which requires Docker), then
# build the site with zensical.

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
uv run scripts/build_data.py
scripts/build_widoco.sh
uv run zensical build --clean --strict
