#bibliotecas
import time
from random import randint

vida_do_monstro = 20
vida = 13

#historinha
print ("Bem vindo aventureiro ! Você está prestes a entrar no sombrio mundo da programação")
time.sleep(1.5)
print ("\nUm mundo no qual pessoas mudam, para piores...")
time.sleep(1.5)
print ("\nVocê batalhara nesse mundo, enfrentara inimigos e muito provalvemente não voltara são da cabeça")
time.sleep(1.5)
print ("\nEstamos entrando no mundo de Programaçãolandia")
time.sleep(1.5)
personagem = input("\nAgora escolha seu personagem, um mago fodastico tipo Gandalf e Dumbledore ou um guerreiro tipo Ragnar ou Rei Arthur com uma espada pegando fogo \n-> ")

#codigo
while True:
    if not "Mago" in personagem and not "Guerreiro" in personagem:
        continue
    break
         

   #guerreiro
if personagem == "Guerreiro":


     personagem == "Guerreiro"    
     print (f"\nAgora você está entrando nas masmoras, e se depara com o monstro C, um dos mais antigos monstros, ele tem {vida_do_monstro} de vida. Você como {personagem} faz o que?\n")
     time.sleep(1.5)
     acao = input("Escolha sua acao: \n Atacar \n Defender \n Curar \n Descansar: ")
     if  not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
       atacar = randint(3, 10)
       ataque_monstro = 3
       vida = 13
       cura = vida + 1
       descansar = randint(1,5)
       poder = randint(5, 10)

       if acao == "Atacar":
        poder -= 2
        vida -= ataque_monstro
        vida_do_monstro -= atacar
        print(f"Sua vida: {vida}")
        print(f"Dano do ataque foi: {atacar}")
        print(f"A vida do monstro: {vida_do_monstro}")
        print(f"Ataque do monstro foi: {ataque_monstro} ")
    
       elif acao == "Defender":
        poder -= 1
        print(f"Sua vida: {vida}")
        print(f"A vida do monstro: {vida_do_monstro}")
    
       elif acao == "Curar":
        vida += cura
        vida -= ataque_monstro
        print(f"Sua vida: {vida}")
        print(f"Dano do ataque foi: {atacar}")
        print(f"Ataque do monstro foi: {ataque_monstro} ")
    
       elif acao == "Descansar":
        poder += descansar
        vida -= ataque_monstro
    
     else:
        print("Por favor digite novamente")   
       

#mago
else:
    personagem == "Mago"    
    print (f"\nAgora você está entrando nas masmoras, e se depara com o monstro C, um dos mais antigos monstros, ele tem {vida_do_monstro} de vida. Você como {personagem} faz o que?\n")
    time.sleep(1.5)

    acao = input("Escolha sua acao: \n Atacar \n Defender \n Curar \n Descansar: ")
    if  not "Atacar" in acao or not "Defender" in acao or not "Curar" in acao or not "Descansar" in acao:
       atacar = randint(0, 8)
       ataque_monstro = 3
       vida = 13
       cura = vida + 2
       descansar = randint(1,5)
       poder = randint(5, 10)

       if acao == "Atacar":
        poder -= 2
        vida -= ataque_monstro
        vida_do_monstro -= atacar
        print(f"Sua vida: {vida}")
        print(f"Dano do ataque foi: {atacar}")
        print(f"A vida do monstro: {vida_do_monstro}")
        print(f"Ataque do monstro foi: {ataque_monstro} ")
    
       elif acao == "Defender":
        poder -= 1
        print(f"Sua vida: {vida}")
        print(f"A vida do monstro: {vida_do_monstro}")
    
       elif acao == "Curar":
        vida += cura
        vida -= ataque_monstro
        print(f"Sua vida: {vida}")
        print(f"Dano do ataque foi: {atacar}")
        print(f"Ataque do monstro foi: {ataque_monstro} ")
    
       elif acao == "Descansar":
        poder += descansar
        vida -= ataque_monstro
    
    else:
        print("Por favor digite novamente")   

if vida == 0:
    "Você morreu, gamer over"
    exit()
if vida_do_monstro == 0:
    "Parabens! Você ganou o monstro morreu"
    exit ()        


  
     
