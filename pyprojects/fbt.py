def foo(n):
    count = 1
    if n > 0:
        count += foo(n - 1) + foo(n - 1)
    print '1'
    print count


foo(5)
