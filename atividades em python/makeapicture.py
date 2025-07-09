def Tirar_foto():
    import cv2
    import numpy as np

    # Initialize the camera
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = camera.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        return

    # Save the captured image
    cv2.imwrite('captured_image.jpg', frame)

    # Release the camera
    camera.release()