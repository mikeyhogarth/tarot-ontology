"""
Tests each provided data file against the test suite's SHACL standards.
"""

import pytest
from pyshacl import validate

from scripts.build_data import DECK_DOCUMENTS, DOCUMENTS, load_graph


@pytest.mark.parametrize("name", DOCUMENTS)
def test_document_has_sources(name):
    """
    Checks each of the document lookups has some files listed (in case someone
    creates a folder with no files in for example).
    """
    assert DOCUMENTS[name], f"No source files found for document {name!r}"


@pytest.mark.parametrize("deck", DECK_DOCUMENTS)
def test_conforms_to_shapes(deck, ontology, correspondences, symbols, shapes):
    """
    Checks each deck against the test suite's shacl shapes file to ensure it conforms
    to the expected standard.
    """
    data = load_graph(deck) + ontology + correspondences + symbols
    conforms, _, report = validate(data, shacl_graph=shapes, advanced=True)
    assert conforms, report
