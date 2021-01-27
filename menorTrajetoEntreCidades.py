print(f'-=-*'*9)
print(f'ESCOLHA A SUA ORIGEM E O SEU DESTINO')
cidade = ('A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H')
for d in cidade:
    print(f'Cidade {d}')
print(f'-=-*'*9)

o = str(input('De onde está partindo? ')).strip().upper()
d = str(input('Para onde você vai? ')).strip().upper()
trajeto = [['A', 'B', 'A -> B'], ['A', 'C', 'A -> C'], 	['A', 'D', 'A -> B -> D'], 	['A', 'E', 'A -> B -> E'], 	['A', 'F', 'A -> C -> F'], 	['A', 'G', 'A -> G'], 	['A', 'H', 'A -> G -> H'], 	['B', 'A', 'B -> A'], 	['B', 'C', 'B -> C'], 	['B', 'D', 'B -> D'], 	['B', 'E', 'B -> E'], 	['B', 'F', 'B -> E -> F'], 	['B', 'G', 'B -> C -> G'], 	['B', 'H', 'B -> D -> H'], 	['C', 'A', 'C -> A'], 	['C', 'B', 'C -> B'], 	['C', 'D', 'C -> B -> D'], 	['C', 'E', 'C -> F -> E'], 	['C', 'F', 'C -> F'], 	['C', 'G', 'C -> G'], 	['C', 'H', 'C -> F -> H'], 	['D', 'A', 'D -> B -> A'], 	['D', 'B', 'D -> B'], 	['D', 'C', 'D -> B -> C'], 	['D', 'E', 'D -> E'], 	['D', 'F', 'D -> E -> F'], 	['D', 'G', 'D -> H -> G'], 	['D', 'H', 'D -> H'], 	['E', 'A', 'E -> B -> A'], 	['E', 'B', 'E -> B'], 	['E', 'C', 'E -> F -> C'], 	['E', 'D', 'E -> D'], 	['E', 'F', 'E -> F'], 	['E', 'G', 'E -> F -> G'], 	['E', 'H', 'E -> F -> H'], 	['F', 'A', 'F -> C -> A'], 	['F', 'B', 'F -> E -> B'], 	['F', 'C', 'F -> C'], 	['F', 'D', 'F -> E -> D'], 	['F', 'E', 'F -> E'], 	['F', 'G', 'F -> G'], 	['F', 'H', 'F -> H'], 	['G', 'A', 'G -> A'], 	['G', 'B', 'G -> A -> B'], 	['G', 'C', 'G -> C'], 	['G', 'D', 'G -> H -> D'], 	['G', 'E', 'G -> F -> E'], 	['G', 'F', 'G -> F'], 	['G', 'H', 'G -> H'], 	['H', 'A', 'H -> G -> A'], 	['H', 'B', 'H -> D -> B'], 	['H', 'C', 'H -> F -> C'], 	['H', 'D', 'H -> D'], 	['H', 'E', 'H -> F -> E'], 	['H', 'F', 'H -> F'], 	['H', 'G', 'H -> G'],]

for a in trajeto:
    if a[0] == o and a[1] == d:
        print(f'O menor trajeto saindo da cidade {o} e indo para a cidade {d} é fazendo o caminho entre as cidades {a[2]}')
        print('Boa Viagem !!!!')
if o == d:
    print('*************** ATENÇÃO ***************')
    print(f'O seu destino é a mesma cidade de partida.')

