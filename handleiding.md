# Doel
Op 'metaniveau' over code kunnen nadenken zodat je 'de beste' oplossing (= algoritme) kunt kiezen voordat je begint te hacken. 

# Boek
Problem Solving with Algorithms and Data Structures using Python 2nd edition door B.N. Miller en D.L. Ranum

# Beoordeling
Je wordt beoordeeld a.d.h.v. een tentamen waarop je een aantal theoretische vragen moet beantwoorden, code en pseudocode moet analyseren met behulp van de big-O en zelf wat code moet schrijven.

# Leerdoelen
De bedoeling is dat je na afloop van deze onderwijseenheid je het volgende kunt:
- geschikte datastructuren kiezen en ontwerpen voor problemen
- algoritmen en datastructuren opzetten en gebruiken
- inschattingen maken van de complexiteit en snelheid van algoritmen
## De leerdoelen die getoetst zullen worden zijn:
- De student is zelfstandig in staat de tijds- c.q. de geheugencomplexiteit van een algoritme te analyseren
- De student is zelfstandig in staat om standaard sorteer- en zoekalgoritmen te beschrijven en te gebruiken.
- De student is zelfstandig in staat om bomen en verwante structuren, zoals heaps, te gebruiken bij het oplossen van problemen.
- De student is zelfstandig in staat om arrays en de diverse vormen van linked lists te gebruiken bij het oplossen van problemen
- De student is zelfstandig in staat om stacks en de diverse queues, te gebruiken bij het oplossen van problemen
- De student is zelfstandig in staat om maps en dictionaries te gebruiken bij het oplossen van problemen
- De student is zelfstandig in staat om recursie te gebruiken bij het oplossen van problemen

# Verwachte voorkennis
- Objectgeörienteerd kunnen coderen in Python3
- Kunnen omgaan met modules in Python
- Kunnen werken in een terminal onder Linux
- Kunnen omgaan met pylint
- Gebruik maken van pydoc

# Invulling van de lessen
De lessen zullen over het algemeen beginnen met een plenair gedeelte waarin ik de theorie in het boek nader toelicht. Vervolgens kun je zelf aan de slag met het bestuderen van de stof en het maken van de opgaven die je hierbij helpen. Voor elke les komen er aparte bestanden met opgaven beschikbaar. De opgaven zijn vergelijkbaar met de vragen op het tentamen. Mocht er iets onduidelijk zijn of heb je vragen over de opaven of de stof dan kun je tijdens dit deel van de les persoonlijke begeleiding vragen.

# Planning
## Les 1: Inleiding & Herhaling
De in deze les behandelde stof zou je, in ieder geval grotendeels, al moeten beheersen. Voor de volledigheid geef ik hier nog een aantal mogelijke bronnen voor zelfstudie.

