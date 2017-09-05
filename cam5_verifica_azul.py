import cv2
import numpy as np  

#definindo a cam0 como sendo origem do video da variavel captura;
captura = cv2.VideoCapture(0) 

#Explicando ao python a cor preta;
preto = (0, 0, 0)

#loop de video;
while(1):
	ret, frame  = captura.read()

        #Quadrado vermelho de acordo com as cords acima;
        frame[198:202, 198:202] = (0, 0, 255)
	frame[298:302, 298:302] = (0, 0, 255)

	#Captura a cor das coordenada 10,10;
	(b, g, r) = frame[10, 10]
	
	cor = "%d" % (b)
	print cor

#	if cor < 150:
#		print "Livre"

	#Exibe a imagem da cam0;
	cv2.imshow('frame',frame)

	# ESC termina a brincadeira;
	k = cv2.waitKey(30) & 0xff
	if k == 27:
        	break
 
captura.release()
cv2.destroyAllWindows()
