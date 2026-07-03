import sqlite3
from pathlib import Path

# Create the data directory if it doesn't exist
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATA_DIR / "crimson_ledger.db"


class Database:

    def get_connection(self):
        return sqlite3.connect(DATABASE_PATH)

    def create_tables(self):

        with self.get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS market_snapshots (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

                item_key TEXT NOT NULL,

                lowest_price INTEGER NOT NULL,

                buy500_average REAL NOT NULL,

                listing_count INTEGER NOT NULL,

                total_quantity INTEGER NOT NULL

            )
            """)

            connection.commit()

    def save_snapshot(
        self,
        item_key,
        lowest_price,
        buy500_average,
        listing_count,
        total_quantity
    ):

        with self.get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
            INSERT INTO market_snapshots (

                item_key,
                lowest_price,
                buy500_average,
                listing_count,
                total_quantity

            )
            VALUES (?, ?, ?, ?, ?)
            """, (

                item_key,
                lowest_price,
                buy500_average,
                listing_count,
                total_quantity

            ))

            connection.commit()

    def get_latest_snapshot(self, item_key):

        with self.get_connection() as connection:

            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM market_snapshots
                WHERE item_key = ?
                ORDER BY timestamp DESC
                LIMIT 1
            """, (item_key,))

            row = cursor.fetchone()

            if row is None:
                return None

            return dict(row)

    def get_snapshot_history(self, item_key, limit=100):

        with self.get_connection() as connection:

            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM market_snapshots
                WHERE item_key = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (item_key, limit))

            rows = cursor.fetchall()

            return [dict(row) for row in rows]