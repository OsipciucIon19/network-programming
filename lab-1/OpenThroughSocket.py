import os
import socket
import re
import ssl
import io


class OpenThroughSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.dd = ""
        self.links_to_images = []

    def get_links(self):
        """
        :return:
        data of site
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Socket utm.md : 443
            s.connect((self.host, self.port))

            if self.port == 443:
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                                    ssl_version=ssl.PROTOCOL_SSLv23)
            request_header = 'GET / HTTP/1.0\r\nHOST: {}' \
                             '\r\nAccept: text/html' \
                             '\r\nConnection: keep-alive' \
                             '\r\nKeep-Alive: timeout=1, max=1000' \
                             '\r\nAccept-Language: ro,en' \
                             '\r\nAllow: GET' \
                             '\r\nDNT: 1' \
                             '\r\nSave-Data: on\r\n\r\n'.format(self.host).encode("utf-8")
            s.send(request_header)
            self.dd = b''
            while True:
                temp = s.recv(8048)
                if len(temp) == 0:
                    break
                else:
                    self.dd += temp
            s.close()
        code_of_page = (self.dd.decode("utf-8"))
        with io.open(os.path.join(os.getcwd(), "context.txt"), "w", encoding="utf-8") as file:
            file.write(code_of_page)
        with io.open(os.path.join(os.getcwd(), "context.txt"), 'r', encoding="utf-8") as file:
            # utm.md : 443

            x = file.readlines()

            if self.port == 443:
                urls = []
                for line_in_file in x:
                    results = re.findall("[^\"']*\\.(?:png|jpg|gif)", line_in_file)
                    for y in results:
                        if "https://" not in y:
                            y = "https://utm.md" + y
                        urls.append(y)
                urls = list(set(urls))
                self.links_to_images = urls

            # me.utm.md : 80

            if self.port == 80:
                tmp_img = re.findall("[^\"']*\\.(?:png|jpg|gif)", str(x))
                if tmp_img is not None:
                    self.links_to_images = tmp_img

            if self.host == "me.utm.md":
                links = []
                for link in self.links_to_images:
                    if link.startswith("http://"):
                        links.append(link)
                    else:
                        links.append("http://me.utm.md/" + link)
                    self.links_to_images = links

            return self.links_to_images