### Gebruik CLI
Er wordt van je verwacht dat je onder Linux in een terminal emulator kunt werken. Je moet in ieder geval het bestandssysteem kunnen navigeren, een programma kunnen starten en rechten doelgericht kunnen veranderen.
Zie o.a. [linuxcommand](http://linuxcommand.org/)

### Pydoc en Python Help
Python heeft krachtige ingebouwde hulpfuncties waar je al mee om hebt leren gaan. Voor propriëtaire functies en modules is dit vaak de enige hulpbron die beschikbaar is. Op het tentamen zal dit de enige beschikbare bron van documentatie zijn. 
Zie o.a [de Python documentatie](https://docs.python.org/3/library/pydoc.html),
    [Socratica tutorial](https://www.youtube.com/watch?v=URBSvqib0xw) en
    [Socratica tutorial](https://www.youtube.com/watch?v=BVXv0-1Rcc8)

### Modules in Python
Je moet niet alleen willekeurige modules kunnen importeren, maar ook zelf kunnen schrijven.
Zie o.a. [de python documentatie](https://docs.python.org/3/tutorial/modules.html)

### Gebruik Pylint
Gedurende de opleiding is er steeds op gewezen dat je code moet voldoen aan de [PEP8](https://www.python.org/dev/peps/pep-0008/) standaard. Dit kun je controleren met behulp van een 'linter', bijvoorbeeld [pylint](https://www.pylint.org/). 
Op het www zijn er genoeg tutorials te vinden over hoe je pylint gebruikt. Zie [bijvoorbeeld](https://docs.pylint.org/en/1.6.0/tutorial.html).

### Object geörienteerd programmeren in Python
Je moet in staat zijn om zelf correcte klasses te schrijven in Python en al geschreven klasses te gebruiken. Verder moet je standaardbegrippen van het objectgeörienteerd programmeren zoals klasse, object, overerving, encapsulatie, veld of property, method e.d. kunnen gebruiken. 
    Ook hiervoor zijn op het internet een plethora aan relevante pagina's te vinden, bijvoorbeeld [de python tutorial zelf](https://docs.python.org/3/tutorial/classes.html) of [Socratica tutorial](https://www.youtube.com/watch?v=apACNr7DC_s). Voor het berbuik van de property decorator zie [hier](https://docs.python.org/3/library/functions.html?highlight=property#property).

### (nieuw) UML klasse diagram
Een UML klasse diagram is een grafische manier om een klasse te beschrijven. Zie hiervoor de relevante presentatie in de BlackBoard cursus.


### (nieuw) Algoritmen en Datastructuren
- Zijn beschrijvingen van oplossingen voor problemen (vgl. recepten)
- Een algoritme kun je beschrijven met behulp van pseudocode (zie toelichting blackboard)
- Aan de hand van de pseudocode kan een algoritme geanalyseerd worden op tijds- en geheugenefficiëntie voordat er gecodeerd wordt
- Nadat een algoritme is geformuleerd kan deze in programmacode geïmplementeerd worden.
- De manier waarop gegevens beschikbaar zijn, de datastructuur, bepaalt in hoge mate welke algoritmen mogelijk zijn.

### (nieuw) Abstracte datastructuren versus implementatie
- Algoritmen en abstracte datastructuren beschrijvingen c.q. ontwerpen c.q. ideeën
- Code is een implementatie van die algoritmen c.q. abstracte datastructuren
- Bestudeer boek H1.

## Les 2: Abstracte datatypen en implementatie, arrays, O() 
In deze les wordt uitgelegd wat een array is, hoe je een array in Python kunt gebruiken en wat referenties zijn. Verder wordt het gebruik van de big-Oh notatie voor het analyseren van algoritmen uitgelegd.

### Referenties
Zie boek p11

### Arrays
Bestudeer boek H8.1 & 8.2
Zie voor gebruik [de Python standard library array](https://docs.python.org/3/library/array.html) en [ctypes](https://docs.python.org/3/library/ctypes.html#arrays)
Verder bevatten diverse externe bibliotheken zoals [NumPy](https://numpy.org/) en [SciPy](https://www.scipy.org/) ook implementaties van arrays (valt buiten deze cursus).
    
### Algoritme analyse
De 'Big-O' kan gebruikt worden om de prestaties van verschillende algoritmen met elkaar te vergelijken.
Bestudeer boek H2 t/m 2.2.1. Lees de rest van H2.

## Les 3: linked lists en andere linked structures
Bestudeer in het boek H3.6
In de les wordt uitgelegd wat 'doubly linked lists' en 'circular linked lists' zijn.

## Les 4: Zoeken in lineaire structuren
Kijken of een datum in een datastructuur aanwezig is, is een een veel voorkomende bezigheid. In deze les worden hiervoor twee alternatieven gegeven en geanalyseerd.

### Sequential search (a.k.a. lineair search)
Bestudeer boek H5 t/m H5.2.1

### Binary search
Bestudeer boek H5.2.2

## Les 5/6: Sorteren
Bestudeer in het het boek H5.3, 5.4.
Extra: Radix Sort. Zie bijvoorbeeld [wikipedia](https://en.wikipedia.org/wiki/Radix_sort)

## Les 7/8: Stacks en queues
Bestudeer boek H3 t/m 3.3
Bestudeer boek H3.4, 3.5 en 3.7

## Les 9/10: recursie
Bestudeer boek H4 t/m H4.2 en 4.8. Lees H4.3 t/m 4.6

## Les 11/12: Binary Trees en Heaps
Bestudeer boek H6 t/m 6.4, 6.5.2 en H6.7
Lees de rest van H6.5
Bestudeer boek H6.6
Lees H6.8

## Les 13: Hashmaps
Bestudeer boek H5.2.3

## Les 14: Vragen?
