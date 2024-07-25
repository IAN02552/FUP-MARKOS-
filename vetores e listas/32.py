# Faça um programa para ler uma lista de nomes dos alunos de uma turma de até 5 alunos. O programa deve solicitar ao usuário os nomes dos alunos, sempre perguntando se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuário irá indicar um nome que ele deseja verificar se está presente na lista, e o programa deve procurar pelo nome (ou parte deste nome) e, se encontrar, deve exibir na tela o nome completo e o índice do vetor onde está guardado este nome.    

l = []  
op = "S" 
while True: 
    if op == "N":   
        break   
    
    nome = str(input("Aluno: "))   
    l.append(nome)  
    if len(l) == 5: 
        break
    op = str(input("Deseja inserir novo aluno? [S/N] ")).upper() 
pesquisa = str(input("Aluno para pesquisa: "))      
for c in range(len(l)):  
    if pesquisa in l[c]:    
        print(l[c])    
        print(c)