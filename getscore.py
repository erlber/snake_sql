import pymssql
from sqlvar import server, userName, pw, db 

def get_highscore():
    conn = pymssql.connect(server, userName, pw)
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute(f"USE {db}")
    sqlLine = "SELECT * FROM snake_hs"

    score = conn.cursor(as_dict = True)
    score.execute(sqlLine)

    highscore = 0
    for s in score:
        if s["score"] > highscore:
            highscore = s["score"]
    
    conn.close()
    return highscore