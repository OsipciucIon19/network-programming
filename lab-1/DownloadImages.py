import socket
import ssl
import threading
from threading import Thread
from urllib.parse import urlparse
import os

sem = threading.Semaphore(2)


class DownloadImages(Thread):
    def __init__(self, image_list, host, port):
        Thread.__init__(self)
        self.HOST = host
        self.image_list = image_list
        self.PORT = port
        self.array1 = []
        self.array2 = []
        self.array3 = []
        self.array4 = []

    def divide_list(self):
        first_array = []
        second_array = []
        for i in range(len(self.image_list)):
            if i % 2 == 0:
                first_array.append(self.image_list[i])
            else:
                second_array.append(self.image_list[i])
        for i in range(len(first_array)):
            if i % 2 == 0:
                self.array1.append(first_array[i])
            else:
                self.array2.append(first_array[i])
        for i in range(len(second_array)):
            if i % 2 == 0:
                self.array3.append(second_array[i])
            else:
                self.array4.append(second_array[i])

    def download_through_sockets(self, name, list_of_images):
        sem.acquire()
        for i in list_of_images[0]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            p = urlparse(i)

            # for utm.md
            if self.PORT == 443:
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                                    ssl_version=ssl.PROTOCOL_SSLv23)
            request_header = 'GET {} HTTP/1.1\r\nHOST: {}\r\n\r\n'.format(p.path, self.HOST).encode()
            s.send(request_header)

            images = b''
            while True:
                data = s.recv(1024)  # a citi cel mult 1024 de octeți,
                if not data:
                    images = images.split(b"\r\n\r\n")  # impartim pe bucati
                    image_path = os.path.join(os.getcwd(), "images", os.path.basename(p.path))
                    with open(image_path, "wb") as f_cont:
                        f_cont.write(images[-1])
                    break
                images += data
            print(threading.current_thread())
            s.close()
        sem.release()

    def start_multi_threading(self):
        thread_list = []
        self.divide_list()
        t1 = Thread(target=self.download_through_sockets, args=(1, [self.array1],))
        t2 = Thread(target=self.download_through_sockets, args=(2, [self.array2],))
        t3 = Thread(target=self.download_through_sockets, args=(3, [self.array3],))
        t4 = Thread(target=self.download_through_sockets, args=(4, [self.array4],))
        thread_list.append(t1)
        thread_list.append(t2)
        thread_list.append(t3)
        thread_list.append(t4)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        for thread in thread_list:
            thread.join()
