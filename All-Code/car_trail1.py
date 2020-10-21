import cv2

def video_classifier(video_file, car_classifer_file, pedistrian_classifer_file):

    car_tracker = cv2.CascadeClassifier(car_classifer_file)

    #pedistrian_tracker = cv2.CascadeClassifier(pedistrian_classifer_file)

    video = cv2.VideoCapture(video_file)

    while True:

        (read_sucessful, frame) = video.read()

        if read_sucessful:

            grey_scale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        else:
            
            break
        
        cars = car_tracker.detectMultiScale(grey_scale_frame)

        #pedistrains = pedistrian_tracker.detectMultiScale(grey_scale_frame)


        for (x, y, w, h) in cars:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
        #for (x, y, w, h) in pedistrains:

         #   cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        cv2.imshow('Automated_software', frame)

        key = cv2.waitKey(1)

        if key == 32:
            
            break

def image_classifer(img_file, image_classifer_file):

    img = cv2.imread(img_file)

    black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    car_tracker = cv2.CascadeClassifier(image_classifer_file)

    cars =  car_tracker.detectMultiScale(black_n_white)

    for (x, y, w, h) in cars:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('car_detected' ,img)

    cv2.waitKey()

image_classifer('ca5_6.jpg', 'cars.xml')

#video_classifier('video_1.mp4', 'cars.xml', 'haarcascade_fullbody.xml')

print('code completed')
