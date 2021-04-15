f = open("results.txt","r")
newf = open("results_parsed.txt","w")
timings=[]
for line in f:
    if "runtime" in line:
        _=line.split()
        timings.append(_[-2])
        print(timings[-1])
string=""
for i in range(3):
    string+="|"
    string+=",".join(timings[i*3:(i+1)*3])
string+="|"
newf.write(string)
newf.close()
f.close()