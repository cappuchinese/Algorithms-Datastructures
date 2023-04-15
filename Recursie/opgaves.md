# Recursie

- Geef de pseude code voor een functie die twee waarden recursief met elkaar vermenigvuldigt (je mag alleen optellen en aftrekken)
- Maak een recursieve functie in je singly linked list die de waarden van alle nodes uitprint in omgekeerde volgorde
- Geef een recursieve definitie van een singly linked list
- Geef de pseudocode voor een recursieve functie die het maximum in een array vindt
  - Wat is de runtime van deze functie?
- Schrijf in Python een functie die recursief bepaalt of de input een palindroom string is. Je mag geen gebruik maken van reguliere expressies.
- Schrijf in Python een functie die recursief een lijst maakt van alle files in een directory en zijn subdirectories. Wees sportief en gebruik niet os.walk() ;0)


Implementeer het volgende in Python: 
```
Naam: determine_gametes_recursively
Doel: Bepaal alle mogelijke gameten die een bepaald genotype kan produceren
precondities: een genotype wordt als een string weergegeven.
    Elk genotype bevat voor elke eigenschap twee allelen die door dezelfde letter worden weergegeven
	Hoofdletters geven dominante eigenschappen weer, normale letters recessieve.
        Bijvoorbeeld voor een genotype met twee eigenschappen zou de input kunnen zijn:
        AaBb of aaBB of AABB of ...
postcondities: een gameet wordt als een string weergegeven
    gameten bevat alle mogelijke genotypen.
    Een bepaalde gameet kan vaker voorkomen.
    Een gameet bevat van elk gen maar 1 allel
Input: string genotype 
Output: gameten: Lijst die de mogelijke genotypen voor de gameten bevat. De gameten bevatten maar 1 allel voor elke eigenschap, maar het formaat is verder hetzelfde als input
```
