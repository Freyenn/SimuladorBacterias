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
        

    def principal(self,sustrato,alimento,tiempo_ticks):
        self.Evaluar_vida(alimento)
        x =self.x;y=self.y;sus = sustrato; ali = alimento;div=False
        if self.estado:
            x,y=self.movimiento_brawmiano()
            sus,ali=self.comer(sustrato,alimento,tiempo_ticks)
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
        if cant_tick < 1 :
            cant_tick = 1
        return cant_tick
        
    def dividir_time(self,alimento):
        if alimento <= -.01:
            pass
        else:
            if self.dup_tick == self.contador_tick and self.estado:
                self.contador_tick = 0
                return True

        self.contador_tick += 1
        return False

    def Evaluar_vida(self,alimento):
        if alimento <= -.1:
            if alimento <= -5:
                rand = random.gauss(0,100)
                #print("Rand:",rand,"Probabilidad:",probabilidad)
                if rand <=int(20) and rand >=0:
                    self.estado =False
                
    

    def comer(self,sustrato,alimento,tiempo_ticks):
        sustrato = sustrato - 0.01*tiempo_ticks
        if sustrato <= 0:
            sustrato = 0
            alimento -= 0.01*tiempo_ticks
            return sustrato,alimento
            
        if alimento >=1:
            alimento = 0
        else:
            alimento = alimento + 0.01*tiempo_ticks
        #print("Alimento:",alimento,"Sustrato:",sustrato)
        return sustrato,alimento