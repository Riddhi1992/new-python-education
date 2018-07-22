def count_dict(mystring):
    d = {}
    for w in mystring:
        d[w] = mystring.count(w)
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring='qwertyqweryyyy'
count_dict(mystring)