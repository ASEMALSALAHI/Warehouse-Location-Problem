def getFile(dosya):
    txt = open(dosya, "r")
    line=txt.readline().split(" ")
    deposay=int(line[0])
    depolar,kisiler,kisi=[],[],[]
    
    for i in range(deposay):
        depoline=txt.readline().split(" ")
        depolar.append([depoline[0],depoline[1].strip(),0])
    txt=txt.read().split("\n")
    for i in range(len(txt)-1):
        if(i%2==0):
            kisi.append(int(txt[i]))
        else:
            al=txt[i].split(" ")
            for j in range(len(al)):
                kisi.append(float(al[j]))
            kisiler.append(kisi)
            kisi=[]
    OptimalControl(depolar,kisiler)
def OptimalControl(depolar,kisiler):
    totalmaliyet=0
    aw=[]
    for i in range(len(kisiler)):
        minmaliyet,minindis=minimalControl(kisiler[i])
        if(int(depolar[minindis-1][0])>=kisiler[i][0]):
            if(depolar[2]==0):
                totalmaliyet+=depolar[1]
                totalmaliyet+=minmaliyet
                depolar[2]=1
            else:
                totalmaliyet+=minmaliyet
        else:
            kisiler[i].pop(minindis)
            minmaliyet,minindis=minimalControl(kisiler[i])
        aw.append(minindis-1)
    print(totalmaliyet)
    print(aw)
def minimalControl(kisi):
    minmaliyet=kisi[1]
    minindis=1
    for j in range(2,len(kisi)):
        if minmaliyet>kisi[j]:
            minmaliyet=kisi[j]
            minindis=j;
    return minmaliyet,minindis
getFile("wl_200_2")
