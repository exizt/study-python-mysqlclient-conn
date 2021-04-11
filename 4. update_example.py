from MySQLdb import connect, OperationalError

try:
    # 커넥션 생성
    db = connect(user='webdb', password='webdb', host='localhost', port=3306, db='webdb', charset='utf8')

    cursor = db.cursor()  # cursor 생성

    # SQL 실행
    sql = '''
        update emaillist set 
            first_name = "마",
             last_name = "이콜"
        where no = %s
             '''
    count = cursor.execute(sql, (19, ))  # 주의 : 인자로 튜플을 넘겨야 하므로 , 를 넣어줘야 함.

    db.commit()  # 커밋

    # 자원 정리
    cursor.close()  # 커서 비우기
    db.close()  # 커넥션 비우기

    # 결과 보기
    print(f'실행결과: {count==1}')

    #for result in results:
    #    print(result)


except OperationalError as e:
    print(f'error: {e}')
