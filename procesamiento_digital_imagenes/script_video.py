import cv2
import numpy as np

cap = cv2.VideoCapture(0)

Redlower1 = np.array([0,80,80],np.uint8)
Redupper1 = np.array([8,255,255],np.uint8)

Redlower2 = np.array([175,80,80],np.uint8)
Redupper2 = np.array([179,255,255],np.uint8)

while cap.isOpened():
	ret, frame = cap.read()
	frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	mascara1 = cv2.inRange(frame_hsv,Redlower1,Redupper1)
	mascara2 = cv2.inRange(frame_hsv,Redlower2,Redupper2)
	mascara = cv2.add(mascara1,mascara2)
	#filtro_img = cv2.bitwise_and(frame,frame,mask = mascara)
	if ret == True:
		cv2.imshow("Video",frame)
		cv2.imshow("mascara",mascara)
		#cv2.imshow("filtro_img",filtro_img)
		#print(frame)
		if cv2.waitKey(1) == 97:
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()

##