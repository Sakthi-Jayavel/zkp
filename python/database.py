import sqlite3

conn = sqlite3.connect("assets.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        asset_id TEXT PRIMARY KEY,
        state TEXT,
        owner TEXT,
        value REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id TEXT,
        event TEXT,
        result TEXT
    )
    """)
    conn.commit()

def save_asset(asset):
    cursor.execute("""
    INSERT OR REPLACE INTO assets VALUES (?, ?, ?, ?)
    """, (asset.asset_id, asset.state, asset.owner, asset.value))
    conn.commit()

def log_event(asset_id, event, result):
    cursor.execute("""
    INSERT INTO events (asset_id, event, result) VALUES (?, ?, ?)
    """, (asset_id, event, result))
    conn.commit()