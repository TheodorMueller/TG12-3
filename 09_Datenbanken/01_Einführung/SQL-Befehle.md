# SQL
## Struktur SELECT-Befehl
### Aufgabe 1:

Nenne die Unterbefehle, die zum SELECT-Befehl gehören.

>FROM     - Auswahl von Tabellen  
>WHERE    - Eingrenzen der auszugebenen Zeilen   
>GROUP BY -   
>ORDER BY - Sortieren der Zeilen  
>ORDER BY DESC  - absteigende Sortierung  
>ORDER BY ASC - aufsteigende Sortierung  
>
>LIKE  - Vergleich Text mit Muster  z.B ``` name LIKE 'ma%'```  
>AND - Abreage mit mehreren Bedingungen  z.B. ```name LIKE 'ma%' AND status LIKE 'friedlich'```  
>OR  - Abreage mit mehreren Bedingungen  
>COUNT  
>SUM  
>AVG  
>IS NULL - Abfrage, ob ein Attribut keinen Wert hat  
>IN  - Abfrage, ob der Wert des Attributes in einer Liste vorkommt
>  
>UPDATE  - Ändert Daten von Zeilen  
>DELETE  - Löscht Zeilen  

![Tabelle Bewohner](Bilder/Tabelle_Bewohner.jpeg)
![Tabelle Dorf](Bilder/Tabelle_Dorf.jpeg)

  
  
```SQL
SELECT Dorf.dorfnr, Bewohner.bewohnernr FROM Dorf, Bewohner WHERE Dorf.dorfnr = Bewohner.bewohnernr
```
|Dorf.dorfnr|Bewohner.bewohnernr|
|:---:|:---:|
|**1**|**1**|
|~~1~~|~~2~~|
|**1**|**3**|
|~~2~~|~~1~~|
|~~2~~|~~2~~|
|~~2~~|~~3~~|
|~~3~~|~~1~~|
|**3**|**2**|
|~~3~~|~~3~~|