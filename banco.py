print("bem vindo ao Banco virtual!")
sal = float(input("Digite seu Saldo:"))
                
opç = 0
newsal = 0
while opç != 4:
        
        opç = int(input(" Digite: 1 se quiser ver seu saldo \n Digite: 2 se quiser depositar \n Digite: 3 se quiser sacar \n Digite: 4 se quiser sair \n"))
        
        if opç == 1:
                print("Seu saldo é:",sal)
        
        elif opç == 2:
            dep = float(input("Digite o valor do deposito:"))
            
            if dep > 0:
                newsal = sal + dep
                print("seu saldo é:",newsal)
                sal = newsal
            else:
                print("operação invalida.")
        
        elif opç == 3:
            sacsaldo = float(input("digite o valor que deseja sacar"))
            
            if sacsaldo < sal:
                newsal = sal - sacsaldo
                print("seu saldo é: ",newsal)
                sal = newsal
            else:
             print("saldo invalido.")
        
        elif opç == 4: 
            print("Obrigado por usar nosso sistema!")

        else:
             print("Digite uma opção valida!")

            