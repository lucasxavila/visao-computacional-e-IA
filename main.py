from ultralytics import YOLO
import cv2

# Carregar modelo treinado
model = YOLO('best.pt')  # Modelo treinado com EPIs

# Captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = box.conf[0]
            if conf > 0.5:
                label = model.names[cls]
                # Exibir resultado
                cv2.rectangle(frame, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0,255,0), 2)
                cv2.putText(frame, label, (int(box.xyxy[0][0]), int(box.xyxy[0][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    cv2.imshow('EPI Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()