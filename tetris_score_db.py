import sqlite3


# Erstellt Tabelle
def create_table(db):
    c = db.cursor()
    c.execute("""
                CREATE TABLE IF NOT EXISTS highscore(
                    id INTEGER PRIMARY KEY,
                    score int
                );
    """)
    db.commit()


# Gibt derzeitigen Highscore zurück (als Tupel einer Liste)
def get_highscore():
    db = sqlite3.connect('highscore_db.sqlite')
    create_table(db)
    c = db.cursor()
    c.execute('SELECT score FROM highscore;')
    r = c.fetchall()
    return r


# Setzt neuen Highscore falls höher
def new_highscore(new_score):
    db = sqlite3.connect('highscore_db.sqlite')
    create_table(db)
    c = db.cursor()
    old_score = get_highscore()
    if not old_score:
        c.execute('INSERT INTO highscore(score) VALUES (?);',(new_score,))
        db.commit()
    elif new_score > old_score[0][0]:
        c.execute('DELETE FROM highscore WHERE id = 1;')
        c.execute('INSERT INTO highscore(score) VALUES (?);',(new_score,))
        db.commit()
