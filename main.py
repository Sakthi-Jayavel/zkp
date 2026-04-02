from src.asset import Asset
from src.database import init_db
from src.event_processor import handle_event

init_db()

asset = Asset("A001", "gold", "owner1", 120, "vault")

print(handle_event(asset, "REGISTER"))
print(handle_event(asset, "IDENTIFY"))
print(handle_event(asset, "VERIFY"))
print(handle_event(asset, "MARK_ELIGIBLE"))
print(handle_event(asset, "TOKENIZE"))