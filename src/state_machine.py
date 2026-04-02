ALLOWED_TRANSITIONS = {
    "UNREGISTERED": ["REGISTER"],
    "REGISTERED": ["IDENTIFY"],
    "IDENTIFIED": ["VERIFY"],
    "VERIFIED": ["MARK_ELIGIBLE"],
    "ELIGIBLE_FOR_TOKENIZATION": ["TOKENIZE"],
    "TOKENIZED": []
}

NEXT_STATE = {
    ("UNREGISTERED", "REGISTER"): "REGISTERED",
    ("REGISTERED", "IDENTIFY"): "IDENTIFIED",
    ("IDENTIFIED", "VERIFY"): "VERIFIED",
    ("VERIFIED", "MARK_ELIGIBLE"): "ELIGIBLE_FOR_TOKENIZATION",
    ("ELIGIBLE_FOR_TOKENIZATION", "TOKENIZE"): "TOKENIZED"
}

def process_event(asset, event):
    if event not in ALLOWED_TRANSITIONS.get(asset.state, []):
        return "REJECTED"

    asset.state = NEXT_STATE[(asset.state, event)]

    if asset.state == "TOKENIZED":
        asset.is_tokenized = True

    return "ACCEPTED"