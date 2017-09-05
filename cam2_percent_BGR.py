import cv2
 
captura = cv2.VideoCapture(0)
 
while(1):
	ret, imagem = captura.read()
	cv2.imshow("Original", imagem)

	(b, g, r) = imagem[0, 0]
	print "Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b) 
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
	        break
 
captura.release()
cv2.destroyAllWindows()
