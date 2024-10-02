import cv2

# Carregar os classificadores pré-treinados
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Carregar o vídeo
video_path = "./la_cabra.mp4"

# Ler o vídeo
cap = cv2.VideoCapture(video_path)
success, frame = cap.read()

height, width, layers = frame.shape
annotated_video = cv2.VideoWriter("annotated_video.avi", 0, 30, (width, height))

while cap.isOpened() and success:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Percorrer as faces detectadas
    for x, y, w, h in faces:
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

	# Detectar olhos
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))

        if len(eyes) < 1:
            continue

	# Desenhar retângulos em torno das faces detectadas
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

	#Percorrer os olhos detectados
        for ex, ey, ew, eh in eyes:
	    # Desenhar retângulo em torno dos olhos detectados
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    annotated_video.write(frame)

    cv2.imshow("Video", frame)
    cv2.waitKey(1)
    success, frame = cap.read()

cap.release()
annotated_video.release()
cv2.destroyAllWindows()
