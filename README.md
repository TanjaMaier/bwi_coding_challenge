# BWI Coding Challenge

Code für die Teilnahme an der BWI Coding Challenge (https://www.get-in-it.de/coding-challenge).

&nbsp;
## Requirements und Ausführung:

Requirements:
- numpy
- pulp

Die Requirements können über pip mit folgendem Befehl installiert werden:

```
pip3 install -r requirements.txt
```

Das Programm wird mit folgendem Befehl ausgeführt:

```
python3 opt_transport.py
```

&nbsp;
## Algorithmus:

Für die Lösung des Problems wird auf Integer Linear Programming zurückgegriffen, da es sich hier um ein klassisches lineares Optimierungsproblem (Nutzenmaximierung) mit linearen Nebenbedingungen (begrenzte Anzahl an Einheiten, begrenztes Fassungsvermögen der Transporter, etc.) handelt, dessen Lösung ganzzahlig sein muss.
Zum Modellieren und Lösen des Problems wird PuLP verwendet: https://pypi.org/project/PuLP/

Der Lösungsvektor x := [x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>19</sub>, x<sub>20</sub>] ist wie folgt definiert:

&nbsp; x<sub>1</sub> =  Anzahl Notebook Büro 13"    in Transporter 1  
&nbsp; x<sub>2</sub> =  Anzahl Notebook Büro 14"    in Transporter 1  
&nbsp; ...  
&nbsp; x<sub>9</sub> =  Anzahl Tablet outdoor klein in Transporter 1  
&nbsp; x<sub>10</sub> = Anzahl Tablet outdoor groß  in Transporter 1  
&nbsp; x<sub>11</sub> = Anzahl Notebook Büro 13"    in Transporter 2  
&nbsp; x<sub>12</sub> = Anzahl Notebook Büro 14"    in Transporter 2  
&nbsp; ...  
&nbsp; x<sub>19</sub> = Anzahl Tablet outdoor klein in Transporter 2  
&nbsp; x<sub>20</sub> = Anzahl Tablet outdoor groß  in Transporter 2  

Die Nebenbedingungen für das jeweilige Ladegewicht der Transporter können wie folgt definiert werden:

&nbsp; &sum;<sub>i = 1</sub><sup>10</sup> g<sub>i</sub> &middot; x<sub>i</sub> &leq; 1100000 - 72400

und

&nbsp; &sum;<sub>i = 11</sub><sup>20</sup> g<sub>i-10</sub> &middot; x<sub>i</sub> &leq; 1100000 - 85700,

wobei g<sub>i</sub> das Gewicht von Gerät i pro Einheit in Gramm angibt, i = 1, ..., 10.

Zudem darf die Gesamtzahl für jedes Gerät die benötigte Anzahl e<sub>i</sub> an Einheiten nicht übersteigen.

&nbsp; x<sub>i</sub> + x<sub>i+10</sub> &leq; e<sub>i</sub> &nbsp; &forall; i = 1, ..., 10.

&nbsp;
## Optimale Verteilung der Hardware:

Gesamtnutzen: &nbsp; __74660__

Gesamtanzahl der jeweils transportierten Geräte:

Gerät | Anzahl
----- | ------
Notebook Büro 13" | 0
Notebook Büro 14" | 0
Notebook outdoor | 0
Mobiltelefon Büro | 60
Mobiltelefon Outdoor | 157
Mobiltelefon Heavy Duty | 220
Tablet Büro klein | 595
Tablet Büro groß | 0
Tablet outdoor klein | 4
Tablet outdoor groß | 370

&nbsp;

Anzahl der jeweils transportierten Geräte in Transporter 1:

Gerät | Anzahl
----- | ------
Notebook Büro 13" | 0
Notebook Büro 14" | 0
Notebook outdoor | 0
Mobiltelefon Büro | 27
Mobiltelefon Outdoor | 0
Mobiltelefon Heavy Duty | 4
Tablet Büro klein | 358
Tablet Büro groß | 0
Tablet outdoor klein | 2
Tablet outdoor groß | 251

&nbsp;

Anzahl der jeweils transportierten Geräte in Transporter 2:

Gerät | Anzahl
----- | ------
Notebook Büro 13" | 0
Notebook Büro 14" | 0
Notebook outdoor | 0
Mobiltelefon Büro | 33
Mobiltelefon Outdoor | 157
Mobiltelefon Heavy Duty | 216
Tablet Büro klein | 237
Tablet Büro groß | 0
Tablet outdoor klein | 2
Tablet outdoor groß | 119