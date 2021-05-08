name,college = map(str,input().split())

def test_fun(*name):
    print(name[0],"studies in",name[1])

test_fun(name,college)