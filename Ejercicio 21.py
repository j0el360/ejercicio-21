import random

def Maso():
   return ['A♥','A♣','A♦','A♠','2♥','2♣','2♦','2♠','3♥','3♣','3♦','3♠',
          '4♥','4♣','4♦','4♠','5♥','5♣','5♦','5♠','6♥','6♣','6♦','6♠',
          '7♥','7♣','7♦','7♠','8♥','8♣','8♦','8♠','9♥','9♣','9♦','9♠',
          '10♥','10♣','10♦','10♠','J♥','J♣','J♦','J♠','Q♥','Q♣','Q♦','Q♠',
          'K♥','K♣','K♦','K♠']

def barajarMaso(a):
    random.shuffle(a)
    return a

def suma(seq):
    if (len(seq)== 0):
        return 0;
    else:
       return seq[0]+sum(seq[1:]);

def establecerSuma(a,b):
   b.clear();
   for x in a:
      if (x=="A♥" or x=="A♣" or x=="A♦" or x=="A♠"):
         if(suma(b[0:a.index(x)])>=10):
             print(suma(b[0:a.index(x)]));
             b.append(1);
         elif(suma(b[0:a.index(x)])<10):
             
             b.append(11);
             print(suma(b[0:a.index(x)]))
             
      else:
          b.append(Valores(x));
   return suma(b);         
              
def Valores(b):
    if any(s for s in b if "2" in b):
        return 2;
    elif any(s for s in b if "3" in b):
        return 3;
    elif any(s for s in b if "4" in b):
        return 4;
    elif any(s for s in b if "5" in b):
        return 5;
    elif any(s for s in b if "6" in b):
        return 6;
    elif any(s for s in b if "7" in b):
        return 7;
    elif any(s for s in b if "8" in b):
        return 8;
    elif any(s for s in b if "9" in b):
        return 9;
    elif any(s for s in b if "10" in b):
        return 10;
    elif any(s for s in b if "J" in b):
        return 10;
    elif any(s for s in b if "Q" in b):
        return 10;
    elif any(s for s in b if "K" in b):
        return 10;
    else:
        return 0;

def comprobarMano(b,c):
   if (establecerSuma(b,[])>21):
      print("Tines mas de 21 HAS PERDIDO a  :(    ");
      print("Tu mano: ")
      print(b);
      print ("Tienes" , establecerSuma(b,[]))
      print("mano de la casa: ")
      print(c)
      return "true";
   elif(establecerSuma(b,[])==21):
      print("Tienes 21   HAS GANADO   :D    ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";   
   elif(establecerSuma(b,[])<21):
      print("Tu mano: ")
      print(b);
      return "false";   
     
def comprobarManoCasa(c,b):
   if (establecerSuma(c,[])>21):
      print("La casa tine mas de 21   HAS GANADO   :D   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      print ("Tiene" , establecerSuma(c,[]))
      return "true";
   elif(establecerSuma(c,[])==21):
      print("La casa tiene 21     HAS PERDIDO  b :(   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";   
   elif(establecerSuma(c,[])<21):
      return "false";  


def compararFinal(c,b):
   if(establecerSuma(c,[])>establecerSuma(b,[])):
      print("La casa ha ganado    HAS PERDIDO  :(   ");
      print("Tu mano: ")
      print(b);
      print ("Tienes" , establecerSuma(b,[]))
      print("mano de la casa: ")
      print(c)
      print ("Tiene" , establecerSuma(c,[]))
   elif(establecerSuma(c,[])<establecerSuma(b,[])):
      print("La casa tiene menos que tu    HAS GANADO   :(   ");
      print("Tu mano: ")
      print(b);
      print ("Tienes" , establecerSuma(b,[]))
      print("mano de la casa: ")
      print(c)
      print ("Tiene" , establecerSuma(c,[]))
   elif(establecerSuma(c,[])==establecerSuma(b,[])):
      print(" HAN EMPATADO   :0   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      print ("Tienen" , establecerSuma(b,[]))

      

def jugar(a,b,c):
   if(len(b)==0 and len(c)==0):
      b.append(a[0]);
      c.append(a[1]);
      b.append(a[2]);
      c.append(a[3]);
      jugar(a[2:],b,c);
   else:
      print("Tu Mano : ");
      print(b);
      print ("llevas" , establecerSuma(b,[]))
      c.append(input("otra? "));
      print("_____________________________________________");
      if('s' in c):
         c.remove("s");
         b.append(a[0]);
         if(comprobarMano(b,c)=="false"):
             print("La casa se reparte otra carta");
             c.append(a[1]);
             if(comprobarManoCasa(c,b)=="false"):
                 jugar(a[2:],b,c);  
      elif('n' in c):
        c.remove("n");
        while(comprobarManoCasa(c,b)=="false"):
            if(establecerSuma(c,[])<21 and establecerSuma(c,[])>17):
               compararFinal(c,b);
               break;
            else:   
               c.append(a[0]);
               a.remove(a[0]);
               print("La casa se reparte otra carta");
     
                      

jugar(barajarMaso(Maso()),[],[]);
