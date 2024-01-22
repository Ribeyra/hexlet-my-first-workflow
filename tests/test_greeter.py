from workflow_course.greeter import greeter

if greeter() != 'Hello':
    raise Exception('fail')

print('pass')
