from PyInquirer import prompt

def isComfirmed():
    answer = prompt([{
        'type': 'confirm',
        'message': 'Вы уверены?',
        'name': 'delete',
        'default': False,
    }])
    return answer['delete']
