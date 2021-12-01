import random
import numpy as np
from rbf import rbf 

class bacteria():
    def __init__(self,x,y,tiempo_ticks,contador_tick=0,temperatura=25,primera_vez=True,dup_tick=0,estado=True,):
        self.x=x
        self.y=y
        self.estado = estado
        self.contador_tick = int(contador_tick)
        self.temperatura = int(temperatura)
        self.primera_vez = primera_vez
        self.dup_tick = int(dup_tick)
        

        if self.primera_vez:
                
                self.dup_tick = self.calc_tDup(self.temperatura,tiempo_ticks)
                self.primera_vez =  False
        

    def principal(self,sustrato,alimento):
        if self.estado:
            x,y=self.movimiento_brawmiano()
            sus,ali=self.comer(sustrato,alimento)
            
            div=self.dividir_time(alimento)

        return x,y,sus,ali,div,self.estado,self.primera_vez,self.dup_tick,self.contador_tick
    

    def movimiento_brawmiano(self):
        sigma = 10; mu = 0
        dx = random.gauss(mu, sigma)
        dy = random.gauss(mu, sigma)
        self.y = int(self.y)+dy
        self.x = int(self.x)+dx
        #Bloqueo de bordes
        if self.x>630 :
            self.x = 630
        if self.x<20:
            self.x = 20
        if self.y<20 :
            self.y = 20
        if self.y>430:
            self.y = 430
        return self.x,self.y

    def calc_tDup(self,temperatura,tiempo_ticks):
        ##Obtener mu 
        temp = np.array(temperatura).reshape(1,-1)
        red = rbf(6)
        mu = red.evaluar(temp)[0,0]
        tiempo_dup = round((np.log(2)/mu)*60)
        centro = tiempo_dup
        sigma = centro*0.20
        tiempo_dup =round(random.gauss(centro,sigma))
        cant_tick = round(tiempo_dup/tiempo_ticks) #10 minutos por tick
        return cant_tick
        

    def dividir(self,alimento):
        if alimento <-5 :
            self.estado =False
            return False
        probabilidad = float(alimento)*50
        rand = random.gauss(0,100)
        #print("Rand:",rand,"Probabilidad:",probabilidad)
        if rand <int(probabilidad) and rand >=0:
            return True
        return False

    def dividir_time(self,alimento):
        if alimento <= -.1:
            
            if alimento <= -5:
                self.estado =False
            return False
        if self.dup_tick == self.contador_tick and self.estado:
            self.contador_tick = 0
            return True
        self.contador_tick += 1
        return False
    

    def comer(self,sustrato,alimento):
        sustrato = sustrato - 0.1
        if sustrato <= 0:
            sustrato = 0
            alimento -= 0.1
            return sustrato,alimento
            
        if alimento >=1:
            alimento = 0
        else:
            alimento = alimento + 0.1
        #print("Alimento:",alimento,"Sustrato:",sustrato)
        return sustrato,alimento