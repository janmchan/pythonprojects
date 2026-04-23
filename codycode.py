subjects = 'math', 'geometry', 'algebra', 'science', 'reading', 'writing'
#if i want to do math type in y
#else ask if i want to do gemetry, and on until writing
#if yes to any subect print a joke or pun about subject
#if i do not want a subject type n

answer = input('what subject do you like? ' + ", ".join(subjects) + ': ')

match answer:
    case 'math':
        print('math joke')
    case 'geometry':
        print('if you were an angle, you\'d be acute one')
    case _:
        print('I do not know that')