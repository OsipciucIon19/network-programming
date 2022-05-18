import cv2
from threading import Thread, Lock


class VideoGrabber(Thread):
    def __init__(self, jpeg_quality):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.buffer = None
        self.lock = Lock()

        self.jpeg_encode_func = lambda img, quality=jpeg_quality: self.cv2_encode_image(img, quality)

    def stop(self):
        self.running = False

    def get_buffer(self):
        if self.buffer is not None:
            self.lock.acquire()
            cpy = self.buffer
            self.lock.release()
            return cpy

    def run(self):
        while self.running:
            success, img = self.cap.read()
            if not success:
                continue

            self.lock.acquire()
            self.buffer = self.jpeg_encode_func(img)
            self.lock.release()

    @staticmethod
    def cv2_encode_image(cv2_img, jpeg_quality):
        encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
        result, buf = cv2.imencode('.jpg', cv2_img, encode_params)
        return buf.tobytes()
