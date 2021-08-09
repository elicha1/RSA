# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:55:35 2018

@author: aicha

"""
def euclide_etendu(a,b):
    x = 0 ; xx = 1
    y = 1 ; yy = 0
    while b !=0 :
        q = a // b
        a , b = b , a % b
        x , xx = xx - q*x , x
        y , yy = yy - q*y , y
    return (a,xx,yy)

def generation_deN(p,q):
    print ("l'envirenment est :n=", p*q)
    return p*q

def generationde_phi(p,q):
    print("Le phi est  : ", (p-1)*(q-1))
    return(p-1)*(q-1)
    
def init_rsa(p,q,e) :
    n= generation_deN(p,q)
    phi= generationde_phi(p,q)   
    c,d,dd = euclide_etendu(e,phi)         # Pgcd et coeff de BÃ©zout
#    print("Coeff. BÃ©zout : d,dd = ", d,dd)
    d = d % phi                            # Bon reprÃ©sentant
    if c != 1 :
        print("Mauvais exposant ! Essayez encore.")
        return None
    else :
        print("Clef publique : n = ", n ,", e = ", e)
        print("Clef privée   : d = ", d)
        print("Outils intermidiaires (à  oublier) : p = ", p,", q = ", q,", phi = ", phi)
        return (d)
def ver_premier(x):
    if (x > 1):
        divisor = 2
        for i in range(divisor,x):
            if (x % i) == 0:
                return False
    else:
        return False
    return True
def chiffrement(m,n,e):
    return pow(m,e,n)
def dechiffrement(x,d,n):
    return pow(x,d,n)
    


if __name__ == '__main__':
       p= int(input("choisissez un nombre premier :"))
       q = int(input("choisissez un nombre premier :"))
       if ver_premier(p) & ver_premier(q):
               n = generation_deN(p,q)
               phi =generationde_phi(p,q)
               e = int(input("choisissez un exposant premier avec phi :"))
               d=init_rsa(p,q,e)
               print("Le clé privée est : d = ",d,"n = ",n)
               m = int(input("Enter à crypter: "))
               x = chiffrement(m,n,e)
               print("Le message crypté : ",x)
               print("Décryptage ...")
               print("Votre messsage était :")
               print(dechiffrement(x,d,n))
       else :
           print ("le p ou q ou les deux et nn premier ")
         
               
               
 
     