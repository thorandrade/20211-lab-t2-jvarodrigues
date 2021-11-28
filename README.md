# http-tupi: HTTP/DEC

## João Victor Andrade Rodrigues

 [HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview) é um protocolo que permite a obtenção de recursos na web. É um protocolo extensível com uso do  cabeçalho ( _headers_) para inclusão de novos campos e valores.  A especificação das mensagens HTTP e extensões estão definidas na [RFC 7230](https://datatracker.ietf.org/doc/html/rfc7230). Nesta RFC são definidos os conceitos de proxy, gateway e túneis HTTP como agentes intermediários capazes de interpretar campos de mensagens de cliente e servidor e em alguns casos traduzir para outros formatos não padronizados pelo HTTP ou redirecionar para servidores internos. Atualmente existe um [grupo de trabalho na Internet](https://httpwg.org/specs/) pesquisando novas extensões para o HTTP. 
 
__Proponha__ uma nova aplicação para resolver um problema específico de um usuário na web. Defina uma nova extensão para o HTTP denominada HTTP Tupi com a inclusão de novos campos de cabeçalho. __Implemente o cliente e servidor HTTP Tupi__, para sua solução proposta. O servidor HTTP Tupi deve ser capaz de reconhecer uma mensagem HTTP Tupi e realizar ações, incluindo a reposta com conteúdo diferente do HTTP/1.1. As respostas podem incluir dados em outros formatos diferentes do HTML, como XML e JSON, por exemplo, de acordo com a especificação de sua proposta.

Se seu servidor receber mensagens sem a extensão do campo proposto, o servidor deve agir de acordo com o protocolo HTTP/1.1. Se a mensagem originada do cliente incluir a extensão no cabeçalho, o servidor deve responder de acodo comm protocolo HTTP Tupi.

## Qual o problema considerado?  
> O problema considerado foi uma página de boas vindas para cada um dos supostos cursos do Departamento de Engenharia Civil.

## Qual o público alvo?  
> Alunos do DEC procurando a página de boas vindas do seu curso.

## Qual a arquitetura?  
> Ele contém três módulos: servidor, cliente geral e cliente do DEC.

## Qual o formato do protocolo?
> Extende em igual o HTTP/1.1, só sendo extendido o campo curso.

### Como as mensagens são definidas?
> O cliente envia o cabeçalho HTTP/1.1 ou HTTP/DEC como uma string única. O servidor então responde com um cabeçalho resumido e então os arquivos html. 

### Quais os campos definidos?
> CURSO: VALORES

### Quais os possíveis valores de cada campo?
> ARQ e ENC

## Como a aplicação pode ser testada no Core?

_Descreva como o servidor pode ser implantado e testado, apresentando um manual de uso_ 
> sua resposta

## Faça um registro do funcionamento de sua aplicação 
_Apresente um exemplo de teste mostrando que o cliente e o servior  HTTP Tupi funcionou corretamente
> sua resposta
