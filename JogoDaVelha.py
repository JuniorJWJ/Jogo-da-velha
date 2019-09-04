import random
matriz=[]
lista=[]
a=" "
b=" "
c=" "
d=" "
e=" "
f=" "
g=" "
h=" "
i=" "
empate=2
soma=0
def exem():
    print("1 |2 |3 ")
    print("--|--|--")
    print("4 |5 |6 ")
    print("--|--|--")
    print("7 |8 |9")
    print("""

    """)
escolhas=["1",'2','3','4','5','6','7','8','9']
print("***BEM VINDO AO JOGO DA VELHA***")
def jogodavelha(a,b,c,d,e,f,g,h,i):
  print(" {} | {} | {} ".format(a,b,c))
  print("---|---|----")
  print(" {} | {} | {} ".format(d,e,f))
  print("---|---|----")
  print(" {} | {} | {} ".format(g,h,i))
  print("""

      """)
print("SEGUE O EXEMPLO:")
print("1 |2 |3 ")
print("--|--|--")
print("4 |5 |6 ")
print("--|--|--")
print("7 |8 |9 ")
print("""

""")
soma=2


while(soma<11):
    if(soma%2==0):
      num=(input("Qual posição você quer jogar:"))
      if(num=='1'):
        escolhas.remove('1')
        if(soma%2==0):
          a="X"
        else:
          a="O"
      elif(num=="4"):
        escolhas.remove("4")
        if(soma%2==0):
          d="X"
        else:
          d="O"
      elif(num=="7"):
        escolhas.remove("7")
        if(soma%2==0):
          g="X"
        else:
          g="O"
      elif(num=="2"):
        escolhas.remove("2")
        if(soma%2==0):
          b="X"
        else:
          b="O"
      elif(num=="5"):
        escolhas.remove("5")
        if(soma%2==0):
          e="X"
        else:
          e="O"
      elif(num=="8"):
        escolhas.remove("8")
        if(soma%2==0):
          h="X"
        else:
          h="O"
      elif(num=="3"):
        escolhas.remove("3")
        if(soma%2==0):
          c="X"
        else:
          c="O"
      elif(num=="6"):
        escolhas.remove("6")
        if(soma%2==0):
          f="X"
        else:
          f="O"
      elif(num=="9"):
        escolhas.remove("9")
        if(soma%2==0):
          i="X"
        else:
          i="O"

    if(soma%2!=0):
        if("5") in escolhas:
            num='5'
            escolhas.remove("5")
            e="O"
        elif (a == "O" and a == b and ("3") in escolhas):  # linha1 xx_
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c="O"
        elif (a == "O" and a == c and ("2") in escolhas):  # linha 1 x_x
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b="O"
        elif (c == "O" and c == a and ("2") in escolhas):  # linha 1 x_x
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b="O"
        elif (c == "O" and c == b and ("1") in escolhas):  # linha 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                c="O"
        #diagonal
        elif (a == "O" and a == i and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (i == "O" and i == a and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (a == "O" and a == e and ("9") in escolhas):  # linha 1 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                b="O"
        elif (i == "O" and i == e and ("1") in escolhas):  # linha 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                a="O"
        elif (c == "O" and c == g and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (g == "O" and g == c and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (c == "O" and c == e and ("7") in escolhas):  # linha 1 xx_
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g="O"
        elif (g == "O" and g == e and ("3") in escolhas):  # linha 1 _xx
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c="O"
        elif (d == "O" and d == e and ("6") in escolhas):  # linha2 xx_
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"
        elif (d == "O" and d == f and ("5") in escolhas):  # linha2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (f == "O" and f == d and ("5") in escolhas):  # linha 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (f == "O" and f == e and ("4") in escolhas):  # linha 2 _xx
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"
        elif (g == "O" and g == h and ("9") in escolhas):  # linha 3 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                i = "O"
        elif (g == "O" and g == i and ("8") in escolhas):  # linha 3 x_x
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (i == "O" and i == g and ("8") in escolhas):  # linha 3 x_x
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (i == "O" and i == h and ("7") in escolhas):  # linha 3 _xx
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g = "O"
        elif (a == "O" and a == d and ("7") in escolhas):  # coluna1 xx_
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g = "O"
        elif (a == "O" and a == g and ("4") in escolhas):  # colunaa 1 x_x
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"
        elif (g == "O" and g == i and ("4") in escolhas):  # colunaa 1 x_x
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"
        elif (g == "O" and g == d and ("1") in escolhas):  # coluna 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                a = "O"
        elif (b == "O" and b == e and ("8") in escolhas):  # coluna2 xx_
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (b == "O" and b == h and ("5") in escolhas):  # colunaa 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (h == "O" and h == b and ("5") in escolhas):  # colunaa 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (h == "O" and h == e and ("2") in escolhas):  # coluna 2 _xx
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b = "O"
        elif (c == "O" and c == f and ("9") in escolhas):  # coluna3 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                i = "O"
        elif (c == "O" and c == i and ("6") in escolhas):  # colunaa 3 x_x
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"
        elif (i == "O" and i == c and ("6") in escolhas):  # colunaa 3 x_x
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"
        elif (i == "O" and i == f and ("3") in escolhas):  # coluna 3 _xx
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c = "O"
        #defender
        elif (a == "X" and a == b and ("3") in escolhas):  # linha1 xx_
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c="O"

        elif (a == "X" and a == c and ("2") in escolhas):  # linha 1 x_x
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b="O"

        elif (c == "X" and c == a and ("2") in escolhas):  # linha 1 x_x
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b="O"

        elif (c == "X" and c == b and ("1") in escolhas):  # linha 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                a="O"
        elif (d == "X" and d == e and ("6") in escolhas):  # linha2 xx_
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"

        elif (d == "X" and d == f and ("5") in escolhas):  # linha2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"

        elif (f == "X" and f == d and ("5") in escolhas):  # linha 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"

        elif (f == "X" and f == e and ("4") in escolhas):  # linha 2 _xx
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"

        elif (g == "X" and g == h and ("9") in escolhas):  # linha 3 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                i = "O"
        elif (g == "X" and g == i and ("8") in escolhas):  # linha 3 x_x
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (i == "X" and i == g and ("8") in escolhas):  # linha 3 x_x
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (i == "X" and i == h and ("7") in escolhas):  # linha 3 _xx
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g = "O"
        elif (a == "X" and a == d and ("7") in escolhas):  # coluna1 xx_
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g = "O"
        elif (a == "X" and a == g and ("4") in escolhas):  # colunaa 1 x_x
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"
        elif (g == "X" and g == i and ("4") in escolhas):  # colunaa 1 x_x
            if (("4") in escolhas):
                num = '4'
                escolhas.remove("4")
                d = "O"
        elif (g == "X" and g == d and ("1") in escolhas):  # coluna 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                a = "O"
        elif (b == "X" and b == e and ("8") in escolhas):  # coluna2 xx_
            if (("8") in escolhas):
                num = '8'
                escolhas.remove("8")
                h = "O"
        elif (b == "X" and b == h and ("5") in escolhas):  # colunaa 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (h == "X" and h == b and ("5") in escolhas):  # colunaa 2 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e = "O"
        elif (h == "X" and h == e and ("2") in escolhas):  # coluna 2 _xx
            if (("2") in escolhas):
                num = '2'
                escolhas.remove("2")
                b = "O"


        elif (c == "X" and c == f and ("9") in escolhas):  # coluna3 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                i = "O"
        elif (c == "X" and c == i and ("6") in escolhas):  # colunaa 3 x_x
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"
        elif (i == "X" and i == c and ("6") in escolhas):  # colunaa 3 x_x
            if (("6") in escolhas):
                num = '6'
                escolhas.remove("6")
                f = "O"
        elif (i == "X" and i == f and ("3") in escolhas):  # coluna 3 _xx
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c = "O"
        #diagonal
        elif (a == "X" and a == i and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (i == "X" and i == a and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (a == "X" and a == e and ("9") in escolhas):  # linha 1 xx_
            if (("9") in escolhas):
                num = '9'
                escolhas.remove("9")
                i="O"
        elif (i == "X" and i == e and ("1") in escolhas):  # linha 1 _xx
            if (("1") in escolhas):
                num = '1'
                escolhas.remove("1")
                a="O"
        elif (c == "X" and c == g and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (g == "X" and g == c and ("5") in escolhas):  # linha 1 x_x
            if (("5") in escolhas):
                num = '5'
                escolhas.remove("5")
                e="O"
        elif (c == "X" and c == e and ("7") in escolhas):  # linha 1 xx_
            if (("7") in escolhas):
                num = '7'
                escolhas.remove("7")
                g="O"
        elif (g == "X" and g == e and ("3") in escolhas):  # linha 1 _xx
            if (("3") in escolhas):
                num = '3'
                escolhas.remove("3")
                c="O"

        else:
            num=random.choice(escolhas)
            if(num=="1"):
                escolhas.remove("1")
                if(soma%2==0):
                    a="X"
                else:
                    a="O"
            if(num=="4"):
                escolhas.remove("4")
                if(soma%2==0):
                    d="X"
                else:
                    d="O"
            elif(num=="7"):
                escolhas.remove("7")
                if(soma%2==0):
                    g="X"
                else:
                    g="O"
            elif(num=="2"):
                escolhas.remove("2")
                if(soma%2==0):
                    b="X"
                else:
                    b="O"
            elif(num=="5"):
                escolhas.remove("5")
                if(soma%2==0):
                    e="X"
                else:
                    e="O"
            elif(num=="8"):
                escolhas.remove("8")
                if(soma%2==0):
                    h="X"
                else:
                    h="O"
            elif(num=="3"):
                escolhas.remove("3")
                if(soma%2==0):
                    c="X"
                else:
                    c="O"
            elif(num=="6"):
                escolhas.remove("6")
                if(soma%2==0):
                    f="X"
                else:
                    f="O"
            elif(num=="9"):
                escolhas.remove("9")
                if(soma%2==0):
                    i="X"
                else:
                    i="O"
    soma = soma + 1
    exem()
    jogodavelha(a,b,c,d,e,f,g,h,i)
    if(a=="X" and a==b and b==c):#linha1
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(a=="X" and a==e and e==i):#diagonal1
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(d=="X" and d==e and e==f):#linha2
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(g=="X" and g==h and h==i):#linha3
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(c=="X" and c==e and e==g):#diagonal2
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(a=="X" and a==d and d==g):#coluna1
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(b=="X" and b==e and e==h):#coluna2
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    if(c=="X" and c==f and f==i):#coluna3
        print("Jogador 1 venceu!!!")
        empate = 1
        break
    #SEGUNDO JOGADOR
    if(a=="O" and a==b and b==c):#linha1
        print("O computador venceu!!!")
        empate = 1
        break
    if(a=="O" and a==e and e==i):#diagonal1
        print("O computador venceu!!!")
        empate = 1
        break
    if(d=="O" and d==e and e==f):#linha2
        print("O computador venceu!!!")
        empate = 1
        break
    if(g=="O" and g==h and h==i):#linha3
        print("O computador venceu!!!")
        empate = 1
        break
    if(c=="O" and c==e and e==g):#diagonal2
        print("O computador venceu!!!")
        empate = 1
        break
    if(a=="O" and a==d and d==g):#coluna1
        print("O computador venceu!!!")
        empate = 1
        break
    if(b=="O" and b==e and e==h):#coluna2
        print("O computador venceu!!!")
        empate = 1
        break
    if(c=="O" and c==f and f==i):#coluna3
        print("O computador venceu!!!")
        empate = 1
        break
if(empate==2):
    print("Deu Empate")

