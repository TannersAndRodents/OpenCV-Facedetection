"""Class with important methods to detect faces in openCV."""

class Detector: 
    """Class with important methods to detect faces in openCV."""

    def __init__(self) -> None:
        pass

    def detect_cascade(self, frame, haarcascade):
        """Applies the given haarcasecade to the given frame to extract a face,  
    using some standard settings.

    Args:
        frame/picture as array
        haarcascade to use
    Returns:
        an array with all found faces:
    [[x position, y position, width, height] [position and dimension of second face ...] ...]"""
        face = haarcascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

        return face
