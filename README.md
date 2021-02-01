# Data-science-and-Iot
Functie van het gemaakte product:
De functie van het product is dat de energie waardes te zien zijn op een website en zodat er een duidelijk overzicht ontstaat van het energieverbruik en de eventuele terug levering van energie.

Idee
Ik ben op het idee gekomen om data uit te lezen van een slimme meter. Ik ben hier op gekomen doordat wij thuis zonnepanelen hebben en het altijd veel werk is om te checken wat de zonnepanelen opgeleverd hebben. Daarom wilde ik dit programma maken. Om het duidelijk en visueel te maken stuur ik alle data door naar een website.

Benodigdheden( Hardware):
•	Slimme meter met P1 aansluiting
•	P1 kabel naar usb
•	Raspberry pi

Benodigheden( software):
•	Putty
•	Winscp
•	Python
•	Thingspeak


Stappenplan om het na te maken:
1.	Zoek uit welke slimme meter er is geïnstalleerd.
2.	Ga naar http://domoticx.com/p1-poort-slimme-meter-hardware/. Zoek de goede slimme meter op in de tabel met de bijbehorende seriële instellingen. Dit is later nodig.
3.	Pas de seriële instellingen aan in het python script om het werkend te maken voor de slimme meter die geïnstalleerd is.
4.	Verbind de P1 kabel met de raspberry pi en de slimme meter.
5.	Open een terminal op de raspberry en voer in: cd /dev
6.	Vul in: ls. Zoek voor ttyUSB in de lijst. De usb zal dan bijvoorbeeld worden: /dev/ttyUSB0.
7.	Vul dit in in het python script bij ser.port in.
8.	Verander in het python bestand de URL die verwijst naar het thingspeak kanaal naar de eigen URL.
9.	Upload het python script naar de raspberry pi. 	
10.	Voer het bestand uit.

Stappenplan:
1.	Goede versie van slimme meter opzoeken en de bijbehorende documentatie. Gevonden op http://domoticx.com/p1-poort-slimme-meter-hardware/ 
2.	Simpel serial read programma maken dat de raw data uitleest van de slimme meter. 
3.	Decoding toegevoegd zodat het mogelijk was om de data uit te lezen op een laptop.
4.	Instellingen verandert en op de raspberry pi werkend krijgen.
5.	Alle data die binnenkomt in een bestand zetten en voor een langere tijd draaien om patronen te kunnen herkennen in de data die binnenkomt.
6.	Het patroon dat er in zit is dat het einde van de data bereikt is als er op de line een ‘!’ staat. Dit is verwerkt in de code zodat het stopt met lezen van data zodra dit bereikt is.
7.	Thingspeak kanaal aanmaken zodat de data daarnaartoe gestuurd kan worden. 
8.	Alle data die van belang eruit filteren zodat alleen de data waar je iets mee kan doorgestuurd kan worden.
9.	Proberen 1 type data door te sturen naar Thingspeak.
10.	Dit stuk code veranderen dat alle type data verstuurd kunnen worden naar Thingspeak.
11.	Error eruit halen waarbij de raspberry pi wifi module in slaap stand gaat.
12.	Product af.


Data pipeline:

Smartmeter --> raspberry 	door middel van p1 kabel naar usb 
Raspberry --> thingspeak	door middel van internet protocol(tcp/udp)

Kijk voor de foto's van het bewijs dat het product werkt op github onder de map img.
 
Er zijn nog meer grafieken maar deze hebben tijdens het testen geen hogere waardes binnen gekregen. Dat komt omdat deze grafieken zijn voor het terug leveren van energie door de zonnepanelen. Op het moment van de metingen en de foto’s was dat nooit hoger dan het huidige verbruik en daarom zijn die grafieken nooit omhoog gegaan.
 
In bovenstaande foto is te zien hoe de raspberry is aangesloten op de slimme meter met een p1 kabel.

Voor code: zie Github

Verbeteringen op product:
Er zijn een paar dingen die later mogelijk verbetert kunnen worden. 
Op dit moment wordt alle data naar thingspeak gestuurd en na een bepaalde tijd verdwijnt de data 
van de website. Om dit te voorkomen kan er gebruik worden gemaakt van een database. Dit kan op 
raspberry pi staan of op een externe server/ harde schijf. Om alle data dan alsnog overzichtelijk weer 
te geven is het het makkelijkst om een website te maken waarbij er gekozen kan worden wat er wordt laten zien. Hier kan bijvoorbeeld een keuze komen welke grafieken je wilt zien of een keuze van welke tijdsperiode je wilt zien. Dit zal het makkelijker maken om een overzicht te krijgen van je energieverbruik.
