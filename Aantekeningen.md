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

## Zoek algoritmes
Linear search:
```python
def linear_search(L, item):
	n = len(L)
	for i in range(n):
		if L[i] == item:
			return True
	return False
```

Binary search:
```python
def binsearch1(L, item):
	low = 0
	high = len(L) – 1
	while low <= high:
		mid = (high + low) // 2
		if L[mid] == item:
			return True
		elif item < L[mid]:
			high = mid – 1
		else:
			low = mid + 1
	return False

def binsearch2(L, item):
	mid = len(L) // 2
	if L[mid] == item:
		return True
	elif mid == 1:
		return False
	elif item < L[mid]:
		return binsearch2(L[:mid])
	else:
		return binsearch2(L[mid:])
```

## Sorteer algoritme
Bubble sort: Itereert elke keer en vergelijkt 2 consecutive items met elkaar en zet de hoogste omhoog. Blijft het herhalen tot het gesorteerd is.
Selection sort: Zoekt de kleinste item en zet hem op de goede plaats
Insertion sort: Itereert door de sequentie en zet elk item op de goede plaats
