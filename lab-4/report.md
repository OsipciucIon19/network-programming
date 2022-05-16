# Laboratorul 4. Programarea în rețea

## Tema: Aplicatie Client-Server TCP 

**Sa se creeze 0 aplicatie Client-Server TCP utilizand Socket API **

### Pentru nota 9-10:
* Sa definiti, proiectati si elaborati propriul protocolP 

### Atenție:
* Fiecare client trebuie procesat de catre server intr-un fir de executie aparte
* Nu se admite aplicatii simple de genul Echo Client-Server 
* Aplicatia poate fi consola sau GUI 
* Pentru cei ce doresc 9 si 10, ca exemplu luati protocoalele HTTP, SMTP unde clientul si serverul
discuta printr-un set de reguli bine definite. De exemplu, pentru o aplicatie de tip chat pentru ca
clientul sa fie identificat de catre server acesta trebuie sa transmita un mesaj de tipul: HELLOREQUEST dupa care serverul va raspunde cu HELLO-APPROVE. Mai detailat accesati ultimele 3
referinte de la sfirsitul acestui fisier. 

### Intrebari la apararea laboratorului: 
* Ce este un protocol orientat pe conexiune ?
 - Mai poate fi numit protocol orientat pe corectitudinea datelor, se utilizeaza in special pentru
a asigura integritatea informatiei transportate.
* Ce tipuri de aplicatii beneficiaza in general de utilizarea protocolului TCP ?
 - Aplicatiile care au nevoie de integritatea datelor, cum ar fi aplicatiile de transfer a fisierelor,
posta electronica, aplicatiile ce necesita logare, sau un flux de date cu caracter personal
(numere de carduri bancare, idnp, parole...)
* Cum TCP garanteaza ca datele vor fi transmise cu succes ?
 - TCP creeaza o conexiune per to per, Transmite un numar de secvente pe care receptorul este
capabil sa-l prelucreze la care se asociaza numarul de secventa, daca receptorul primeste
numarul de packete definit de secventa, atunci receptorul raspunde cu un mesaj de
confirmare (ACK) pentru packele expediate, in caz contrar, in caza ca serverul nu primeste
confirmare pentru careva pcket atunci acesta este retransmis cu urmatoarea secventa de
pakete.
Diferenta dintre blocking si non-blocking sockets
 - Blocking asteatpta neaparat raspuns din partea la server, iar operatiunile sunt realizate una
dupa alta, pe cand in nom-blocking clientul poate da start la conexiune iar intretimp sa faca alte operatii
ca send(), recvQ), daca utilizatorul in timp ce nu s-a realizat connect() apasa butonul cancel,
putem chema metoda close().
 - Diferenta dintre blocking multithreaded si non-blocking single thread socket

* Cum are loc procesul TCP Three Way Handshake ?
 - In prima faza, Clientul (cel care incepe conexiunea) 11 va trimite serverului:
1. Un mesaj de sincronizare (SYN) sau de incepere a conexiunii
2. Serverul va raspunde cu o confirmare (SYN-ACK)
3. Clientul va raspunde si el cu un mesaj de confirmare (ACK)

* Numiti cele 4 apeluri de sistem necesare pentru a crea un server TCP
 - LISTEN - in cazul unui server se asteapta o solicitare din partea unui client
 - SYN-SENT - se asteapta din partea nodului pereche trimiterea unui segment TCP cu
flagurile de SYN si ACK setate (starea este specifica clientilor ce ruleaz4 protocolul
TCP)
 - SYN-RECEIVED - asteapta din partea nodului pereche a confirmarii ca raspuns la
confirmarea de conectare trimisa catre acesta (stare specifica serverelor cu TCP)
 - ESTABLISHED - portul este pregatit pentru a trimite/primi date catre/dinspre nodul
pereche

* Care este rolul metodei bind() ?
 - Stabilirea adresei, socket-ul respectiv va primi doar cereri de conectare destinate adresei
indicate in bind()

* Care este rolul metodei accept() ?
 - Apelul functiei accept() are ca efect crearea unui socket de cone-xiune, asociat unui client
conectat (prin apelul connect()) la socket-ul de asteptare. Daca nu exista inca nici un client
conectat si pentru care sa nu sa creat socket de conexiune, functia accept() asteapta piana la
conectarea urmatorului client.

* Ce se intimpla cind apelati mai intii connect() apoi bind() ?
 - Functia bind poate apelata doar pentru un socket proaspat creat,caruia nu i s-a atribuit inca o
adresa. Astfel bind(Q) va esua. 

* Ati avea vreodata nevoie sA implementati un timeout intr-un client sau server care
utilizeaza TCP?
 - Desigur, in caz de retineri de lunga durata, v-a trebui sa afisam un mesaj de asteptare sau de
esuare.
* Intr-o conexiune TCP, clientul sau serverul trimite mai intai datele ?
 - Mai intai trimite cereri, primeste raspuns, dupa care trimite datele.

* Care este adresa de loopback IPv4 si care este rolul ei ?
 - Intervalul de la 127.0.0.0 pana la 127.255.255.255, este utilizata pentru a identifica
dispozitivul.

* De unde stie un sistem de operare ce aplicatie este responsabila pentru un pachet
primit din retea ?
 - Prin intermediul setarilor firewall, Prin folosirea unui firewall avem posibilitatea de a seta
exceptii sau de a bloca traficul de date al anumitor aplicatii in functie de caz.
* Datele primite prin recv() au intotdeauna aceeasi dimensiune cu datele trimise cu
send(Q) ?
 - Sistemul garanteaza sosirea la destinatie a tuturor octetilor trimisi(sau instiintarea
receptorului, printr-un cod de eroare, asupra caaderii cone-xiunil), in ordinea in care au fost
trimisi. Nu se pastreaza insa demarcarea intre secventele de octeti trimise in apeluri send()
distincte. De exemplu, este posibil ca emitatorul sa trimita, in doua apeluri succesive, sirurile
abc si def,iar receptorul sa primeasca, in apeluri recv() succesive, sirurile ab, cde , f

* Este acceptabil sa inchei executia programului daca este detectata o eroare de retea ?
 - Da este acceptabil in cazul in care este o eroare de hardware, afisand mesajul informativ.

* Puteti imbunatati performanta aplicatiei prin dezactivarea algoritmului Nagle ?
 - Nagle algoritmul este utilizabil doar cu TCP. Alte protocoale, inclusiv UDP , nu o
accepta.
 - Aplicatiile TCP care au nevoie de raspuns rapid la retea, cum ar fi apelurile telefonice
prin Internet sau jocurile de tip shooter pentru prima persoana, ar putea s4 nu functioneze
bine cand Nagle este activat. Intarzierile cauzate in timp ce algoritmul necesita un timp
suplimentar pentru a asambla mai multe bucati de date mai mici poate provoca o vizibilitate
vizibila pe ecran sau intr-un flux audio digital. Aceste aplicatii dezactiveaza de obicei Nagle.
* Ce instrumente listeazé socket-urile TCP deschise in sistemele de operare Windows si
Linux ?

* Tehnici de sincronizare a firelor de executii
 - Using locks in the with statement - context manager
 - Condition objects with producer and consumer
 - Producer and Consumer with Queue
 - Semaphore objects & thread pool 



