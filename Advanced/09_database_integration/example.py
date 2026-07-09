import os
import sqlite3

# ----------------------------------------------------
# 1. Custom Database Context Manager
# ----------------------------------------------------
class SQLiteTransactionManager:
    """A context manager to handle database transactions safely."""
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Establish connection and return the connection/cursor
        self.conn = sqlite3.connect(self.db_name)
        # Enable foreign key support
        self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # An error occurred inside the 'with' block; rollback transaction
            print(f"Exception intercepted: {exc_val}. Rolling back database changes.")
            self.conn.rollback()
        else:
            # Transaction successful; commit changes
            self.conn.commit()
        # Close database connection
        self.conn.close()


# ----------------------------------------------------
# 2. Database schema setup and parameterized queries
# ----------------------------------------------------
db_file = "test.db"

# Cleanup previous test db if it exists
if os.path.exists(db_file):
    os.remove(db_file)

try:
    print("--- 1. Setting up Schema ---")
    with SQLiteTransactionManager(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
        """)
        print("Database schema created.")

    print("\n--- 2. Parameterized SQL insertions ---")
    with SQLiteTransactionManager(db_file) as conn:
        cursor = conn.cursor()
        
        # Safe Parameterized inserts
        users_to_add = [
            ("akshit", "akshit@company.com"),
            ("dev_user", "dev@company.com"),
            ("ops_leader", "ops@company.com")
        ]
        
        cursor.executemany(
            "INSERT INTO users (username, email) VALUES (?, ?)", 
            users_to_add
        )
        print(f"Inserted {len(users_to_add)} users.")

    print("\n--- 3. Querying database rows ---")
    with SQLiteTransactionManager(db_file) as conn:
        cursor = conn.cursor()
        
        # Retrieve all users
        cursor.execute("SELECT id, username, email FROM users")
        all_users = cursor.fetchall()
        print("All registered users:")
        for user_id, username, email in all_users:
            print(f"  [ID {user_id}] {username} - {email}")

        # Retrieve single user using parameters
        search_name = "dev_user"
        cursor.execute("SELECT email FROM users WHERE username = ?", (search_name,))
        row = cursor.fetchone()
        if row:
            print(f"Email for '{search_name}': {row[0]}")
        else:
            print(f"User '{search_name}' not found.")

    print("\n--- 4. Demonstrating transaction rollback ---")
    try:
        with SQLiteTransactionManager(db_file) as conn:
            cursor = conn.cursor()
            
            # Insert a user successfully
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("temp_user", "temp@company.com"))
            print("Inserted temp_user successfully.")
            
            # Force a database constraint error (username is UNIQUE)
            # This duplicate username will raise an IntegrityError
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("akshit", "duplicate@company.com"))
    except sqlite3.IntegrityError as e:
        print(f"Intercepted database integrity exception: {e}")

    # Verify that 'temp_user' was NOT committed to the database (rolled back)
    print("\nVerifying database state post-exception:")
    with SQLiteTransactionManager(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", ("temp_user",))
        row = cursor.fetchone()
        if row is None:
            print("  Confirmed: 'temp_user' was rolled back completely (transaction safety).")
        else:
            print("  Warning: 'temp_user' was committed!")

finally:
    # Cleanup the test db file
    if os.path.exists(db_file):
        os.remove(db_file)
        print("\nCleaned up temporary database file.")
