import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            localidade TEXT NOT NULL
        )
    ''')
    # Inserindo os dados iniciais no banco de dados
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, localidade)
        VALUES
        ('curitiba_user', 'senha_curitiba', 'curitiba'),
        ('sp_user', 'senha_sp', 'sp')
    ''')
    conn.commit()
    conn.close()

# Execute esta função para criar o banco de dados e a tabela
create_database()
