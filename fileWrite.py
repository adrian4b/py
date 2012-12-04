import datetime

now = datetime.datetime.now()
try:
    f = open('./testing.txt', 'w')
    f.write('this is a file test')
    f.write(str(now))
finally:
    f.close()
