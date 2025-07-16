import sqlite3

def create_connection(db_name="banco.db"):
    """Establish and return a database connection."""
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """Create the 'hoteis' table if it does not exist."""
    sql = '''
    CREATE TABLE IF NOT EXISTS hoteis (
        hotel_id TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        estrelas REAL NOT NULL,
        diaria REAL NOT NULL,
        cidade TEXT NOT NULL
    );
    '''
    conn.execute(sql)
    print("Table 'hoteis' ensured.")

def insert_hotel(conn, hotel_id, nome, estrelas, diaria, cidade):
    """Insert a hotel into the table with parameterized query."""
    sql = "INSERT OR IGNORE INTO hoteis (hotel_id, nome, estrelas, diaria, cidade) VALUES (?, ?, ?, ?, ?);"
    conn.execute(sql, (hotel_id, nome, estrelas, diaria, cidade))
    print(f"Hotel '{nome}' inserted (if not already present).")

def list_hotels(conn):
    """Print all hotels in the table."""
    cursor = conn.execute("SELECT * FROM hoteis;")
    print("\nHotels registered:")
    for row in cursor:
        print(row)

def main():
    # Create database connection
    conn = create_connection()
    try:
        create_table(conn)

        insert_hotel(conn, 'alpha', 'Alpha Hotel', 4.3, 345.30, 'Rio de Janeiro')

        list_hotels(conn)

        conn.commit()
    finally:
        conn.close()
        print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
