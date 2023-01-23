import RPi.GPIO as GPIO # Biblioteca para manejo de pines
import time # Biblioteca para funciones de tiempo
from datetime import datetime # Biblioteca para manejo de fechas

#Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)

# Iniciar archivo log
sFileStamp = time.strftime('%Y%m%d%H')
sFileName = '\out' + sFileStamp + '.txt'
f=open(sFileName, 'a')
f.write('TimeStamp,Value' + '\n')
print ("Inicia la toma de datos")

# Intentar lo siguiente
try:
    # Repetir idefinidamente
    while True:
        print ("acerque el objeto para medir la distancia")

        # Bloque que activa el sensor
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER,False)

        # Medir la señal de respuesta del sensor
        start = time.time()
        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()
        while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()
        
        # Calcular el periodo del pulso de respuesta del sensor
        elapsed = stop-start

        # Ecuación para calcular la distancia
        distance = (elapsed * 34300)/2

        # Realizaar log en archivo de texto
        sTimeStamp = time.strftime('%Y%m%d%H%M%S')
        f.write(sTimeStamp + ',' + str(distance) + '\n')
        print (sTimeStamp + ' ' + str(distance))

        # Espera entre lecturas
        time.sleep(1)

        # Reportar y crear el archivo en caso de que no exista
        sTmpFileStamp = time.strftime('%Y%m%d%H')
        if sTmpFileStamp != sFileStamp:
            f.close
            sFileName = 'out/' + sTmpFileStamp + '.txt'
            f=open(sFileName, 'a')
            sFileStamp = sTmpFileStamp
            print ("creando el archivo")

# Acciones a realizar ante un error o una interrupción del programa
except KeyboardInterrupt:
    print ('\n' + 'termina la captura de datos.' + '\n')
    
    # Cerrar el archivo
    f.close

    #Liberar los recursos de manejo de hardware
    GPIO.cleanup()
