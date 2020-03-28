

import datetime
from time import ctime
import ntplib
import os


x0=datetime.datetime.now()
print("\nHORA DE INICIO DE LA PETICION\n%s" % x0+"\n")

servidor_de_tiempo="time-c-g.nist.gov"

cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
x1 = datetime.datetime.now()

print("HORA DE LLEGADA DE LA PETICION\n%s" % x1+"\n")

print("RESPUESTA DEL SERVIDOR\n"+servidor_de_tiempo+": "+str(hora_actual)+"\n")
print("AJUSTE:\n"+str((x1-x0)/2)+"\n")

cambio_hora=hora_actual+((x1-x0)/2)

print("\nHORA/FECHA QUE SE VA A CAMBIAR EN LA COMPUTADORA LOCAL:\n"+str(cambio_hora)+"\n")

call= 'date -u "'+str(cambio_hora.strftime("%m%d%H%M%Y.%S"))+'"'
os.system(call)
