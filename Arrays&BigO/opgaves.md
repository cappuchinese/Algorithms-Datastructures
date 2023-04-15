# Arrays en BigO

- Bestudeer boek p11
- Bestudeer Arrays
- Bestudeer boek H8.1 & 8.2
    - Zie voor gebruik [de Python standard library array](https://docs.python.org/3/library/array.html) en [ctypes](https://docs.python.org/3/library/ctypes.html#arrays)
    - Verder bevatten diverse externe bibliotheken zoals [NumPy](https://numpy.org/) en [SciPy](https://www.scipy.org/) ook implementaties van arrays (valt buiten deze cursus).

- Bestudeer Algoritme analyse
    - De 'Big-O' kan gebruikt worden om de prestaties van verschillende algoritmen met elkaar te vergelijken.
- Bestudeer boek H2 t/m 2.2.1. Lees de rest van H2.

1. Geef de pseudocode van een algoritme dat de hoogste waarde bepaalt in een array.
2. Geef de pseudocode van een algoritme dat een getal in een gesorteerde array op de goede plaats toevoegt.

3. *A* is een array van getallen waarvan er een dubbel voorkomt.
    - Ontwerp een efficient algoritme (pseudocode) dat het dubbele getal opspoort.
4. Herschrijf Bag m.b.v. array en/of ctype array
5. Schrijf de Python code om twee gesorteerde lists/arrays samen te voegen tot een nieuwe gesorteerde list/array.
6. In welke O() loopt het ophalen van een waarde op een bepaalde positie in een array? Beredeneer dit aan de hand van de stof uit de les.
7. In welke O() loopt het controleren of een bepaalde waarde zich in een array bevindt?
    - Idem, maar in een Bag?
    - Idem, maar bepalen wat de grootste waarde in een Bag is?
8. Kun je de Bag aanpassen zodat het bepalen van de grootste waarde in O(1) loopt?

## H2.6 opdrachten

1. Zet de volgende expressies op volgorde van kleinste naar grootste als n -> oneindig:
    - n*log(n)
    - 4^n
    - k*log(n)
    - 5*n^2
    - 40*log(n)
    - 12*n^6

2. Wat is de tijdscomplexiteit voor de volgende operaties in een Set:
    - difference()
    - intersection()

3. Stel je hebt een set die geïmplementeerd (gebaseerd) is op een list:
    - Beredeneer wat de tijdscomplexiteit is van het toevoegen van een item aan een dergelijke set.
    - Idem, maar van het verwijderen van een item uit een dergelijke set.