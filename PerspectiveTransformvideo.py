import cv2
import numpy as np

def clics(event,x,y,flags,param): #Eventos del mouse
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append([x,y])

def dibujando_puntos(puntos): #Marcan los puntos 
    for x, y in puntos:
        cv2.circle(Entrada,(x,y),5,(0,255,0),2)
#Coordenadas
def uniendo4puntos(puntos):
    cv2.line(Entrada,tuple(puntos[0]),tuple(puntos[1]),(255,0,0),1)#Superiorderecho
    cv2.line(Entrada,tuple(puntos[0]),tuple(puntos[2]),(255,0,0),1)#Superiorizquiero
    cv2.line(Entrada,tuple(puntos[2]),tuple(puntos[3]),(255,0,0),1)#Inferiorderecho
    cv2.line(Entrada,tuple(puntos[1]),tuple(puntos[3]),(255,0,0),1)#Inferiorizquierdo

puntos = [] #En este array se almacenan las coordinadas de los vértices

#cap = cv2.VideoCapture('ejemplo1.mp4')
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)

cv2.namedWindow('Entrada')
cv2.setMouseCallback('Entrada',clics)

while True:
    ret, Entrada = cap.read()
    if ret == False: break
    dibujando_puntos(puntos)

    if len(puntos) == 4:
        uniendo4puntos(puntos)
        pts1 = np.float32([puntos])
        pts2 = np.float32([[0,0], [500,0], [0,300], [500,300]])#Nuevovideo

        M = cv2.getPerspectiveTransform(pts1,pts2) #Funcion calcula la transformacion de perspectiva
        dst = cv2.warpPerspective(Entrada, M, (500,300))#Funcion aplica la transformacion perspectiva
        cv2.imshow('dst', dst)
    cv2.imshow('Entrada',Entrada)
    
    
    k = cv2.waitKey(30) & 0xFF 
    if k == ord('n'): # Limpiar el contenido de la Entrada
        puntos = []
        
    elif k == 27:
        break
cap.release()
cv2.destroyAllWindows()