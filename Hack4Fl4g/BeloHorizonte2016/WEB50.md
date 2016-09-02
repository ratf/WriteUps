# WEB 50

**O Problema**

Marque 1337 pontos para conseguir a flag... talvez seja melhor "hackear" a aplicação..


A página apresentava um texto com o nome do jogador informando que ele deveria chega à 1337 pontos. Nessa página era apresentada uam
soma e a ideia era ir acertanod a soma até juntar os 1337 pontos

**A Resolução**

O próprio enunciado já sugeria de "hackear" a página. A primeira idéia  já foi criar um script que automatizasse a tarefa, portanto a primeira coisa era conferir os dados utilizados pela página e nessa parte já se encontrava um *cookie* que era preciso enviar nas requisições. Houve, depois, gente dizendo que havia a soma já em algum *cookie*, o que facilitaria um script ao invés do script ter de extrair e calcular a soma par air para a proxima página.

Abaixo segue o código escrito:

```
var fun = new function() {
    var a = document.getElementsByTagName('p')[0].textContent.split('+');
    var r = parseInt(a[0]) + parseInt(a[1]);
    document.getElementsByTagName('input')[0].value = r;
    document.getElementsByTagName('form')[0].submit();
}();

Author: Marcio Motta
```
Com esse código foi possível rodar de modo "semi-automático" um parsing da página e no fim chegar na flag.

Infelizmente não há um registro da flag. =( mas isso ai trazia ela com certeza!
