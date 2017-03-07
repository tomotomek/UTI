import itertools, time
start = time.time()

allPrograms = set()
allCharPrograms = set()
goodPrograms = [] #do tohoto pola budem ukladat syntakticky spravne programy
znaky = []
pp = []

for i in range(1,128):
    znaky.append(i)

#generuje programy zvolenej dlzky (3)
for i in range(1,3):
    pp.append(itertools.combinations_with_replacement(znaky, i))

#prejde vsetkymi vygenerovanymi programami
for dlzky in pp:
    for x in dlzky:
        #urobi permutacie a vlozi ich do mnoziny
        #aby sme sa zbavili pripadov typu ([0,0],[0,0])
        permutacie = itertools.permutations(x)
        for z in permutacie:
            pom = []
            for c in z:
                pom.append(chr(c))
                #z n-tic vytvori stringy, aby sme ich mohli neskor testovat
            allCharPrograms.add(''.join(pom))
            allPrograms.add(''.join(map(str, z)))
            
for program in allPrograms:
    try:
        #postupne testuje vsetky programy, syntakticky spravne vlozi do pola
        compile(program,"<string>", "exec")
        goodPrograms.append(program)
    except:
        pass

#utriedenie pola podla dlzky, potom lexikograficky
#subor programu dlzky 1 znak ma velkost 1 byte
goodPrograms.sort(key=lambda x: (len(x), x))

print(len(goodPrograms))
print(goodPrograms[1328])
print(goodPrograms[272], goodPrograms[8162])
print(time.time() - start)
