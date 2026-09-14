"""fixture.py — loader for namespaced fixtures. Each brief's files live under data/<namespace>/.
This LOADS; it does not validate, retrieve, score, route or dedupe — that is your project."""
import json, os
_H = os.path.dirname(__file__)

def namespaces():
    d = os.path.join(_H, "data")
    return sorted(n for n in os.listdir(d) if os.path.isdir(os.path.join(d, n)))

def load(ns, filename):
    """Load a jsonl file from your brief's namespace, e.g. load("meesho", "tickets.jsonl")."""
    with open(os.path.join(_H, "data", ns, filename), encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]

def kinds(ns, filename):
    return {r.get("kind") for r in load(ns, filename) if "kind" in r}
