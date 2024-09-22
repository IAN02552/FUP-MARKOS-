import random    
def desenho(vetor):   
    for c in range(len(vetor)):   
        for j in range(len(vetor)): 
            if vetor[c][j] != 0:
                print(vetor[c][j],end= "") 
            else:   
                print(" ",end="") 
            if j < len(vetor)-1:    
                print("  |",end="")  
        print() 
        if c < 2:
            print("---+---+--- ")    


def jogar(vetor):   
    desenho(vetor)    
    for j in range(5):   
        while True: 
            l = int(input("Qual a linha? ")) 
            c = int(input("Qual a coluna? "))    
            if (l > 0 and l < 4) and (c > 0 and c < 4): 
                if vetor[l-1][c-1] !="X" and vetor[l-1][c-1] !="O": 
                    vetor[l-1][c-1] = "X"   
                    break   
            else:   
                print("Posição inválida, por favor digite novamente.")  

        if primeiro == 0: 
            if j == 4: 
             
                desenho(vetor)  
                if ganhador(vetor) != None:  
                    print(ganhador(vetor))  
                if ganhador(vetor) == None:
                    print("----EMPATE---")
                break   
        if primeiro == 1: 
            if j == 3: 
                computador(vetor)
                desenho(vetor)  
                if ganhador(vetor) != None:  
                    print(ganhador(vetor))  
                if ganhador(vetor) == None:
                    print("----EMPATE---")
                break  
        if ganhador(vetor) != None: 
            desenho(vetor) 
            print(ganhador(vetor))  
            break
        computador(vetor)    
        desenho(vetor)  
        if ganhador(vetor) != None:  
            print(ganhador(vetor))  
            break  

    
def computador(vetor):    
    while True: 
        l = random.randint(0,3)
        c = random.randint(0,3)    
        if vetor[l-1][c-1] !="X" and vetor[l-1][c-1] !="O": 
            vetor[l-1][c-1] = "O"   
            break   
                

def ganhador(vetor):    
    # sec = secundária     
    checkdiagonal_X = checkdiagonal_O = 0
    checksecdiagonal_X = checksecdiagonal_O = 0
    
    for c in range(3):  
        checklinha_X = checklinha_O = checkcoluna_X = checkcoluna_O = 0  
        
        for j in range(3):  
            # Verifica linhas
            if vetor[c][j] == "X":  
                checklinha_X +=1  
            if vetor[c][j] == "O":  
                checklinha_O +=1    
                
            # Verifica colunas
            if vetor[j][c] == "X":  
                checkcoluna_X +=1  
            if vetor[j][c] == "O":  
                checkcoluna_O +=1   
                
        # Verifica diagonais dentro do loop externo
        if vetor[c][c] == "X":  
            checkdiagonal_X += 1  
        if vetor[c][c] == "O":  
            checkdiagonal_O += 1    
        if vetor[c][2-c] == "X":    
            checksecdiagonal_X +=1  
        if vetor[c][2-c] == "O":    
            checksecdiagonal_O +=1 
        
        # Verifica se há um ganhador nas linhas ou colunas
        if checklinha_X == 3: 
            return "Que droga, você ganhou."    
        if checklinha_O == 3: 
            return "Computador ganhou"  
        if checkcoluna_X == 3: 
            return "Que droga, você ganhou."    
        if checkcoluna_O == 3: 
            return "Computador ganhou"  
    
    # Verifica se há um ganhador nas diagonais
    if checkdiagonal_X == 3: 
        return "Que droga, você ganhou."    
    if checkdiagonal_O == 3: 
        return "Computador ganhou"    
    if checksecdiagonal_X == 3: 
        return "Que droga, você ganhou."  
    if checksecdiagonal_O == 3: 
        return "Computador ganhou"  
    
    return None  
    

vet = [[0]*3,[0]*3,[0]*3]   
primeiro = random.randint(0,1)  
if primeiro == 1:   
    computador(vet)
jogar(vet)
 
