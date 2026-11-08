import pytest
from rdflib import Graph
from rdflib.compare import isomorphic

from build_data import DOCUMENTS, build, load_graph

FORMATS = {"ttl": "turtle", "jsonld": "json-ld"}


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    return build(tmp_path_factory.mktemp("site"))


@pytest.mark.parametrize("extension", FORMATS)
@pytest.mark.parametrize("name", DOCUMENTS)
def test_round_trip(name, extension, site):
    path = next(p for p in site[name] if p.suffix == f".{extension}")
    parsed = Graph().parse(path, format=FORMATS[extension])
    source = load_graph(name)
    assert len(parsed) == len(source)
    assert isomorphic(parsed, source)
