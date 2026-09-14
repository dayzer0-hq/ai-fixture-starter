# ai-fixture-starter

Starter skeleton for DZ0 **AI Engineer** briefs. A runnable harness that reads a **fixture** —
recorded model responses — instead of calling a live model. This is the seam the whole track is
built on: the graded run is deterministic, costs nothing, needs no API key, and — the point —
can hand your code a failure **on demand**.

## Run it (no key, no bill)

```bash
python3 --version      # 3.10+
git --version          # you submit every ticket as a pull request
pip install -r requirements.txt
pytest -q
```

The smoke tests pass out of the box: the loader works and all four broken-response kinds are
present. One test is skipped — that is where **your** validator/handler goes.

## The fixture is the curriculum

`data/fixture.jsonl` holds recorded responses. Some are well-formed; **four kinds are deliberately
broken**, and handling them IS the work. Each is a named case you can pull with
`fixture.case("<kind>")`:

  - **malformed_json** — a `raw` string that is not valid JSON; your parser must reject it, not crash.
  - **refusal** — the model returned prose ("I can't help with that"), not the JSON your contract asked for.
  - **off_contract** — valid JSON but breaking the contract (an extra field, a value outside the allowed set).
  - **timeout** — the call did not return; your code must fall back, not hang.

A fixture that only returned well-formed answers would turn every brief back into call-and-print
and you would write no failure handling, because nothing would ever fail. That is why the broken
cases are here and named.

## What this does NOT contain

No worked answer to any brief. `fixture.py` only LOADS responses — it does not parse, validate or
judge them. Choosing the validation, the eval, the fallback is your project.

## A fixture is not the model

Code that passes against these canned responses can still break on a real model — different token
counts, real latency, unicode, a refusal phrased in a way this fixture never produced. Green
fixture tests mean your handling is correct against the cases you have, not that it is
production-ready. If you run it live, the README's optional path uses **Ollama** (local, free, no
key) first; a paid key (your own, never DayZer0's) is an alternative, never required, and never
graded.

## Your project's data

Your brief names the specific data it gives you (e.g. `data/tickets.jsonl`, a labelled set, a
corpus). That per-brief data is provided WITH your project and lands in `data/`. The
`data/fixture.jsonl` here is the shared demonstrator: it shows the shape and the four failure
kinds every brief's fixture carries.

## Cost, tokens and repeats

Each well-formed case carries `cost_paise`, `latency_ms`, `prompt_tokens` and `completion_tokens`, and one case is an exact repeat — so the cost, token-trim, cache and latency briefs measure a real per-call cost and a real cache hit against the fixture, no live call needed.
