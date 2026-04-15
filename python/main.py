import random
from src.asset import Asset
from src.database import init_db
from src.event_processor import handle_event

init_db()

valid_flow = ["REGISTER", "IDENTIFY", "VERIFY", "MARK_ELIGIBLE", "TOKENIZE"]
invalid_events = ["TOKENIZE", "VERIFY"]

accepted = 0
rejected = 0

for i in range(100):
    asset = Asset(f"ASSET_{i:03d}", "gold", f"owner_{i}", random.randint(50, 150), "vault")

    use_invalid = random.random() < 0.2

    if use_invalid:
        flow = ["REGISTER", random.choice(invalid_events)]
    else:
        flow = valid_flow

    for event in flow:
        result = handle_event(asset, event)
        if result == "ACCEPTED":
            accepted += 1
        else:
            rejected += 1
            break

print("Simulation Results")
print("Accepted:", accepted)
print("Rejected:", rejected)