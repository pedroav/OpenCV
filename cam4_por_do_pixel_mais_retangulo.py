import cv2
import numpy as np  

#definindo a cam0 como sendo origem do video da variavel captura;
captura = cv2.VideoCapture(0) 

#Explicando ao python a cor preta;
preto = (0, 0, 0)

#loop de video;
while(1):
	ret, frame = captura.read()

	#Captura a cor das coordenada 10,10;
	(b, g, r) = frame[10, 10]
	
	#Quadrado vermelho de acordo com as cords acima;
	frame[198:202, 198:202] = (0, 0, 255)
	
	#Preview;
	frame[10:90, 10:90] = (b, g, r)	

	#Exibe o retangulo preto nas cords 10,10 de tamanho 90,190;
	cv2.rectangle(frame, (10, 10), (198, 198), preto)

	#Exibe a imagem da cam0;
	cv2.imshow('frame',frame)

	# ESC termina a brincadeira;
	k = cv2.waitKey(30) & 0xff
	if k == 27:
        	break
 
captura.release()
cv2.destroyAllWindows()
