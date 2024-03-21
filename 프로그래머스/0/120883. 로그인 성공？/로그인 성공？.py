def solution(id_pw, db):
    tempdb = dict(db)
    
    for x in tempdb.keys():
        if(id_pw[0] == x):
            if(id_pw[1] == tempdb[x]):
                return "login"
            else:
                return "wrong pw"
    return "fail"