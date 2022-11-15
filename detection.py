import cv2


class Detection:
    """
    Facedetection via haar cascades.
    """

    def __init__(self, cascade_file: str):
        self.cascade_file = cascade_file

    def detect_face(self, image: str) -> list:
        """
        Takes a given, detects a face (if possible)
        and returns a list of coordinates.

        :param image: Picture ['.png', '.jpg'].
        :return: List of tuples with coordinates: [(x_start, y_start, x_end, y_end)].
        """

        coordinates = []  # list to save coordinates

        cascade = cv2.CascadeClassifier(file=self.cascade_file)  # Face-Classifier

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grey color
        image_gray = cv2.equalizeHist(image_gray)  # adapt histogram

        faces = cascade.detectMultiScale(image_gray)  # face detection

        for x, y, width, height in faces:  # e.g. [(0, 0, 42, 69), (0, 0, 42, 69)] "2-Faces"
            coordinates.append((x, y, x + width, y + height))  # save coordinates

        return coordinates
