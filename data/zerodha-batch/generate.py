"""Deterministic generator for the 10,000-message batch. A generator, not a committed 10k file:
batching and cost-at-scale are meaningless at 30 rows, and this is smaller than the data.

    python data/zerodha-batch/generate.py > data/zerodha-batch/messages.jsonl

Produces 10,000 messages with MANY repeats (so caching pays) drawn from a fixed pool — same output
every run, no randomness, no network.
"""
import json, sys
POOL = ["how do I add funds","why is my order rejected","kyc pending status","how to withdraw",
        "what are the brokerage charges","reset my password","2fa not working","how to sell shares",
        "margin shortfall","account opening stuck","how to add a nominee","what is an SIP"]
def main(n=10000):
    for i in range(n):
        q = POOL[(i * 7) % len(POOL)]           # deterministic, heavy repeats
        print(json.dumps({"id": f"z{i}", "message": q}))
if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10000)
