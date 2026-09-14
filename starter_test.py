"""Smoke test: every namespace ships a model_fixture with the four broken kinds. Passes out of the
box; writing the validator/handler is your project."""
import os, glob, json
D=os.path.join(os.path.dirname(__file__),"data")
FOUR={"malformed_json","refusal","off_contract","timeout"}
def test_each_namespace_has_a_model_fixture_with_the_four_broken_kinds():
    nss=[n for n in os.listdir(D) if os.path.isdir(os.path.join(D,n))]
    assert nss, "no namespaces"
    for n in nss:
        f=os.path.join(D,n,"model_fixture.jsonl")
        assert os.path.exists(f), f"{n}: no model_fixture.jsonl"
        ks={json.loads(l).get("kind") for l in open(f) if l.strip()}
        assert FOUR<=ks, f"{n}: missing broken kinds {FOUR-ks}"
