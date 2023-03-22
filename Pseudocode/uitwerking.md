programmeer een library in Python 
	met een node class
	met een singly linked list class
    let op je pylint score!

Schrijf de pseudocode om een node met een integer op de juiste plaats toe te voegen in een gesorteerde singly linked list met integers.
    Wat is de tijdscomplexiteit?
    implementeer je pseudocode in Python.

Idem in een gesorteerde array.
    zie BinarySearch


Implementeer een Bag met een singly linked list als interne datacontainer i.p.v. een array of een Python list.
    Vergelijk de tijdscomplexiteit van de verschillende functies met die van de andere versies.

Gegeven een node en een singly linked list als in de volgende ascii-art

[//]: <> (+----------------------------------------+
          |                                        |
          |                  new_node              |
          |                  |                     | 
          |                 {22|NULL}              |
          |                                        |
          |  {73|=>}{2|=>}{52|=>}{18|=>}{36|NULL}  |
          |   |      |                             |
          |   head   cur_node                      |
          |                                        |
          +----------------------------------------+)
Laat in ascii-art de stappen zien die nodig zijn om de nieuwe node direct na de node met daar in 52 toe te voegen
Gebruik geen loop en voeg geen extra externe referenties toe.


  +----------------------------------------+
  |                                        |
  |                  new_node              |
  |                  |                     | 
  |                 {22|NULL}              |
  |                                        |
  |  {73|=>}{2|=>}{52|=>}{18|=>}{36|NULL}  |
  |   |            |                       |
  |   head         cur_node                |
  |                                        |
  +----------------------------------------+
     
  +----------------------------------------+
  |                                        |
  |                  new_node              |
  |                  |                     | 
  |                 {22|   |}              |
  |                        V               |
  |  {73|=>}{2|=>}{52|=>}{18|=>}{36|NULL}  |
  |   |            |                       |
  |   head         cur_node                |
  |                                        |
  +----------------------------------------+

  +----------------------------------------+
  |                                        |
  |                  new_node              |
  |                  |                     | 
  |                  {22|   |}             |
  |                    ^    V              |
  |  {73|=>}{2|=>}{52| |}{18|=>}{36|NULL}  |
  |   |            |                       |
  |   head         cur_node                |
  |                                        |
  +----------------------------------------+


Zoals in de les aangegeven is, kun je ook 'doubly linked lists' hebben
Geef de pseudocode voor het toevoegen van een node aan een doubly linked list
Beredeneer wat hiervan de tijdscomplexiteit is
Geef de pseudocode voor het verwijderen van een node uit een doubly linked list  
Beredeneer wat hiervan de tijdscomplexiteit is

Schrijf de pseudocode om een node met een integer op de juiste plaats toe te voegen in een gesorteerde doubly linked list met integers.
    Wat is de tijdscomplexiteit?
    implementeer je pseudocode in Python.
 
Beredeneer a.d.h.v. pseudocode en/of Python code welke datastructuur je zou nemen om een palindroom-checker te schrijven.

bedenk een algoritme om een array van integers te sorteren en schrijf de pseudocode hiervoor.
    wat is de tijdscomplexiteit van je algoritme?
kijk of je het algoritme wat je bedacht hebt ook in je boek terug kunt vinden
    klopt je analyse van de tijdscomplexiteit van je algoritme met wat er in het boek staat?
implementeer je algoritme in Python
test je code

Computerprocessen krijgen ieder op de beurt processing time. Als het laatste proces aan de beurt is geweest, wordt weer van voren af aan begonnen.
Bedenk/beschrijf in detail een linked structure waarmee je dit zou kunnen implementeren
