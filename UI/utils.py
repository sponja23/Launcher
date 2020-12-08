from numpy import ndarray
from PyQt5.QtGui import QImage, QPixmap


def ndarrayToPixmap(img: ndarray) -> QPixmap:
    height, width, channel = img.shape
    bpl = 3 * width
    qImg = QImage(img.data, width, height, bpl, QImage.Format_RGB888).rgbSwapped()
    return QPixmap(qImg)
