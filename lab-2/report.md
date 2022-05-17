 # Laboratorul 2. Programarea in retea

## Tema: SMTP / POP3 / IMAP

**Sa se creeze un program client de posta electronica (MUA - Mail User Agent) apt sa trimita si sa citeasca mesajele 
prin intermediul unui cont de posta electronica.**

### Pentru nota 9 si 10:
* Sa se poata afisa si fisiere in mesaj ce nu depasesc 2MB, cele care depasesc sa fie respinse
* Sa se creeze un GUI (Graphical User Interface) pentru clientul de posta electronica

### Atentie:
* Pentru acest laborator utilizati librarii deja existente pentru SMTP, POP3 sau IMAP, nu este necesar de a utiliza
socket. Cine doreste poate sa faca prin socket ca si in primul laborator.
* Pentru contul postei electronice puteti alege Yandex, Gmail, Yahoo Mail, Outlook, GMX, etc.
* Pentru a transmite mesajele utilizati SMTP, pentru a extrage si citi mesajele utilizati POP3 sau IMAP, la dorinta.

### Intrebari la apararea laboratorului:
* Scopul protocolului SMTP
  - SMTP face parte din stratul aplicatiei de protocol TCP/IP. Folosind un proces numit **store and forward**, SMTP
  trimite emailurile prin intermediul retelelor de calculatoare. Lucreaza indeaproape cu un agent de mail transfering,
  numit Mail Transfer Agent (MTA), pentru a trimite comunicarea conexiunii la calculatorul potrivit si catre casuta de
  mesaje primite.

* Cum se poate verifica daca serverul SMTP functioneaza utilizand linia de comanda?
  - telnet.smtp.gmail.com 465

* Care sunt comenzile SMTP?
  - HELO - identificare computer expeditor
  - EHLO - identificare computer expeditor cu cere de mod extins
  - MAIL FROM - specificarea expeditorului
  - RCPT TO - specificarea destinatarului
  - DATA - continutul mesajului
  - RSET - reset
  - QUIT - termina sesiunea
  - HELP - ajutor pentru comenzi
  - VRFY - verifica o adresa
  - EXPN - expandeaza o adresa
  - VERB - informatii detaliate

* Pentru ce este nevoie de MUA, MSA, MTA si MDA?
  - MUA (Agent utilizator de posta) - Aplicatie client permite primirea si trimiterea de e-mailuri. Poate fi o aplicatie
  desktop, cum ar fi Outlook, Thunderbird, s.a. sau bazata pe web, cum ar fi: Gmail, Hotmail, s.a.
  - MSA (Agent de trimitere a corespondentei) - un program de server care primeste e-mail de la un MUA, verifica
  eventualele erori si il transera (cu SMTP) catre MTA gazduit pe acelasi server.
  - MTA (Agent de transfer postal) - O aplicatie server care primeste mesaje de la MSA sau de la un alt MTA. Acesta va
  gasi (prin intermediul serverelor de nume si DNS) inregistrarea MX din zona DNS a domeniului destinatarului pentru a
  sti cum sa transfere e-mailul. Apoi transfera posta catre un alt MTA (cunoscut sub numele de SMTP relaying).
  - MDA (Mail Delivery Agent) - Un program de server care primeste mesaje de la MTA ale serverului si le stocheaza in
  cutia postala. MDA este cunoscut sub numele de LDA (Local Delivery Agent).

* Care este diferenta dintre porturile 25, 465 si 587?
  - Sunt porturi SMTP, doar ca portul 25 este blocat sau restrictionat de majoritatea providerilor, pentru a reduce
  numarul de emailuri nedorite din reteaua lor. Portul 465 nu a fost inregistrat ca un canal oficial de transmisie de
  catre IEFT si de IANA, este sigur deoarece utilizeaza SSL. Portul 587 va reduce numarul de mesaje respinse.

* Care este diferenta dintre porturile 110 si 995?
  - 110 - POP3 port necriptat
  - 995 - POP3 port criptat

* Care este diferenta dintre porturile 143 si 993?
  - 143 - IMAP port nesecurizat
  - 993 - IMAP port securizat

* Cum functioneaza protocolul SMTP?
  - Comunicarea intre client si server se realizeaza prin texte ASCII. Initial clientul stabileste conexiunea catre
  server si asteapta ca serverul sa-i raspunda cu mesajul "220 Service Ready". Daca serverul e supraincarcat, poate sa
  intarzie cu primirea acestui raspuns. Dupa primirea mesajului cu codul 220, clientul trimite comanda HELO prin care
  isi va indica identitatea. In unele sisteme mai vechi se trimite comanda EHLO, comanda EHLO indicand faptul ca
  expeditorul mesajului poate sa proceseze extensiile serviciului si doreste sa primeasca o lista cu extensiile pe care
  le suporta serverul. Daca clientul trimite EHLO iar serverul ii raspunde ca aceasta comanda nu e recunoscuta, clientul
  va avea posibilitatea sa revina si sa trimita HELO.
  
    Odata ce comunicarea a fost stabilita, clientul poate trimite unul sau mai multe mesaje, poate incheia conexiunea
  sau poate folosi unele servicii precum verificarea adreselor de e-mail. Serverul trebuie sa raspunda dupa fiecare
  comanda indicand astfel daca aceasta a fost acceptata, daca se mai asteapta comenzi sau daca exista erori in scrierea
  acestor comenzi.

* Scopul protocoalelor POP3 si IMAP
  - IMAP si POP3 reprezinta doua protocoale de mail pe care aplicatiile le folosesc pentru a accesa casuta postala
  virtuala stocata pe computere la distanta.

* Diferenta dintre POP3 si IMAP
  - Un cont de email POP3 descarca mailul pe computerul local in mod implicit. 1 dispozitiv IMAP presupune accesarea
  emailurilor din locatii multiple, deoarece emailurile raman salvate pe serverul de mailing al ISP-ului.

* Cum sa verificati daca exista o adresa de e-mail fara a trimite un e-mail?
  - Cu comanda smtp VERIFY

* Diferenta dintre SSL si TLS
  - Principala diferenta intre SSL si TLS este ca SSL este un protocol care asigura securitatea comunicatiilor intr-o
  retea de calculatoare, in timp ce protocolul TSL este o evolutie a protocolului SSL si consta in caracteristici
  suplimentare de confidentialitate si securitate.
    SSL este un protocol folosit pentru a trimite informatii in siguranta prin retea. Site-urile Web utilizeaza SSL
  pentru a asigura securizarea paginilor de utilizator si pentru checkouts online. Acesta cripteaza datele pentru a
  evita accesul unei terte parti la datele de transmitie. Pe de alta parte, TLS este un succesor al SSL. Ofera
  confidentialitate, integritate si protectie a datelor.


RFC - request for comments 