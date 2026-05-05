with open("requirements.txt") as f :
    req=f.read()
    req=req.split()

    for i,name in enumerate(req):
        print(f"{i+1}.{name}")