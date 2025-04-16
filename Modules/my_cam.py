import cv2

# Open the default camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

window_name = 'Semantic_Analyzer'


def run_cam():
    
    while True:
        
        ret, frame = cam.read()
        
        frame = cv2.resize(frame, (854, 480))

        # Display the captured frame
        cv2.imshow(window_name, frame)

        # Press 'q' to exit the loop
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    # Release the capture and writer objects
    cam.release()
    cv2.destroyAllWindows()