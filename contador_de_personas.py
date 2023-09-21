import cv2
import imutils
import numpy as np
import torch
import os
from shutil import rmtree
import gdown

if(os.path.exists('DetectorDePersonas.pt')):
    print('DetectorDePersonas.pt listo')
else:
    url = "https://drive.google.com/file/d/1M7CJKTKMd0Z2RC4AZllXKnl8jlQ_lPYN/view?usp=drive_link"
    output = "DetectorDePersonas.pt"
    gdown.download(url, output, quiet=False, fuzzy=True)



#Lectura del modelo
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path = './DetectorDePersonas.pt')

cap = cv2.VideoCapture('./video_prueba/video_test.mp4')   #video de prueba del modelo


# Eliminar carpeta de resultados pasados
try:
    rmtree('./resultados')
except:
    print('Esta es la primer prueba')


# Crear directorio para almacenar los fotogramas
output_dir1 = './resultados/frames'
os.makedirs(output_dir1, exist_ok=True)

# Crear directorio para almacenar un video con los fotogramas
output_dir2 = './resultados/video'
os.makedirs(output_dir2, exist_ok=True)

frame_count = 0
contadorFrames = 0

#Variables y Contador de incremento o decremento de personas
person_counter = 0
contacar = 4
pm=0
conta_fot = 0
vector = [] # crear una lista vacía para almacenar los valores de pm
segundo_valor=0
matriz=[]
centroid_x = 0
centroid_y = 0

lim= 285
lim_i = 304

while True:

    #Realizar lectura de la captura

    ret, frame = cap.read()

    # Mostramos el numero de vehiculos
    cv2.putText(frame, "Ocupacion: ", (20, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.putText(frame, str(contacar), (200, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.putText(frame, "Personas", (260, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    if ret == False: break
    frame = imutils.resize(frame, width= 1000)

    #Mejora por rendimiento de CPU, Procesando 10 FPS
    conta_fot +=1
    if conta_fot % 3 !=0:
        continue

    #Detecciones. size debe tener el mismo tamaño de las imagenes en el entrenamiento
    detect = model(frame,size=224)

    # Extraccion de la informacion
    info = detect.pandas().xyxy[0].to_dict(orient='records')  # Predicciones

    # dibujar linea de referencia en el fotograma
    #cv2.line(frame, (530, lim), (980, lim), (0, 255, 0), 2) #Superior
    #cv2.line(frame, (530, lim_i), (980, lim_i), (0, 255, 0), 2) #Inferior

    # Preguntamos si hay Detecciones
    if len(info) != 0:
        # Creamos FOR
        for result in info:
            # Confianza
            conf = result['confidence']
            #print(conf)

            if conf >= 0.65:
                # Clase
                cls = int(result['class'])
                # Xi
                xi = int(result['xmin'])
                # Yi
                yi = int(result['ymin'])
                # Xf
                xf = int(result['xmax'])
                # Yf
                yf = int(result['ymax'])

                # Cálculo de las coordenadas del centroide
                centroid_x = int((xi + xf) / 2)
                centroid_y = int((yi + yf) / 2)

                # Dibujamos
                cv2.rectangle(frame, (xi, yi), (xf, yf), (0, 255, 0), 2)

                # Dibujar un círculo o marcador en el centroide
                cv2.circle(frame, (centroid_x, centroid_y), 5, (0, 0, 255),
                           -1) 

                # Guardar los valores en una lista
                vector = [centroid_y]
                # Agregar la lista de valores a la matriz
                matriz.append(vector)
                primero = matriz[-3:]

                if lim <= centroid_y <= lim_i:
                    # Verificar si la matriz está en orden ascendente
                    if primero == sorted(primero):
                        print("Entrando")
                        contacar = contacar + 1
                        break
                    # Verificar si la matriz está en orden descendente
                    elif primero == sorted(primero, reverse=True):
                        print("Saliendo")
                        contacar = contacar - 1
                        break
                    else:
                        print("La matriz no está en orden ascendente ni descendente")
                #print(cls)
                #vector.append(pm)  # agregar el valor actual de pm a la lista
                
    # Guardar el fotograma como una imagen separada
    output_path = os.path.join(output_dir1, f'frame_{frame_count}.jpg')
    cv2.imwrite(output_path, frame)
    frame_count += 1

    # Crea vídeo a partir de los fotogramas 
    if (contadorFrames<1):
        tamanoFrame = frame.shape
        salida = cv2.VideoWriter('./resultados/video/videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(tamanoFrame[1],tamanoFrame[0]))
        contadorFrames = contadorFrames + 1
    else:
        salida.write(frame)


    cv2.imshow('frame', frame)
    #salida.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
