from MySQLdb import connect, OperationalError

try:
    # 커넥션 생성. user = DB 유저, db = DB 명
    db = connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')

    print('ok')

except OperationalError as e:
    print(f'error: {e}')
