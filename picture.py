import cv2
import os
from datetime import datetime

from detection import Detection


class Camera:
    """
    Camera class to take pictures.
    """

    def __init__(self, port: int = 0):
        self.capture = cv2.VideoCapture(port)  # initialize the camera at port 0 TODO: check when no camera is pluged in
        self.scaling_factor_x = 0.5  # scaling factor
        self.scaling_factor_y = 0.5  # scaling factor
        self.ramp_frames = 30

    @staticmethod
    def create_timestamp(tsp_format: str = "%d%m%Y_%H%M%S") -> str:
        """
        Creates a timestamp with datetime.
        Default: "%d%m%Y_%H%M%S".

        :param tsp_format: Format of the string.
        :return: Timestamp as string.
        """

        now = datetime.now()
        time_stamp = now.strftime(tsp_format)
        return time_stamp

    def take_picture(self) -> tuple:
        """
        Takes a picture and returns its frame & timestamp.
        :return: (frame, timestamp).
        """

        for i in range(self.ramp_frames):
            self.capture.read()  # wait to initialize camera

        _, frame = self.capture.read()  # Capture the current frame
        timestamp = self.create_timestamp()  # create timestamp

        frame = cv2.resize(frame, None, fx=self.scaling_factor_x, fy=self.scaling_factor_y,
                           interpolation=cv2.INTER_AREA)

        return frame, timestamp

    def save_picture(self, image: str, path: str = "") -> None:
        """
        Save a frame, taken with cv2 as '.png' at a given or default path.
        Default path: cwd.

        :param image: Cv2 image/frame to be saved.
        :param path: Path to save image.
        :return:
        """

        if not path:
            time_stamp = self.create_timestamp()
            path = os.path.join(os.getcwd(), time_stamp + ".png")

        try:
            cv2.imwrite(path, image)  # save image

        except IOError as e:
            print(f"Error saving picture: {e}")

    def show_frame(self, frame: cv2) -> None:
        """
        Display a cv2 frame.

        :param frame: Cv2 frame taken before.
        :return:
        """

        while True:
            cv2.imshow('Webcam', frame)  # Display the image

            if cv2.waitKey(1) == 27:  # Detect if the Esc key has been pressed
                break

        self.capture.release()  # release camera
        cv2.destroyAllWindows()  # Close all active windows


if __name__ == "__main__":
    print(__file__)
