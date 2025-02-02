import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from ultralytics import YOLO

#Using v8 Model for much faster, lightweight and accurate real-time detection

model = YOLO("yolov8n.pt")  # Using the small model for speed

def detect_objects(frame):
    results = model(frame)
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get class index
            if class_id == 9:  # 'Traffic Light' class in COCO dataset
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                roi = frame[y1:y2, x1:x2]  # Extract traffic light region
                
                predicted_label = classify_traffic_light(roi)
                print(f"Traffic Light Detected: {predicted_label}")
                
                if predicted_label == 'Red':
                    print("Instruction: Stop")
                elif predicted_label == 'Green':
                    print("Instruction: Go")
                elif predicted_label == 'Yellow':
                    print("Instruction: Slow down")

    return results

def normalize_image(image):
    # Convert image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # Spliting LAB channels
    l, a, b = cv2.split(lab_image)
    
    # Applying histogram equalization to L channel
    l_eq = cv2.equalizeHist(l)
    
    # Merge equalized L channel with original A and B channels
    normalized_lab_image = cv2.merge((l_eq, a, b))
    
    # Converting back to BGR color space
    normalized_image = cv2.cvtColor(normalized_lab_image, cv2.COLOR_LAB2BGR)
    
    return normalized_image


def imgdetection():
    
    video= cv2.VideoCapture(0)

    
    

    while True:
        x, frame= video.read()
        normalized_frame = normalize_image(frame)
        bound, label, config= cv.detect_common_objects(normalized_frame)
        output_image=draw_bbox(normalized_frame, bound, label, config)
        
        
        tred = 0
        tgreen = 0
        tyellow = 0
        
        for i, l in enumerate(label):
            if l == 'traffic light':
                # Extract bounding box coordinates
                x, y, w, h = bound[i]

                # Crop the bounding box region from the frame
                traffic_light_roi = normalized_frame[y:y+h, x:x+w]

                if traffic_light_roi.size == 0:
                    continue
                
                # bright_red_lower = (0, 100, 100)
                # bright_red_upper = (80, 255, 255)
                # bright_green_lower = (40, 40, 40)
                # bright_green_upper = (80, 255, 255)
                # bright_yellow_lower = (20, 100, 100)
                # bright_yellow_upper = (30, 255, 255)

                
                # mask_red = cv2.inRange(traffic_light_roi, bright_red_lower, bright_red_upper)
                # mask_green = cv2.inRange(traffic_light_roi, bright_green_lower, bright_green_upper)
                # mask_yellow = cv2.inRange(traffic_light_roi, bright_yellow_lower, bright_yellow_upper)

                # # Count pixels for each bright color
                # red_pixels = cv2.countNonZero(mask_red)
                # green_pixels = cv2.countNonZero(mask_green)
                # yellow_pixels = cv2.countNonZero(mask_yellow)
                
                # total_red_pixels += red_pixels
                # total_green_pixels += green_pixels
                # total_yellow_pixels += yellow_pixels
                # Count red and green pixels within the bounding box
                #if cv2.inRange(traffic_light_roi, (0, 0, 100), (80, 80, 255)).sum() or cv2.inRange(traffic_light_roi, (0, 100, 0), (80, 255, 80)).sum() or cv2.inRange(traffic_light_roi, (0, 100, 100), (80, 255, 255)).sum():
                rpx = cv2.inRange(traffic_light_roi, (0, 0, 100), (80, 80, 255)).sum()
                gpx = cv2.inRange(traffic_light_roi, (0, 100, 0), (80, 255, 80)).sum()
                ypx = cv2.inRange(traffic_light_roi, (0, 100, 100), (80, 255, 255)).sum()

                # Update total counts
                tred += rpx
                tgreen += gpx
                tyellow += ypx
        
        if tred > tgreen and tred>tyellow:
            print("There are more red pixels in the traffic lights.")
            print("Instruction: Stop")
            # a="There are more red pixels in the traffic lights."
            # new_sentence.append(a)
        if tred < tgreen and tgreen>tyellow:
            b="There are more green pixels in the traffic lights."
            print("There are more green pixels in the traffic lights.")
            print("Instruction: Go")
            # new_sentence.append(b)
        if tyellow > tred and tyellow > tgreen:
            print("There are more yellow pixels in the traffic lights.")
            print("Instruction: Slow down")
        # else:
        #     print("The number of red and green pixels is equal.")
        
        cv2.imshow("Object Detection", output_image)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
# def speech(text):
#     print(text)
#     language='en'
#     output=gTTS(text=text, lang=language, slow=False)
#     output.save("./sounds/output.mp3")
#     playsound("./sounds/output.mp3")
    
    
imgdetection()
#speech(" ".join(new_sentence))