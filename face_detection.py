import cv2

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#path to cascade file
rec = cv2.VideoCapture(0)# to capture video from the webcam use 1 for external webcam
'''rec = cv2.VideoCapture(//path of the video.mp4//)'''# to detect faces in a video file
while True:
	ret, frame = rec.read() #takes two arguments and start reading frames
	faces = classifier.detectMultiScale(frame)# variables for finding frames
	for (x,y,w,h) in faces: #loop for each frame and putting them in rectangles
		cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)# name of the second argument at line 5, area of rectangle, color of rectangle in BGR, width of rectangle
	cv2.imshow("Faces here",frame)# function to show what's going on
	key = cv2.waitKey(1) & 0xFF# waiting for key press

	if key == ord("q") or key ==27:# if key is q then break the loop
		break
cv2.destroyAllWindows()#closes all running windows
