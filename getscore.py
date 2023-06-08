import pymssql
from mssqlvariabler import server, password, user, database

def get_highscore():
    # Kobler til databasen
    conn = pymssql.connect(server, user, password)
    # Setter på autolagring
    conn.autocommit(True)
    # Lager peker inn til databasen
    cursor = conn.cursor()
    cursor.execute(f"USE {database}")
    score = conn.cursor(as_dict=True)
    sqlLine = "SELECT * FROM snake_hs"
    score.execute(sqlLine)

    highScore = 0
    for s in score:
        if s["score"] > highScore:
            highScore = s["score"]
    
    score.close()
    return highScore