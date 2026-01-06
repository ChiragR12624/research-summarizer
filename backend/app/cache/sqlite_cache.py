import sqlite3
import json
from pathlib import Path

DB_PATH = Path("data/cache.db")
DB_PATH.parent.mkdir(exist_ok=True)


class CacheDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS papers (
                paper_id TEXT PRIMARY KEY,
                data TEXT
            )
        """)
        self.conn.commit()

    def store_paper(self, paper_id: str, data: dict):
        self.conn.execute(
            "INSERT OR REPLACE INTO papers (paper_id, data) VALUES (?, ?)",
            (paper_id, json.dumps(data))
        )
        self.conn.commit()

    def get_paper(self, paper_id: str):
        cur = self.conn.execute(
            "SELECT data FROM papers WHERE paper_id = ?",
            (paper_id,)
        )
        row = cur.fetchone()
        return json.loads(row[0]) if row else None
