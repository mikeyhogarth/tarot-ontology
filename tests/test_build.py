"""
Tests the build_data functionality
"""

import json
import pytest

from scripts.build_data import (
    DATA_DIRECTORY,
    DATA_OUTPUT_DIRECTORY,
    DOCUMENTS,
    PREFIXES,
    build,
)


@pytest.fixture(scope="module", name="site")
def fixture_site(tmp_path_factory):
    """
    Performs the build and writes the result to a temporary directory. Note that this is
    scoped to module so will only run once (in this module) and all tests use that result.
    If this fixture ever goes to live somewhere else (e.g. to conftest) then the scope will
    need to be changed.
    """
    tmp_root = tmp_path_factory.mktemp("tmp")
    return tmp_root, build(tmp_root)


@pytest.mark.parametrize("name", DOCUMENTS)
def test_build_writes_expected_files(name, site):
    """
    Checks each document is written out as a non-empty .ttl and .jsonld file at the
    path the published download links expect (data/<name>.ttl and data/<name>.jsonld).
    """
    tmp_root, written = site
    expected = tmp_root / DATA_OUTPUT_DIRECTORY
    assert written[name] == [expected / f"{name}.ttl", expected / f"{name}.jsonld"]
    for path in written[name]:
        assert path.is_file()
        assert path.read_text().strip(), f"{path} is empty"


@pytest.mark.parametrize("name", DOCUMENTS)
def test_jsonld_uses_project_context(name, site):
    """
    Checks the json-ld output declares our PREFIXES as its @context.
    """
    _, written = site
    jsonld = json.loads(written[name][1].read_text())
    assert jsonld["@context"] == PREFIXES


def test_every_source_file_is_published():
    """
    Checks every .ttl file under data/ belongs to some document in DOCUMENTS (and
    vice versa), so a new file or deck can't be silently left out of the build.
    """
    on_disk = set(DATA_DIRECTORY.rglob("*.ttl"))
    published = {path for paths in DOCUMENTS.values() for path in paths}
    assert on_disk == published
