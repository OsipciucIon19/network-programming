# Laboratorul 3. Programarea în rețea

## Tema: HTTP Client

**Să se creeze o aplicație client HTTP**

### Pentru nota 7-8:
* Cererile HTTP să fie făcute prin intermediul unui proxy
* Să se utilizeze expresiile regulate

### Pentru nota 9 si 10:
* Să se utilizeze firele de execuții și tehnici de sincronizare
* Clientul trebuie să se poată autentifica pe resursă utilizînd cookies

### Atenție:
* Pentru acest laborator utilizați librării HTTP deja existente, nu este necesar de a utiliza Socket
API. Cine dorește poate să facă prin socket ca și la primul laborator.
* Clientul trebuie să facă cereri GET, POST, HEAD și OPTIONS
* Aplicația poate fi consolă sau GUI
* Nu sunteți limitați la funcțional, resura(pagina web) la care clientul o să facă cereri HTTP este
la alegere.
* Vă recomand să folosiți proxy private și nu free: https://proxy-seller.com
* Aplicația elaborată trebuie să posede o logică bine definită

### Întrebări la apărarea laboratorului:
* Cum este formatat corpul unei cereri HTTP pentru o cerere HTTP de tip POST ?
* De unde știe un client HTTP ce tip de conținut trimite serverul HTTP ?
* Cum decide un client dacă ar trebui să aibă încredere în certificatul unui server ?
* Care este problema principală cu certificatele autosemnate ?
* Conexiunea persistentă HTTP – care sunt principalele beneficii ?
* Ce este negocierea conținutului în HTTP și cum are loc ?
* Care sunt tipurile de negociere a conținutului HTTP ?
* Ce este un ETag în HTTP și cum funcționează ?
* Diferența dintre protocoalele fără stare și cele cu stare. Cărui tip îi aparține HTTP ?
* Avantajele cheie ale HTTP/2 în comparație cu HTTP/1.1
* Ce este un tip MIME, din ce constă și pentru ce se folosește ?
* Care este diferența dintre GET și POST ?
* Care este diferența dintre PUT și POST ?
* Care sunt metodele idempotente în HTTP și care sunt scopul lor.
* Cum sunt identificate resursele în protocolul HTTP ?
* Care sunt metodele sigure și nesigure în HTTP ?
* Pentru ce este nevoie de cURL ?