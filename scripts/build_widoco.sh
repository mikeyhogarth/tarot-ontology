#!/usr/bin/env bash
# Generate the WIDOCO ontology documentation (requires Docker) into docs/reference/, where zensical
# copies it into the site as-is. Safe to run at any time and in any order relative to zensical.
# The RDF downloads come from build_data.py.

set -euo pipefail
WIDOCO_IMAGE="ghcr.io/dgarijo/widoco:v1.4.26"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

rm -rf "$ROOT/docs/reference"

docker run --rm --platform linux/amd64 \
  -v "$ROOT:/usr/local/widoco/repo" \
  "$WIDOCO_IMAGE" \
  -ontFile repo/data/ontology.ttl -outFolder repo/docs/reference \
  -uniteSections -lang en -rewriteAll \
  -confFile repo/widoco/config.properties -getOntologyMetadata \
  -noPlaceHolderText -doNotDisplaySerializations

# WIDOCO always writes its own re-serialisation of the ontology. The canonical RDF is
# data/ontology.* (put there by scripts/build_data.py), so drop WIDOCO's copies. Also drop its
# readme.md, which zensical would otherwise render as a stray page.
rm -f "$ROOT"/docs/reference/ontology.{ttl,jsonld,nt,owl} "$ROOT/docs/reference/readme.md"
