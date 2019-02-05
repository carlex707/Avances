import math
def ecuacion():
   a=int(input('Introduce el valor de a:'))
   b=int(input('Introduce el valor de b:'))
   c=int(input('Introduce el valor de c:'))

   d=(b*b)-4*a*c
   if d<0 :
       print('No existen soluciones reales')
   else:
       x1=(-b+math.sqrt(d))/(2*a) 
       x2=(-b-math.sqrt(d))/(2*a)    
       print('Solucion x1=',"{:.2f}".format(x1))
       print('Solucion x2=',"{:.2f}".format(x2))
ecuacion()