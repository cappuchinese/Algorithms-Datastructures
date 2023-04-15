#!/usr/bin/python3

def get_gametes_recursively(genomestring):
	
	#grenswaarde:
	if len(genomestring) == 2:
		gametes = []
		gametes.append(genomestring[0])
		gametes.append(genomestring[1])
		return gametes
	else:
		gen_alleles = genomestring[0:2]
		#nadert grenswaarde
		shorter_genome = genomestring[2:]
		#recursieve functie call
		old_gametes = get_gametes_recursively(shorter_genome)
		
		gametes = [x + y for x in old_gametes for y in gen_alleles]
#		equivalent aan: ;0)
#		gametes = []		
#		for gamete in old_gametes:
#			gametes.append(gamete + gen_alleles[0])
#			gametes.append(gamete + gen_alleles[1])
		
		return gametes
