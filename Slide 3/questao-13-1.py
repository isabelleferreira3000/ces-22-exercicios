f = open("arquivo.txt", "r")
xs = f.readlines()
f.close()

ss = []
for i in range(len(xs)):
    ss.append(xs[len(xs)-i-1])

g = open("inverso.txt", "w")
for v in ss:
    g.write(v)
g.close()
