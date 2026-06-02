'''
Task 1: Create a New SQLite Database
'''

import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' is already in the database.")

def add_subscriber(cursor, name, address):
    try:
        existing = cursor.execute(
            "SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address)
        ).fetchone()
        if existing:
            print(f"Subscriber '{name}' at '{address}' is already in the database.")
            return
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' is already in the database.")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        existing = cursor.execute(
            "SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        ).fetchone()
        if existing:
            print(f"Subscription already exists, skipping.")
            return
        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.IntegrityError:
        print(f"Subscription is already in the database.")


with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 2: Define Database Structure
    cursor.execute('''CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expiration_date TEXT NOT NULL,
        magazine_id INTEGER NOT NULL,
        subscriber_id INTEGER NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES magazines(id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id))''')

    # Task 3: Populate Tables with Data
    add_publisher(cursor, "The Arena Group")
    add_publisher(cursor, "National Geographic Society")
    add_publisher(cursor, "Meredith")

    arena_id = cursor.execute("SELECT id FROM publishers WHERE name = 'The Arena Group'").fetchone()[0]
    natgeo_id = cursor.execute("SELECT id FROM publishers WHERE name = 'National Geographic Society'").fetchone()[0]
    meredith_id = cursor.execute("SELECT id FROM publishers WHERE name = 'Meredith'").fetchone()[0]

    add_magazine(cursor, "Sports Illustrated", arena_id)
    add_magazine(cursor, "Men's Journal", arena_id)
    add_magazine(cursor, "National Geographic", natgeo_id)
    add_magazine(cursor, "People", meredith_id)
    add_magazine(cursor, "Time", meredith_id)

    add_subscriber(cursor, "Misha Mikelson", "123 Atlantic Ave, Brooklyn")
    add_subscriber(cursor, "Ada Osman", "456 Grand Concourse, Bronx")
    add_subscriber(cursor, "Shanida Washington", "789 Broadway, Manhattan")

    misha_id = cursor.execute("SELECT id FROM subscribers WHERE name = 'Misha Mikelson'").fetchone()[0]
    ada_id = cursor.execute("SELECT id FROM subscribers WHERE name = 'Ada Osman'").fetchone()[0]
    shanida_id = cursor.execute("SELECT id FROM subscribers WHERE name = 'Shanida Washington'").fetchone()[0]

    si_id = cursor.execute("SELECT id FROM magazines WHERE name = 'Sports Illustrated'").fetchone()[0]
    mj_id = cursor.execute("SELECT id FROM magazines WHERE name = \"Men's Journal\"").fetchone()[0]
    ng_id = cursor.execute("SELECT id FROM magazines WHERE name = 'National Geographic'").fetchone()[0]
    people_id = cursor.execute("SELECT id FROM magazines WHERE name = 'People'").fetchone()[0]
    time_id = cursor.execute("SELECT id FROM magazines WHERE name = 'Time'").fetchone()[0]

    add_subscription(cursor, misha_id, si_id, "2026-12-31")
    add_subscription(cursor, misha_id, ng_id, "2026-06-30")
    add_subscription(cursor, ada_id, mj_id, "2025-11-30")
    add_subscription(cursor, ada_id, people_id, "2026-03-31")
    add_subscription(cursor, shanida_id, time_id, "2026-08-31")
    add_subscription(cursor, shanida_id, si_id, "2025-12-31")

    # Task 4: Write SQL Queries
    rows = cursor.execute("SELECT * FROM subscribers").fetchall()
    for row in rows:
        print(row)

    rows = cursor.execute("SELECT * FROM magazines ORDER BY name").fetchall()
    for row in rows:
        print(row)

    rows = cursor.execute("""
        SELECT magazines.name, publishers.name 
        FROM magazines 
        JOIN publishers ON magazines.publisher_id = publishers.id
        WHERE publishers.name = 'The Arena Group'
    """).fetchall()
    for row in rows:
        print(row)

    conn.commit()