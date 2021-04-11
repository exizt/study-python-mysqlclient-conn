import model


def run_list():
    results = model.findall()
    for index, result in enumerate(results):
        print(f'{index+1}:{result["first_name"]}{result["last_name"]}:{result["email"]}')


def run_add():
    firstname = input('first name:')
    lastname = input('last name:')
    email = input('email:')

    model.insert(firstname, lastname, email)

    run_list()


def run_delete():
    email = input('email:')
    model.deletebyemail(email)
    run_list()


def main():
    while True:
        cmd = input('(l)목록, (a)추가, (d)삭제, (q)종료 >')

        if cmd == 'q':
            break

        elif cmd == 'l':
            run_list()

        elif cmd == 'a':
            run_add()

        elif cmd == 'd':
            run_delete()
        else:
            print('알수없는 메뉴입니다.')


if __name__ == '__main__':
    main()