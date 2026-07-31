import sqlite3
import json
from datetime import datetime

class MemoryBCellAgent:
    def __init__(self, db_path="b_cell_memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memory_cells (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    problem_signature TEXT NOT NULL UNIQUE,
                    formulation TEXT NOT NULL,
                    success_score REAL NOT NULL,
                    metadata TEXT,
                    timestamp TEXT NOT NULL
                )
            ''')
            conn.commit()

    def memorize(self, problem_signature: str, formulation: dict, success_score: float, metadata: dict = None):
        timestamp = datetime.now().isoformat()
        formulation_json = json.dumps(formulation)
        metadata_json = json.dumps(metadata) if metadata else "{}"

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT success_score FROM memory_cells WHERE problem_signature = ?', (problem_signature,))
            existing_record = cursor.fetchone()

            if existing_record:
                if success_score > existing_record[0]:
                    cursor.execute('''
                        UPDATE memory_cells 
                        SET formulation = ?, success_score = ?, metadata = ?, timestamp = ?
                        WHERE problem_signature = ?
                    ''', (formulation_json, success_score, metadata_json, timestamp, problem_signature))
            else:
                cursor.execute('''
                    INSERT INTO memory_cells (problem_signature, formulation, success_score, metadata, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (problem_signature, formulation_json, success_score, metadata_json, timestamp))
            conn.commit()

    def recall(self, problem_signature: str) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT formulation FROM memory_cells WHERE problem_signature = ?', (problem_signature,))
            result = cursor.fetchone()
            if result:
                return json.loads(result[0])
            return None

if __name__ == "__main__":
    # Sistemin kendi kendini dogrulamasi icin kucuk bir test blogu
    agent = MemoryBCellAgent()
    agent.memorize("init_test", {"status": "active", "layer": "memory"}, 1.0, {"module": "Biokernel"})
    print(f"[Memory B-Cell] Sistem aktif. Dogrulama: {agent.recall('init_test')}")
