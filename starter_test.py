"""starter_test.py — the smoke test that proves the harness runs.

It confirms the loader works and that all four broken-response kinds are present in the fixture,
so you can build your handling against real failures. It passes out of the box. It does NOT
implement your validator/handler — that is your project. The skipped test below marks where your
work begins.
"""
import pytest
from fixture import load_cases, case

REQUIRED_KINDS = {"malformed_json", "refusal", "off_contract", "timeout"}


def test_fixture_loads():
    cases = list(load_cases())
    assert cases, "the fixture is empty"


def test_all_four_broken_kinds_are_present():
    kinds = {c["kind"] for c in load_cases()}
    missing = REQUIRED_KINDS - kinds
    assert not missing, f"the fixture is missing broken kinds: {missing}"


def test_each_broken_kind_is_findable():
    for kind in REQUIRED_KINDS:
        c = case(kind)
        assert c["kind"] == kind


@pytest.mark.skip(reason="YOUR WORK: implement your validator/handler and assert it degrades each broken case safely")
def test_your_handler_degrades_every_broken_case():
    # Example shape — replace with your project's handler:
    #   for c in load_cases():
    #       result = your_handler(c)
    #       assert result is not None            # never a crash
    #       if c["kind"] != "well_formed":
    #           assert result.is_fallback         # every broken case degrades safely
    ...
