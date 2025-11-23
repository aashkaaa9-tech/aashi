import json
import os

u = []
b = []

if os.path.exists("data.json"):
    try:
        raw = open("data.json", "r").read()
        obj = json.loads(raw)
        u = obj["names"]
        b = obj["data"]
    except:
        pass

while True:
    print("1: user, 2: bill, 3: calc")
    i = input(">> ")

    if i == "1":
        n = input("name: ")
        u.append(n)
        
        d = {"names": u, "data": b}
        f = open("data.json", "w")
        f.write(json.dumps(d))
        f.close()
        
        
    if i == "2":
        try:
            amt = float(input("amt: "))
            what = input("for: ")
            who = input("payer: ")
            
            cnt = len(u)
            if cnt > 0:
                share = amt / cnt
                s = {}
                for p in u:
                    s[p] = share
                    
                new_b = {
                    "desc": what,
                    "total": amt,
                    "who": who,
                    "splits": s
                }
                b.append(new_b)
                
                d = {"names": u, "data": b}
                f = open("data.json", "w")
                f.write(json.dumps(d))
                f.close()
        except:
            print("bad input")

    if i == "3":
        bal = {}
        for p in u:
            bal[p] = 0
            
        for item in b:
            if item["who"] in bal:
                bal[item["who"]] += item["total"]
            
            for k in item["splits"]:
                if k in bal:
                    bal[k] -= item["splits"][k]

        cents = {}
        for p in bal:
            cents[p] = int(bal[p] * 100)

        out_lines = []
        
        for _ in range(999):
            neg_p = ""
            for k in cents:
                if cents[k] < -1:
                    neg_p = k
                    break
            
            pos_p = ""
            for k in cents:
                if cents[k] > 1:
                    pos_p = k
                    break
            
            if neg_p == "" or pos_p == "":
                break
                
            val = 0
            if abs(cents[neg_p]) < cents[pos_p]:
                val = abs(cents[neg_p])
            else:
                val = cents[pos_p]
                
            cents[neg_p] += val
            cents[pos_p] -= val
            
            s_val = str(val / 100.0)
            line = neg_p + " pays " + pos_p + " " + s_val
            out_lines.append(line)
            print(line)
            
        print("csv? y/n")
        c = input()

        if c == "y":
            f = open("out.csv", "w")
            f.write("from,to,amt\n")
            for l in out_lines:
                parts = l.split(" ")
                row = parts[0] + "," + parts[2] + "," + parts[3] + "\n"
                f.write(row)
            f.close()