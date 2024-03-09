def pert_fibonacci(num):
    a, b = 0, 1

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False

# Número a ser verificado na sequência de Fibonacci
num_verificado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if pert_fibonacci(num_verificado):
    print(f"{num_verificado} pertence à sequência de Fibonacci.")
else:
    print(f"{num_verificado} não pertence à sequência de Fibonacci.")