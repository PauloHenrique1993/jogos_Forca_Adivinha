import random

def jogar():
  print("*********************************")
  print("Bem vindo ao jogo de Adivinha��o!")
  print("*********************************")

  numero_secreto = random.randrange(1,101)
  total_de_tentativas = 0
  pontos = 1000

  print("Qual o n�vel de dificuldade?")
  print("(1) F�cil (2) M�dio (3) Dif�cil")

  nivel = int(input("Defina o n�vel: "))

  if(nivel == 1):
      total_de_tentativas = 20
  elif(nivel == 2):
      total_de_tentativas = 10
  else:
      total_de_tentativas = 5

  for rodada in range(1, total_de_tentativas + 1):
      print("Tentativa {} de {}".format(rodada, total_de_tentativas))

      chute_str = input("Digite um n�mero entre 1 e 100: ")
      print("Voc� digitou " , chute_str)
      chute = int(chute_str)

      if(chute < 1 or chute > 100):
          print("Voc� deve digitar um n�mero entre 1 e 100!")
          continue

      acertou = chute == numero_secreto
      maior   = chute > numero_secreto
      menor   = chute < numero_secreto

      if(acertou):
          print("Voc� acertou e fez {} pontos!".format(pontos))
          break
      else:
          if(maior):
              print("Voc� errou! O seu chute foi maior do que o n�mero secreto.")
          elif(menor):
              print("Voc� errou! O seu chute foi menor do que o n�mero secreto.")
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos
          
  print("O numero secreto era ",numero_secreto)
  print("Fim do jogo")

if(__name__ == "__main__"): 
  jogar()