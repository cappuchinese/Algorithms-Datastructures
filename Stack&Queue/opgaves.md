# Stack en Queue

- Bestudeer de relevante hoofdstukken uit het boek

1. Maak een palindroom checker m.b.v. een queue. Gebruik hiervoor de meegeleverde module. 
2. Leg uit hoe je een palindroomchecker kunt maken m.b.v. een deque. 
   - Wat is de tijdscomplexiteit?
3. Geef de pseudocode om een queue met behulp van een of meer stacks te implementeren
   - Beredeneer aan de hand hiervan de tijdscomplexiteit van deze oplossing voor enqueue en dequeue
   - Implementeer dit in Python en gebruik hiervoor de meegeleverde module 
4. Geef de pseudocode om een stack met behulp van een of meer queues te implementeren 
   - Beredeneer aan de hand hiervan de tijdscomplexiteit 
   - Implementeer dit in Python en gebruik hiervoor de meegeleverde module

Hoe kun je een queue maken: 
- m.b.v. een array
- zonder dat je ooit onder water een nieuwe array aan hoeft te maken
- waarbij zowel enqueue als dequeue in O(1) lopen
- Wat voor voorwaarde is hiervoor nodig?
Schrijf hiervoor de pseudocode
Implementeer dit in Python (je mag hiervoor een list gebruiken ipv een array)

Geef de pseudocode voor een stack gebaseerd op een array
- wat is de runtime van push?
- wat is de runtime van pop?
- wat is de runtime van size?
- wat is het geheugengebruik van deze implementatie (uitgedrukt in O())?

Geef de pseudocode voor een stack gebaseerd op een singly linked list
- wat is de runtime van push?
- wat is de runtime van pop?
- wat is de runtime van size?
- wat is het geheugengebruik van deze implementatie (uitgedrukt in O())?

Geef de pseudocode voor de volgende operaties bij een queue gebaseerd op een singly linked list
- enqueue
- dequeue
- size
- Wat is de runtime van deze implementatie van enqueue)?

Beredeneer aan de hand van de O() wat een efficientere implementatie van een stack, m.b.v. een array of m.b.v. een linked list
idem voor een queue
idem voor een dequeue
