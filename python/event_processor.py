from src.state_machine import process_event
from src.database import save_asset, log_event

def handle_event(asset, event):
    result = process_event(asset, event)
    save_asset(asset)
    log_event(asset.asset_id, event, result)
    return result