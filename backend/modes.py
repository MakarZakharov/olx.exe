import sqlite3

def init_db():
    conn = sqlite3.connect('olx.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS slaves (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quality_of_work TEXT NOT NULL,
            description TEXT,
            image BLOB
        )
    ''')
    conn.commit()
    conn.close()

def init_users():
    conn = sqlite3.connect('olx.db')
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

def add_users(name, password):
    conn = sqlite3.connect('olx.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, password) VALUES (?, ?)
    ''', (name, password))
    conn.commit()
    conn.close()
def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def add_slaves(name, quality_of_work, description, image_path):
    conn = sqlite3.connect('olx.db')
    c = conn.cursor()
    image = convert_to_binary_data(image_path)
    c.execute('''
        INSERT INTO slaves (name, quality_of_work, description, image) VALUES (?, ?, ?, ?)
    ''', (name, quality_of_work, description, image))
    conn.commit()
    conn.close()

def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def retrieve_image(slave_id, output_path):
    conn = sqlite3.connect('olx.db')
    c = conn.cursor()
    c.execute('SELECT image FROM slaves WHERE id = ?', (slave_id,))
    image_data = c.fetchone()[0]
    write_to_file(image_data, output_path)
    conn.close()

# Инициализация базы данных
# init_db()
init_users()
# Добавление новой записи с изображением
add_slaves("vlad", "7", "cant python", "imeges/slave1.png")

# Извлечение и сохранение изображения в файл
# retrieve_image(1, "output_image.jpg")
add_users("egor","ee22")