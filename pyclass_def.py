import sqlite3
import os

class WriteDB:
    """
    A simple class to demonstrate Object-Oriented Programming concepts
    while performing SQLite database operations.
    
    This class shows:
    - Constructor (__init__)
    - Instance variables (self.db_name, self.connection)
    - Methods (create_table, insert_user, etc.)
    - Encapsulation (private methods with _)
    """
    
    def __init__(self, database_name="example.db"):
        """
        Constructor - runs when creating a new instance of the class
        """
        self.db_name = database_name  # Instance variable
        self.connection = None
        self.cursor = None
        print(f"WriteDB instance created for database: {database_name}")
    
    def connect(self):
        """
        Method to establish database connection
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to database: {self.db_name}")
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def create_table(self):
        """
        Method to create a users table
        """
        if not self.connection:
            print("Error: Not connected to database")
            return False
        
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Users table created successfully")
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False
    
    def insert_user(self, name, email, age):
        """
        Method to insert a new user into the database
        """
        if not self._is_connected():  # Using private method
            return False
        
        try:
            insert_query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
            self.cursor.execute(insert_query, (name, email, age))
            self.connection.commit()
            print(f"User '{name}' inserted successfully")
            return True
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
            return False
    
    def insert_multiple_users(self, users_list):
        """
        Method to insert multiple users at once
        users_list should be a list of tuples: [(name, email, age), ...]
        """
        if not self._is_connected():
            return False
        
        try:
            insert_query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
            self.cursor.executemany(insert_query, users_list)
            self.connection.commit()
            print(f"Inserted {len(users_list)} users successfully")
            return True
        except sqlite3.Error as e:
            print(f"Error inserting multiple users: {e}")
            return False
    
    def get_all_users(self):
        """
        Method to retrieve all users from the database
        """
        if not self._is_connected():
            return []
        
        try:
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            return users
        except sqlite3.Error as e:
            print(f"Error retrieving users: {e}")
            return []
    
    def update_user_age(self, user_id, new_age):
        """
        Method to update a user's age
        """
        if not self._is_connected():
            return False
        
        try:
            update_query = "UPDATE users SET age = ? WHERE id = ?"
            self.cursor.execute(update_query, (new_age, user_id))
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"User ID {user_id} age updated to {new_age}")
                return True
            else:
                print(f"No user found with ID {user_id}")
                return False
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")
            return False
    
    def delete_user(self, user_id):
        """
        Method to delete a user by ID
        """
        if not self._is_connected():
            return False
        
        try:
            delete_query = "DELETE FROM users WHERE id = ?"
            self.cursor.execute(delete_query, (user_id,))
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"User ID {user_id} deleted successfully")
                return True
            else:
                print(f"No user found with ID {user_id}")
                return False
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
            return False
    
    def _is_connected(self):
        """
        Private method (starts with _) to check if database is connected
        This is meant for internal use only
        """
        if not self.connection:
            print("Error: Not connected to database. Call connect() first.")
            return False
        return True
    
    def close(self):
        """
        Method to close the database connection
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed")
        else:
            print("No active connection to close")
    
    def __del__(self):
        """
        Destructor - runs when the object is destroyed
        """
        if self.connection:
            self.connection.close()
        print("WriteDB instance destroyed")