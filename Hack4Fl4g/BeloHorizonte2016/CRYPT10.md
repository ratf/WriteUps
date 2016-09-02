# CRYPT 10

**O problema**

Descobrimos essa string. Ela parece bastante familiar, mas algo está invertido. Você consegue descobrir o que é?
```
q3j5ChrVideWig1HAxmGzSOHy2LSihf1zsb0AxjHCIbKB2nLigrLignYAwfUW6DHlI4UigrLC2vJE3iZDJnYCZnFyMfZzty0FqO=
```


**Resolução**

O problema diz que tem algo invertido, então ataquei a única coisa que consegui ver que poderia inverter: o case das letras.

Com o código com o abaixo, você coloca o hash no lugar de Mr. Ed e ja joga a saída no base64 - d

```
name = 'Mr.Ed'
name_list = []

for i in name:
    if i.isupper():
        name_list.append(i.lower())
    elif i.islower():
        name_list.append(i.upper())
    else:
        name_list.append(i)

print ''.join(name_list)
```
```
python invertString.py | base64 - d
```

E você encontra a saída:

```
Crypto 10 mais f�!cil que tirar doce de criança... desec{r3v3rs3_base64}
```
