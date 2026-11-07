"""Build the RDF downloads (.ttl and .jsonld) for every published document into docs/data/ (zensical copies them into the site)."""

from pathlib import Path

from rdflib import Graph

ROOT = Path(__file__).parent.parent
DATA_DIRECTORY = ROOT / "data"
DECKS_DIRECTORY = DATA_DIRECTORY / "decks"
VOCABS_DIRECTORY = DATA_DIRECTORY / "vocabs"
OUTPUT_ROOT = ROOT / "docs"
DATA_OUTPUT_DIRECTORY = "data"  # subfolder of the site holding the RDF downloads
DECK_NAMES = ["rws", "marseille", "sola-busca"]
DECK_DOCUMENTS = [f"deck/{deck}" for deck in DECK_NAMES]

PREFIXES: dict[str, str] = {
    "tarot": "https://w3id.org/tarot/ontology#",
    "corr": "https://w3id.org/tarot/correspondence#",
    "symbol": "https://w3id.org/tarot/symbol#",
    "rws": "https://w3id.org/tarot/deck/rws#",
    "mar": "https://w3id.org/tarot/deck/marseille#",
    "sb": "https://w3id.org/tarot/deck/sola-busca#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "void": "http://rdfs.org/ns/void#",
    "vann": "http://purl.org/vocab/vann/",
    "bibo": "http://purl.org/ontology/bibo/",
    "schema": "https://schema.org/",
}

DOCUMENTS: dict[str, list[Path]] = {
    "ontology": [DATA_DIRECTORY / "ontology.ttl"],
    "correspondence": [VOCABS_DIRECTORY / "correspondences.ttl"],
    "symbol": [VOCABS_DIRECTORY / "symbols.ttl"],
    **{
        f"deck/{name}": sorted((DECKS_DIRECTORY / name).glob("*.ttl"))
        for name in DECK_NAMES
    },
}


def load_graph(name: str) -> Graph:
    """load all graphs for a particular document into an rdflib graph and return them"""
    g = Graph()
    for path in DOCUMENTS[name]:
        g.parse(path)
    return g


def build(output_dir: Path = OUTPUT_ROOT) -> dict[str, list[Path]]:
    """write turtle and json-ld files for each document; return the files written per document"""
    written: dict[str, list[Path]] = {}
    for name in DOCUMENTS:
        g = load_graph(name)
        for prefix, namespace in PREFIXES.items():
            g.bind(prefix, namespace, override=True, replace=True)

        base = output_dir / DATA_OUTPUT_DIRECTORY / name
        base.parent.mkdir(parents=True, exist_ok=True)
        ttl = base.parent / f"{base.name}.ttl"
        jsonld = base.parent / f"{base.name}.jsonld"

        g.serialize(ttl, format="turtle")
        g.serialize(jsonld, format="json-ld", context=PREFIXES, auto_compact=True)
        written[name] = [ttl, jsonld]

    return written


if __name__ == "__main__":
    for name, paths in build().items():
        for path in paths:
            print(f"{name}: {path.relative_to(ROOT)}")
