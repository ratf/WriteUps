# WEB30

A primeira coisa que se faz numa flag web é abrir o código fonte, e abaixo tem o que encontramos no código da página

```
<html>
    <head>
        <title>403 Forbidden</title>
    </head>
    <body>
        <h1>Forbidden</h1>
        <p>You don't have permission to access / on the server.</p>
        <hr>
        <address>Apache/2.4 (Cent OS) Server at 127.0.0.1 Port 80</address>
    </body>
</html>
<!--
arquivo.php?dsTitulo=f.ext&arquivo=base
-->
```

De cara já da pra ver o código comentado, então a gente ia pra ele e chamava a URL
http://192.168.0.200/arquivo.php?dsTitulo=f.ext&arquivo=base

Essa requisição retornava um base64 gigante, que descriptografando e jogando em um arquivo você descobria que era uma [imagem.](https://postimg.org/image/l2283uwzx/)

Nessa parte não teve muito jeito, foi meio que guessing.Olhando o parâmetro `arquivo` ele vem com o texto `base` e ai pq não colocar a "base" dos parâmetros?

http://192.168.0.200/arquivo.php?dsTitulo=f.ext&arquivo=`arquivo.php`

Isso trazia o código PHP da página, mas que esqueci de salvar **=P**. Dentro desse código PHP você encontrava outro nome de arquivo estranho que jogando na URL anterior trazia a flag...que também esqueci de salvar.