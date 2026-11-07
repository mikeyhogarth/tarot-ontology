# Developing

This is a `uv` project and therefore requires [uv](https://docs.astral.sh/uv/) (Python 3.14+) to be installed. Building the ontology documentation also requires Docker.

```sh
# install dependencies
uv sync

# Build site
./scripts/build.sh

# Run site locally
uv run zensical serve
```

The site is built in three parts: first it builds the RDF downloads themselves (the source for which is in `data/`), then the ontology documentation (generated from the ontology itself using [WIDOCO](https://github.com/dgarijo/Widoco)) and finally the hand-written docs via [Zensical](https://zensical.org/) (the source for which is in `docs/`).

## Running the tests

Run tests via [pytest](https://docs.pytest.org/en/stable/).

```sh
uv run pytest
```

The tests themselves are mostly driven via a SHACL file (`tests/shapes.ttl`) which exists to ensure that the ontology and any accompanying data files are of high quality.
