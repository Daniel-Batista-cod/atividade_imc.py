nome_do_paciente = input ("digite o nome")
peso = float(input("digite o peso"))
altura =float(input("digite a altura"))

imc = peso  /(altura**2)

if imc<18.5:
    print(f"{nome_do_paciente},abaixo do peso")
elif imc <24.9:
    print(f"{nome_do_paciente},peso normal")
elif imc <29.9:
    print(f"{nome_do_paciente},sobrepeso")
elif imc <34.9:
    print(f"{nome_do_paciente},obesidade grau I")
elif imc <39.9:
    print(f"{nome_do_paciente},obesidade grau II")
elif imc >40.0:
    print(f"{nome_do_paciente},obesidade grau III")

