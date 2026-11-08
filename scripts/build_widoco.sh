#!/usr/bin/env bash
# Generate the WIDOCO ontology documentation (requires Docker) into a gitignored folder
# within the zensical source folder (docs/reference/).

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

# WIDOCO always writes its own re-serialisation of the ontology, but we want to treat our published
# version as the canonical RDF. This command drops WIDOCO's copies and its readme.md, which
# zensical would otherwise render as a page in our docs.
rm -f "$ROOT"/docs/reference/ontology.{ttl,jsonld,nt,owl} "$ROOT/docs/reference/readme.md"
