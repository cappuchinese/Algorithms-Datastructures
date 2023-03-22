# Algoritme & Datastructuren
Naam: Lisa Hu<br>
Docent: Arne Poortinga (PARN)

## Pseudocode
```
NaamVanDeProcedure
Doel: korte_omschrijving
Input: namen en typen van de input, omschrijving
Output: omschrijving en type van de output
Precondities:
Postcondities:
Algoritme:
#compleet, kort, nauwkeurig
#geen Python code!
#blokken geindenteerd, vgl. Python
```

## Geheugen
| Taal     | Stack (lineair data structuur)     | Heap (hierarchisch datastructuur)  |
|----------|------------------------------------|------------------------------------|
| Algemeen | Naam var: memory link naar object1 | object1                            |
| Python   | Naam var: refereert naar object2   | object2 met referenties naar items |

## Big O notatie
O(n) met O als functie en n de variabele, geeft tijdsverloop aan

- 1 loop = O(n)
- x aantal nested loops = O(n^x)
- Exponentieel = O(a^n)
- Logaritmisch = O(log n)

## Stack
- LIFO structuur: Last In, First Out
```
s = Stack()         s.isEmpty() -> True         s = []
                    s.peek() -> null
                    s.size() -> 0

s.push(5)           s.isEmpty() -> False        s = [5]
                    s.peek() -> 5
                    s.size() -> 1

s.push(8)           s.peek() -> 8               s = [5, 8]
                    s.size() -> 2

s.push(7)           s.peek() -> 7               s = [5, 8, 7]
                    s.size() -> 3

s.pop()             s.peek() -> 8               s = [5, 8]
                    s.size() -> 2
```

## Queue
- FIFO structuur: First In, First Out
```
q = Queue()         q.isEmpty() -> True         q = []
                    q.size() -> 0

q.enqueue(5)        q.isEmpty() -> True         q = [5]
                    q.size() -> 1

q.enqueue(8)        q.size() -> 2               q = [5, 8]

q.enqueue(7)        q.size() -> 3               q = [5, 8, 7]

q.dequeue()         q.size() -> 2               q = [8, 7]
```

### Een Queue van Stacks
Alle bovenste items eerst naar een andere Stack. Dan de laatste item checken.