import cv2
import os


class Webcam:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Initialize video capture
        self.scaling_factor = 0.5  # scaling factor


    def take_picture(self):

        ret, frame = self.cap.read()  # Capture the current frame
        frame = cv2.resize(frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA)
        cv2.imwrite()


    def show_image(self, frame):

        while True:
            # Display the image
            cv2.imshow('Webcam', frame)

            # Detect if the Esc key has been pressed
            c = cv2.waitKey(1)
            if c == 27:
                break

        # Release the video capture object
        self.cap.release()

        # Close all active windows
        cv2.destroyAllWindows()
