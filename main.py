import cv2

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame from the camera
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Gesture-AI', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
