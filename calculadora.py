import sys
import math

msgsintaxinval = "Sintaxe Inválida!"
msghelpstrs = []
msghelpstrs.append("\nAs operações permitidas são:\n\n")
msghelpstrs.append("[+] : para somar dois números; sintaxe: <numero 1> + <numero 2>\n")
msghelpstrs.append("[-] : para subtrair dois números; sintaxe: <numero 1> + <numero 2>\n")
msghelpstrs.append("[*] : para multiplicar dois números; sintaxe: <numero 1> + <numero 2>\n")
msghelpstrs.append("[/] : para dividir dois números; sintaxe: <numero 1> + <numero 2>\n")
msghelpstrs.append("[sqrt] : para calcular a raiz quadrada de um número; sintaxe: sqrt <numero>\n")
msghelpstrs.append("[sin] : para calcular o seno de um angulo em graus; sintaxe: sin <angulo>\n")
msghelpstrs.append("[cos] : para calcular o coseno de um angulo em graus; sintaxe: cos <angulo>\n")
msghelpstrs.append("[tan] : para calcular a tangente de um angulo em graus; sintaxe: tan <angulo>\n")
msghelpstrs.append("[ln] : para calcular o logaritmo natural, de base e, de um número; sintaxe: ln <numero>\n")
msghelpstrs.append("[log] : para calcular o logaritmo de base 10 de um número; sintaxe: log <numero>\n")
msghelpstrs.append("[!] : para calcular o fatorial de um número; sintaxe: ! <numero>\n")
msghelpstrs.append("[pi] : retorna a constante pi; sintaxe: pi\n")
msghelpstrs.append("[e] : retorna a constante e; sintaxe: e\n")
msghelpstrs.append("\n..................................................................\n\n")
msghelpstrs.append("[q] : para sair\n")


# dicionário de operações
ops = {
      "sqrt": (lambda x: math.sqrt(x)),
      "sin": (lambda x: math.sin(x)),
      "cos": (lambda x: math.cos(x)),
      "tan": (lambda x: math.tan(x)),
      "ln": (lambda x: math.log(x)),
      "log": (lambda x: math.log10(x)),
      "!": (lambda x: math.factorial(x)),
      "pi": (math.pi),
      "e": (math.e),
      "+": (lambda x,y: x+y), 
      "-": (lambda x,y: x-y), 
      "x": (lambda x,y: x*y),
      "/": (lambda x,y: x/y)}

# verifica se s é um número
# in: string
# out: boolean
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# verifica se o input é válido
# in: string
# out: boolean
def isvalid(s):
    if ('.' in s) or ('/' in s) or ('*' in s) or ('+' in s) or ('-' in s):
        if is_number(s):
            return True
        else:
            return False
    else:
        return False
    

# converte uma string em int ou float
# in: string
# out1: int
# out2: float
def tonum(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


# executa operacao
# in: string[]
def executa_operacao(*optodo):
  nargumentos = len(optodo)
  if nargumentos == 1:
      if(optodo[0].startswith("+") or optodo[0].startswith("-")):
        return tonum(optodo[0])
      else:
        return ops[optodo[0]] 
  elif nargumentos == 2:
      return ops[optodo[0]] (tonum(optodo[1]))
  else:
      return ops[optodo[1]] (tonum(optodo[0]), tonum(optodo[2]))

def main():
    if( len(sys.argv)-1 > 0):
        print("sintaxe inválida!")
        exit(0)

    while True:
        userinput = []
        nargumentos  = 0
        result = 0.0
        userinput = input(">>> ").split()
        nargumentos = len(userinput)

        if nargumentos < 1:
            print ("Número de argumentos inválidos.")
            print ("? ou help para mais ajuda")
        elif userinput[0] in("q", "Q"):
            break
        elif nargumentos == 1:
            if userinput[0] in("?", "help", "HELP"):
                print ("\nBem vindo à ajuda da CALCULADORA PYTHON")
                
                ### IMPLEMENTAR !!!! HELP PARA APENAS 1 operacao!!!!!
                
                print (*msghelpstrs)
            elif userinput[0] in("pi", "e"):
                print(executa_operacao(userinput[0]))
            elif isvalid(userinput[0]):
                print(executa_operacao(userinput[0]))
            else : print (msgsintaxinval)
        elif nargumentos == 2:
            if userinput[0] in("sqrt", "sin", "cos", "tan", "ln", "!",  
                                "log", "x2", "x3", "xy") and is_number(userinput[1]):
                    if (userinput[0] == "sqrt" and tonum(userinput[1]) < 0) or (userinput[0] == "log" and tonum(userinput[1]) == 0) or (userinput[1] == "ln" and tonum(userinput[1] < 0)):
                        print("Operação inválida!")
                    elif (userinput[0] == "log" and tonum(userinput[1]) < 0) or (userinput[0] == "ln" and tonum(userinput[1]) == 0):
                        print("-∞")
                    else:
                        print(executa_operacao(userinput[0],  userinput[1])) 
            else : print (msgsintaxinval)
        elif nargumentos == 3:
            if userinput[1] in("+", "-" , "x", "/") and is_number(userinput[0]) and is_number(userinput[2]):
                if userinput[1] == "/" and tonum(userinput[2]) == 0:
                    print("Divisor não pode ser zero!")
                else:
                    print(executa_operacao(userinput[0],  userinput[1], userinput[2]))
            else : print (msgsintaxinval)
        else : print (msgsintaxinval)


if __name__== "__main__":
    main()
