# Linked Structures
```
naam: AddItem
Doel: voeg een integer toe op de goede plaats in een sll
precondities: de sll is gesorteerd
postcondities: na de functie is het item toegevoegd; de sll is nog steeds gesorteerd
input: sll L, int x
output:

Alg:
- maak node met x genaamd N
- maak node N met x

positie = 0
positie_gevonden = False
huidigeNode = L.eersteNode

zolang niet aan het einde van L en positie_gevonden == False:
	als waarde in huidigeNode > x:
		positie_gevonden = True
	anders:
        huidigeNode = huidigeNode.nextNode
		positie = positie + 1

teller = -1
M = L.eersteNode
zolang teller + 1 < positie:
	teller = teller + 1
	M = M.getNextNode

zet N.nextnode = M.nextNode
als teller == -1:
    #toevoegen aan begin
    L.firstNode = N
anders:
    M.nextNode = N

```

```
Alternatief:

- maak node met x genaamd N
N = Node(x)

vorigeNode = L.eersteNode
volgendeNode = vorigeNode.eersteNode
klaar = False

zolang klaar == False en volgendeNode.nextnode niet null:
	als volgendeNode.waarde =< N.waarde:
		N.nextNode = volgendeNode
		klaar = True
        als vorigeNode == L.firstNode:
            L.firstNode = N
        anders:
		    vorigeNode.nextNode = N
	anders:
		vorigeNode = vorigeNode.nextNode
		volgendeNode = vorigeNode.nextNode
```
