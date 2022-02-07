'''
    20/1/22 laboratorio  operaciones numeros complejos
    Juan José Álvarez Beltrán
'''
##Suma
##Producto
##Resta
##División
##Módulo
##Conjugado
##Conversión entre representaciones polar y cartesiano
##Retornar la fase de un número complejo.
import math
def suma(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
def producto(c1,c2):
    return ((c1[0]*c2[0])-(c1[1]*c2[1]),(c1[0]*c2[1])+(c1[1]*c2[0]))
def resta(c1,c2):
    return (c1[0]-c2[0]),(c1[1]-c2[1])
def division(c1,c2):
    return (((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2))),(((c1[1]*c2[0])-(c1[0]*c2[1]))/((c2[0]**2)+(c2[1]**2)))
def modulo(c1):
    return (((c1[0]**2)+(c1[1]**2))**0.5)
def conjugado(c1):
    return (c1[0],-c1[1])
def conversor_cartesiano_a_polar(c1):
    imaginario = math.atan(c1[1]/c1[0])
    return (modulo(c1), imaginario)
def conversor_polar_a_cartesiano(c1):
    real=c1[0]*(math.cos(c1[1]))
    imaginario =c1[0]*(math.sin(c1[1]))
    return (real, imaginario)
def fase(c1):
    return (math.atan(c1[0]/c1[1]))
if __name__=='__main__':
        print(suma((2,15),(3,8)))
        print(producto((4,3),(2,11)))   
        print(resta((5,7),(9,2)))
        print(division((4,-1),(2,3)))
        print(modulo((1,1)))
        print(conjugado((2,1)))
        print(fase((-1,2)))
        print(conversor_cartesiano_a_polar((5,3)))
        print(conversor_polar_a_cartesiano((5.830951894845301,0.5404195002705842)))
