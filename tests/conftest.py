"""
Shared pytest fixtures.
"""

from pathlib import Path

import pytest
from rdflib import Graph

from scripts.build_data import load_graph


@pytest.fixture(scope="session")
def ontology():
    return load_graph("ontology")


@pytest.fixture(scope="session")
def correspondences():
    return load_graph("correspondence")


@pytest.fixture(scope="session")
def symbols():
    return load_graph("symbol")


@pytest.fixture(scope="session")
def shapes():
    return Graph().parse(Path(__file__).parent / "shapes.ttl")
