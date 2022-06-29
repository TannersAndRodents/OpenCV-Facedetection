"""Module with important tools detect faces."""

from cv2 import cvtColor, COLOR_BGR2GRAY

class Detector:
    """Class with important methods to detect faces in openCV."""

    def __init__(self) -> None:
        pass

    def detect_cascade(self, frame, haarcascade):
        """Applies the given haarcasecade to the given frame to extract a face, 
        using some standard settings.

        Args:
            frame/picture as array (Gray or Color)
            haarcascade to use
        Returns:
            An array with all found faces:
            [[x position, y position, width, height] [position and dimension of second face ...] ...]
        """

        if len(frame.shape) == 3:
            frame = cvtColor(frame, COLOR_BGR2GRAY)

        faces = haarcascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

        return faces