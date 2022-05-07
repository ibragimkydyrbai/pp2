from functions import execute
command = ''

while command != 'quit':
    command = input("\nEnter a command:")
    
    if command == 'select':
        table = input('table:')
        order = input('order:')
        limit = input('limit:')
        offset = input('offset:')
        execute('select_pag', table=table, order=order, limit=limit, offset=offset)

    elif command == 'create':
        table = input('table:')
        execute('create', name=table)

    elif command == 'insert':
        table = input('table:')
        name = input('name:')
        surname = input('surname:')
        phone = input('phone:')
        execute('insert', table=table, name=name, surname=surname, phone=phone)

    elif command == 'insert list':
        list = []
        n = int(input("Enter the size of the list:"))
        table = input('table:')
        for i in range(n):
            name = input('name:')
            surname = input('surname:')
            phone = input('phone:')
            list.append((name, surname, phone))
            
        execute('insert', list=list, table=table)
    
    elif command == 'upload':
        path = input('path:')
        table = input('table:')
        execute('upload', path=path, table=table)
    
    elif command == 'update':
        table = input('table:')
        name = input('name:')
        surname = input('surname:')
        phone = input('phone:')
        execute('update', table=table, name=name, surname=surname, phone=phone)

    elif command == 'delete':
        table = input('table:')
        phone = input('phone:')
        execute('delete', table=table, phone=phone)

    elif command == 'search':
        table = input('table:')
        pattern = input('pattern:')
        execute('search', table=table, pattern=pattern)

    elif command != 'quit':
        print('Invalid command!')