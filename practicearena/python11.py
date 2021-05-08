given_name,given_college,given_stream,given_gender = map(str,input().split())

def task(**kwargs):
    if kwargs["d"] == "male":
        print(kwargs["a"],"is studying at",kwargs["b"],"he took the stream",kwargs["c"])
    elif kwargs["d"] == "female":
        print(kwargs["a"],"is studying at",kwargs["b"],"she took the stream",kwargs["c"])
    else:
        print(kwargs["a"], "is studying at", kwargs["b"], "they took the stream", kwargs["c"])

task(a = given_name,b = given_college,c = given_stream,d = given_gender)