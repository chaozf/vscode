x = 1
def a():
    x = 25
    print('\n local x in a is',x,'after entering a')
    x += 1
    print('loacal x in a is ',x,'before exiting a')
def b():
    global x
    print('\n local x in x is',x,'after entering b')
    x *= 10
    print('loacal x in a is ',x,'before exiting b')

print('global x is',x)

x = 7
print('global x is',x)

a()
b()
a()
b()