def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        #if not
        if not line:break
        function(line)
    file.close()
