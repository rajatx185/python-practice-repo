import sys
some_var = "Educative"
print(sys.getrefcount(some_var))
another_var = some_var
print(sys.getrefcount(some_var))

