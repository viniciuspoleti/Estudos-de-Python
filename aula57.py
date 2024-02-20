""" 
Lista de listas e seus índices
"""

turmas = [
    #0          1
    ['A', ['Maria', 'Helena', ],
    
    ],
    
    ['B', 
    ['Elaine', ], 
    ],
    
    ['C',     
    ['Luiz', 'João', 'Eduarda', 
     ],
    ]
    
]
#print(salas[2][3][5][1][0])

for turma in turmas:
    
    for sala in turma:
        for aluno in sala:
            print(aluno)