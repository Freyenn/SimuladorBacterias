# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:35:40 2021

@author: luis-
"""
from kmeans import KMEANS
import numpy as np

class rbf():
    def __init__(self,k=6):
        cnew= np.array([25.5802,29.8233,9.88916,36.5778,44.7004,21.1119])
        cnew= cnew[:,np.newaxis]
        Wnew= np.array([1.36249,-1.38424,0.167512,2.86138,0.0642429,0.0704927])
        Wnew= Wnew[:,np.newaxis]
        self.c = cnew
        self.sigma = np.array([6.86441,8.0893,10.8691,10.0391,12.3839,7.68934])
        self.W = Wnew
        self.k=k
        
    def entrenamiento(self,x,y):
        #Etapa no supervisada
        self.x=x
        #inicializar el clasificador
        clasificador = KMEANS(self.k)
        #agrupar datos
        c,grupos = clasificador.AGRUPAR(x)
        self.c=c.T
        #Calcular sigma
        distancias_c = np.zeros((self.c.shape[0],self.x.shape[1]))
        for i in range(self.c.shape[0]):
            for j in range(self.x.shape[1]):
                distancias_c[i,j]=EUCLIDIANA(self.c[i,:],self.x[:,j])
                
        sigma = np.zeros((distancias_c.shape[0]))
        for i in range(distancias_c.shape[0]):        
            sigma[i]=(np.amax(distancias_c[i,:])-np.amin(distancias_c[i,:]))/np.sqrt(2*self.k)
                
        #sigma = (max(distancias_c)-min(distancias_c))/np.sqrt(2*self.k)
        print("Sigma",sigma)
        #self.sigma = sigma[0]
        self.sigma = sigma
# =============================================================================
#         #matriz G
#         G=np.zeros((x.shape[1],self.k))
#         for i in range(x.shape[1]):
#             for j in range(self.k):
#                 dist = np.linalg.norm(x[:,i]-self.c[j],2)
#                 G[i,j] = np.exp((-1/self.sigma**2) * dist**2)
#                 
#         self.W = np.dot(np.linalg.pinv(G),y.T)
#         print("Tamaño W",self.W.shape)
# =============================================================================
# =============================================================================
# Matriz G Multiple
        G=np.zeros((x.shape[1],self.k))
        for i in range(x.shape[1]):
            for j in range(self.k):
                dist = np.linalg.norm(x[:,i]-self.c[j,:],2)
                G[i,j] = np.exp((-1/(self.sigma[j]**2)) * dist**2)
                
        print("Matriz G:",G)        
        self.W = np.dot(np.linalg.pinv(G),y.T)
        print("Tamaño W",self.W.shape)


# =============================================================================
    def evaluar(self,entrada):
            G=np.zeros((entrada.shape[1],self.k))
            for i in range(entrada.shape[1]):
                for j in range(self.k):
                    dist = np.linalg.norm(entrada[:,i]-self.c[j,:],2)
                    G[i,j] = np.exp((-1/(self.sigma[j]**2)) * dist**2)
                    
            ynew = np.dot(G,self.W)
            

            # for i in range(len(ynew)):
            #       if ynew[i] >0 :
            #           ynew[i]=1
            #       else:
            #           ynew[i]=-1

            return ynew       
# =============================================================================
#     def evaluar(self,entrada):
#         G=np.zeros((entrada.shape[1],self.k))
#         for i in range(entrada.shape[1]):
#             for j in range(self.k):
#                 dist = np.linalg.norm(entrada[0,i]-self.c[j],2)
#                 G[i,j] = np.exp((-1/self.sigma**2) * dist**2)
#                 
#         ynew = np.dot(G,self.W)
#         return ynew
# =============================================================================

def EUCLIDIANA(x,y):
    return np.sqrt(np.sum((x-y)**2)) 