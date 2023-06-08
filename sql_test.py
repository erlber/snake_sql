import pymssql

def add_new_score(sqlLine):
    server = "192.168.15.15\\IT22"
    userName = "sa"
    pw = "123QWEr"
    db = "db_eb_1im"

    conn = pymssql.connect(server, userName, pw)
    conn.autocommit(True)
    useDb = f"USE {db}"
    cursor = conn.cursor()
    cursor.execute(useDb)
    cursor.execute(sqlLine)

    conn.close()

    


name = "pelle"
score = 99
sqlLine = f"INSERT INTO snake_hs (score, playerName) VALUES({score}, '{name}')"

add_new_score(sqlLine)



    