import mysql.connector

goDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bbb'
)

goCursor = goDb.cursor()


def saveUser(psName: str, psSurname: str, psUserName: str, psPhoneNum: str, pnBarberId: int, pnTelegramID: int):
    vsSql = """INSERT INTO user (`name`, `surname`, `user_name`, `phone`, `barber`, `telegram_id`)
                VALUES (%s, %s, %s, %s, %s, %s);"""

    vaVaL = (psName, psSurname, psUserName, psPhoneNum, pnBarberId, pnTelegramID)

    goCursor.execute(vsSql, vaVaL)

    goDb.commit()

    return True


def getUserByTgID(pnTelegramID: int):
    vsSql = f"""SELECT * FROM user WHERE telegram_id = {pnTelegramID}"""

    goCursor.execute(vsSql)

    vRes = goCursor.fetchone()

    return vRes


def deleteUserByID(pnTelegramID: int):
    vsSql = f"""DELETE FROM user WHERE telegram_id = {pnTelegramID}"""

    goCursor.execute(vsSql)

    goDb.commit()

    return True


def correctAutoIncrement(pnNumID):
    vsSql = f"""ALTER TABLE user AUTO_INCREMENT = {pnNumID} ;"""
    goCursor.execute(vsSql)
    goDb.commit()
    print('Auto increment changed')


print(getUserByTgID(431510980))
