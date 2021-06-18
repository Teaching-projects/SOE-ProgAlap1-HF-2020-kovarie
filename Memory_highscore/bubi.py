import os
import matplotlib.pyplot as plt


def highscore():
    f,a = plt.subplots()


    a.set_title("Legjobb eredmények")
    a.set_xlabel("Helyezések")

    x =[]
    y= []

    # Beolvassa a korábbi táblát
    file1 = open('highscore.txt', 'r')
    while(True):
        line = file1.readline()
        if line == '': break    # ha üres sor jött, vége a fájlnak, kilép
        tab_helye= line.find('\t')
        x.append(line[:tab_helye])
        y.append(int(line[tab_helye:]))
    file1.close()


    for j in range(len(y)):

        for i in range(0, len(y)-j-1):
            if y[i+1]<y[i]:
                x[i+1], x[i] = x[i], x[i+1]
                y[i+1], y[i] = y[i], y[i+1]



    print("X tengely: ",x)
    print("Y tengely: ",y)


    print(x)
    print(y)

    egyik= x 
    masik= y

    a.bar(egyik,masik)


    f.savefig('Highscore.jpg')

