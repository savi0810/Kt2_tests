import sqlite3

def get_string_length(s: str) -> int:
    return len(s)

def save_string_to_file(content: str, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

class DatabaseManager:
    def __init__(self, db_path: str = ':memory:'):
        self.db_path = db_path
        self.connection = None
    
    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def disconnect(self):
        if self.connection:
            self.connection.close()