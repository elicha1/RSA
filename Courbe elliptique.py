# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:19:59 2018

@author: aicha
"""

from math import sqrt


          
def Verifier_courbe(a,b):
          v= 4*pow(a,3)+27 * pow(b,2)
          if v == 0 :
                 print ("la courbe  est  mal definie ")
                 a=int(input("la valeur de a"))
                 b=int(input("la valeur de b"))
                 Verifier_courbe(a,b)
          else: 
              print ("la courbe  est  bien definie ")
def addpointdis(x,y,c,d) :
             s= (y-d)/(x-c)
             xres= pow(s,2)-(x+c)
             yres= s *(x-c)-y
             print (" Le point résultant R a comme coordonnées  : ", xres,yres) 
             return s,xres,yres

def addition_2_fois(x,y,a) :
                 s=(3*pow(x,2)+a)/(2*y)
                 xres=pow(s ,2)-2*x
                 yres= s*(x-xres)-y
                 print (" Le point résultant R a comme coordonnées  : ", xres,yres) 
                 return s,xres,yres

def verifie_Verc(x,y,c,d) :
    
           if x==c & d==y:
               print (" le double est ") 
               addition_2_fois(x,y,a)
           elif x==c & d!=y:
               print (" l'infinie est le resultat") 
           elif x!=c & y!=d:
               print (" l'addition de deux point #") 
               addpointdis(x,y,c,d)
def multiplierparpaire(xp,yp,nbr,a):
        while nbr/2!=1:
           S,X,Y= addition_2_fois(xp,yp,a)
           nbr=nbr/2
           xp=X
           yp=Y
        addition_2_fois(xp,yp,a)
    
def multiplier(xp,yp,nbr,a):
        par,exe,ey=multiplierparpaire(xp,yp,nbr-1,a)
        addpointdis(xp,yp,exe,ey)
        
                          
          

if __name__ == '__main__':


       print(" veuillez etablir l'equation de weirstrass ( y²=x^3+ a*x+b) est suivre le traitement :")
       a=int(input("la valeur de a"))
       b=int(input("la valeur de b"))
       
       Verifier_courbe(a,b)
       
       choix=input("veuillez taper la nature de traitment que vou voulez faire :A/M")
       if choix=='A':
            print(" traitemnt d'addition :")
            xp=int(input("la valeur de x de premier point"))
            yp=int(sqrt(pow(xp,3)+a*xp+b))
            print("la valeur de yp est  :",yp)
       
            xq=int(input("la valeur de x de deuxieme point"))
            yq=int(sqrt(pow(xq,3)+a*xq+b))
            print("la valeur de yq est  :",yq)
            verifie_Verc(xp,yp,xq,yq)
       elif choix =='M':
            print(" traitmnt de multiplication par un scalaire  :")
            nbr=int(input("tapez le nombre scalaire "))
            xp=int(input("la valeur de x du point"))
            yp=int(sqrt(pow(xp,3)+a*xp+b))
            print("la valeur de yp est  :",yp)
            if nbr%2==0:
                  multiplierparpaire(xp,yp,nbr,a)
            else :
                  multiplier(xp,yp,nbr,a)
                  
       
      
            