import pytest
from pyshacl import validate
from rdflib import Graph

from build_data import DECK_DOCUMENTS, DOCUMENTS, load_graph


@pytest.mark.parametrize("name", DOCUMENTS)
def test_document_has_sources(name):
    assert DOCUMENTS[name], f"No source files found for document {name!r}"


@pytest.mark.parametrize("deck", DECK_DOCUMENTS)
def test_conforms_to_shapes(deck, ontology, correspondences, symbols, shapes):
    # Decks are checked together with the ontology and the shared correspondence and symbol
    # vocabularies, as consumers load them, so suits, ranks, symbols and links are visible.
    data = load_graph(deck) + ontology + correspondences + symbols
    conforms, _, report = validate(data, shacl_graph=shapes, advanced=True)
    assert conforms, report
