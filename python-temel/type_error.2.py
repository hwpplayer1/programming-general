def foo():
    return 10 + 'ali'
try:
    foo()
except ValueError:
    print('ValueError occured...')
except TypeError:
    print('TypeError occured...')
print('continues...')
