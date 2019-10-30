# Importar biblioteca 'sys' e 'math'
import sys
import math

msgsintaxinval = "Sintaxe Inválida!"
msginvhelpkey = "Entrada não encontrada no Help!"

# dicionario de help
helps = dict({"? +": "[+] : para somar dois números; sintaxe: <numero 1> + <numero 2>", 
              "? -": "[-] : para subtrair dois números; sintaxe: <numero 1> + <numero 2>",
              "? x": "[x] : para multiplicar dois números; sintaxe: <numero 1> + <numero 2>",
              "? /": "[/] : para dividir dois números; sintaxe: <numero 1> + <numero 2>",
              "? sqrt": "[sqrt] : para calcular a raiz quadrada de um número; sintaxe: sqrt <numero>", 
              "? sin": "[sin] : para calcular o seno de um angulo em graus; sintaxe: sin <angulo>",
              "? cos": "[cos] : para calcular o coseno de um angulo em graus; sintaxe: cos <angulo>",  
              "? tan": "[tan] : para calcular a tangente de um angulo em graus; sintaxe: tan <angulo>",  
              "? ln": "[ln] : para calcular o logaritmo natural, de base e, de um número; sintaxe: ln <numero>",  
              "? log": "[log] : para calcular o logaritmo de base 10 de um número; sintaxe: log <numero>",
              "? !": "[!] : para calcular o fatorial de um número; sintaxe: ! <numero>",   
              "? pi": "[pi] : retorna a constante pi; sintaxe: pi",  
              "? e": "[e] : retorna a constante e; sintaxe: e",
              "? q": "[q] : para sair"})


def print_all_help_msgs():
    for keys, values in helps.items():
        print(values)

result = 0.0

# dicionario de operações
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
    if ('.' in s) or ('/' in s) or ('x' in s) or ('+' in s) or ('-' in s):
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
        return ops["+"] (tonum(result), tonum(optodo[0]))
      elif optodo[0].startswith("/"):
        return ops["/"] (tonum(result), tonum(optodo[0].replace("/","")))
      elif optodo[0].startswith("x"):
        return ops["x"] (tonum(result), tonum(optodo[0].replace("x","")))
      else:
        return optodo[0]
  elif nargumentos == 2:
      return ops[optodo[0]] (tonum(optodo[1]))
  else:
      return ops[optodo[1]] (tonum(optodo[0]), tonum(optodo[2]))

# funcao main
def main():
    if( len(sys.argv)-1 > 0):
        print("sintaxe inválida!")
        exit(0)

    while True:
        global result
        showresult = False
        userinput = []
        nargumentos  = 0
        userinput = input(">>> ").split()
        nargumentos = len(userinput)

        if nargumentos < 1:
            print ("Número de argumentos inválidos.")
            print ("? para mais ajuda")
        elif userinput[0] in("q", "Q"):
            break
        elif userinput[0] in("C", "c"):
            result = 0
            showresult = True
        elif nargumentos == 1:
            if userinput[0] == "?":
                print ("\nBem vindo à ajuda da CALCULADORA PYTHON\n")
                print_all_help_msgs()
            elif userinput[0] in("pi", "e"):
                result = executa_operacao(userinput[0])
                showresult = True
            elif isvalid(userinput[0]):
                result = executa_operacao(userinput[0])
                showresult = True
            elif is_number(userinput[0]):
                result = tonum(userinput[0])
                showresult = True
            else : print (msgsintaxinval)
        elif nargumentos == 2:
            if userinput[0].startswith("?"):
                keyhelp = userinput[0] + " " + userinput[1]
                if keyhelp in helps:
                    print(helps[keyhelp])
                else: 
                    print (msginvhelpkey)
            elif userinput[0] in("sqrt", "sin", "cos", "tan", "ln", "!",  
                                "log", "x2", "x3", "xy") and is_number(userinput[1]):
                    if (userinput[0] == "sqrt" and tonum(userinput[1]) < 0) or (userinput[0] == "log" and tonum(userinput[1]) == 0) or (userinput[0] == "ln" and tonum(userinput[1]) < 0):
                        print("Operação inválida / não definida!")
                    elif (userinput[0] == "log" and tonum(userinput[1]) < 0) or (userinput[0] == "ln" and tonum(userinput[1]) == 0):
                        result = "-∞"
                        showresult = True
                    else:
                        result = executa_operacao(userinput[0],  userinput[1])
                        showresult = True
            else : print (msgsintaxinval)
        elif nargumentos == 3:
            if userinput[1] in("+", "-" , "x", "/") and is_number(userinput[0]) and is_number(userinput[2]):
                if userinput[1] == "/" and tonum(userinput[2]) == 0:
                    print("Divisor não pode ser zero!")
                else:
                    result = executa_operacao(userinput[0],  userinput[1], userinput[2])
                    showresult = True
            else : print (msgsintaxinval)
        else : print (msgsintaxinval)
        if(showresult):
            print("= {}".format(result))


if __name__== "__main__":
    main()
