"""fixture.py — the fixture LOADER for the AI Engineer track.

This is a SEAM, not a model. The graded run reads recorded responses from data/fixture.jsonl
instead of calling a live model, so your work is deterministic and free — and so the failures
your code must handle are present ON DEMAND. This loader hands you each recorded response,
including the deliberately broken ones. It does NOT parse, validate or judge them — that is your
project. Choosing the validation is the work; this file only gives you the raw material.
"""
import json
import os

_HERE = os.path.dirname(__file__)


def load_cases(path=None):
    """Yield each recorded case as a dict. A case is one of:
      - well_formed:   has a `response` dict.
      - malformed_json: has a `raw` string that is NOT valid JSON.
      - refusal:        has a `raw` string that is prose, not JSON.
      - off_contract:   has a `response` dict that breaks the contract (extra/invalid fields).
      - hallucinated_citation (RAG): a `response` citing a source not in the corpus.
      - timeout:        has `error == "timeout"` and no response.
    The `kind` field names which — use it to find a case to test against, e.g.
        next(c for c in load_cases() if c["kind"] == "timeout")
    """
    path = path or os.path.join(_HERE, "data", "fixture.jsonl")
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def case(kind, path=None):
    """Return the first recorded case of a given kind. Raises if there is none."""
    for c in load_cases(path):
        if c.get("kind") == kind:
            return c
    raise KeyError(f"no fixture case of kind {kind!r}")
