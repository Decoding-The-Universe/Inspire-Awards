import cv2

def smile_detecion(face_classifer_file, smile_classifer_file):

	smile_detector = cv2.CascadeClassifier(smile_classifer_file)

	face_detector = cv2.CascadeClassifier(face_classifer_file)

	while True:

		webcam = cv2.VideoCapture(0)

		read_success, frame = webcam.read()

		if read_success:

			grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			
			faces = face_detector.detectMultiScale(grey_frame)

			        

						

			for (x, y, w, h) in faces:

				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) 

				face_frame = frame[y:y+h, x:x+w]

				face_grey_image = cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)

				smiles = smile_detector.detectMultiScale(face_grey_image, 1.7, 20)
           
				if len(smiles)>0:
					cv2.putText(frame, 'smiling', (x, y+h+50), fontScale = 3,thickness = 2 ,color = (255, 0, 0), fontFace = cv2.FONT_HERSHEY_PLAIN)
			
				#for (x_, y, w, h) in smiles:

				#	cv2.rectangle(face_frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 						
				#	cv2.putText(face_frame, 'smiling', (x, y), fontScale = 3,thickness = 2 ,color = (255, 0, 0), fontFace = cv2.FONT_HERSHEY_PLAIN)

			cv2.imshow('Face_Detection', frame)



		else:

			
			break
			webcam.release()
			
    
		key = cv2.waitKey(1)

		if key == 32:

			break
			webcam.release()
			
smile_detecion('haarcascade_frontalface_default.xml', 'haarcascade_smile.xml')        







