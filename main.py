n1, n2, n3, n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n1 = float(n1 * 2)
n2 = float(n2 * 3)
n3 = float(n3 * 4)
n4 = float(n4 * 1)
media = float ((n1 + n2 + n3 + n4) / 10)
print("Media: %.1f"%(media))
if media >= 7:
    print("Aluno aprovado.")
else:
    if media < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        c = float(input())
        print("Nota do exame: %.1f"%(c))
        media = float((media + c) / 2)
        if media >= 5:
            print("Aluno aprovado.")
            print("Media final: %.1f"%(media))
        else:
            print("Aluno reprovado.")
            print("Media final: %.1f"%(media))