from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

try:
    db = connect(user='webdb', password='webdb', host='localhost', port=3306, db='webdb',charset='utf8')

    cursor = db.cursor(DictCursor)

    sql = 'select no, first_name, last_name, email from emaillist order by no desc limit 1'
    cursor.execute(sql)

    result = cursor.fetchone()

    cursor.close()
    db.close()

    print(result)


except OperationalError as e:
    print(f'error: {e}')

