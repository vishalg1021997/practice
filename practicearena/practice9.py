input_name,input_college,input_stream = map(str,input().split(","))
def details(stream,name="rohan rathore",college="MIT"):
    print("name=",name,"stream=",stream,"college=",college)
    return name,stream,college

if input_name == "rohan" :
    input_name = "rohan rathore"
if input_college == "mit":
    input_college = "MIT"

details(input_stream,input_name,input_college,)


