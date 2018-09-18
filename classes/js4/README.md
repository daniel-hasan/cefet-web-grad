<!-- {"layout": "title"} -->
# Javascript (parte 4)
## Web Storage, AJAX, JSON e Star Wars :stars:

---
# Roteiro

1. _Web Storage_
1. AJAX
1. JSON
1. jQuery

<!--
# Exercícios

- Há três exercícios a serem feitos e entregues nesta aula
  1. Dois sobre armazenamento
  1. Um sobre AJAX
- Eles serão descritos ao longo dos slides de conteúdo
- Você deve entregá-los como um código do jsfiddle ou do codepen.io e colocar
  o link no Moodle
 -->
---
<!-- {"layout": "section-header", "slideHash": "usando-o-web-storage"} -->
 # Usando o <br>**Web Storage**
 ## Salvando dados na página

 - Por que e o que salvar?
 - O Web Storage
   - `localStorage`
   - `sessionStorage`

 <!-- {ul^1:.content} -->

---
 <!-- {"layout": "regular"} -->
# Por que e o que salvar?

 - As nossas páginas podem querer salvar várias coisas:
   1. Exemplo: Moodle
      - **Motivo**: manter preferências do usuário sobre a interface
      - **O que salvar?** o que está aberto/fechado, a língua etc
   1. Exemplo: Slides da aula
      - **Motivo**: mostrar o "tutorial" apenas 3x
      - **O que salvar?** quantas vezes já mostrou o tutorial
   1. Exemplo: Trello
      - **Motivo**: guardar um "rascunho" que ainda não foi salvo
      - **O que salvar?** o conteúdo digitado pelo usuário

---
 <!-- {"fullPageElement": "#moodle-video", "playMediaOnActivation": {"selector": "#moodle-video" }} -->

 <video src="//fegemo.github.io/cefet-front-end-large-assets/videos/local-storage-moodle.webm" controls id="moodle-video"></video>

---
 <!-- {"fullPageElement": "#trello-video", "playMediaOnActivation": {"selector": "#trello-video" }} -->

 <video src="//fegemo.github.io/cefet-front-end-large-assets/videos/local-storage-trello.webm" controls id="trello-video"></video>

---
<!-- {"layout": "regular"} -->
## O Web Storage

 - O Web Storage permite páginas **armazenarem de dados <u>
   no navegador</u>**
   - _storage_ === armazenamento
 - Existem dois sabores:
   1. `localStorage`, salva os dados <u>"para sempre"</u>
   1. `sessionStorage`, salva <u>apenas "durante a sessão"</u>
 - Os dados são salvos **apenas no próprio navegador** <!-- {li^0:.nota} -->
   - Isto é, se você abrir a página em <u>outro</u> navegador ou computador,
     ainda não existem dados salvos

---
<!-- {"layout": "regular", "slideHash": "local-storage"} -->
## `localStorage` e `sessionStorage`

 - Ambos nos permitem **armazenar valores dentro de _Strings_** <!-- {ul:.bulleted} -->
 - Cada item armazenado é composto por **uma chave (nome) e um valor**
   - Exemplo (salvando):
     ```js
     window.localStorage.setItem('personagem', 'Jake');
     window.localStorage.setItem('quest', 'Salvar a Jujuba');
     ```
     - Lembre-se: ~~`window.`~~`localStorage`
   - Exemplo (recuperando):
     ```js
     let nome = localStorage.getItem('personagem');    // retorna "Jake"
     let objetivo = localStorage.getItem('quest');     // retorna "Salvar a Jujuba"
     ```

---
<!-- {"layout": "2-column-content"} -->
## **localStorage**

 - O navegador **armazena permanentemente**, ou até que o usuário limpe: <!-- {ul.bulleted} -->
     ![right](../../images/clear-cookies.png) <!-- {img:style="max-height: 200px"} -->


---
## Exemplo de uso do **localStorage**

 - Um evento de clique em um botão que **faz o menu aparecer e desaparecer**:
   ```js
   // ...
   botaoMenuEl.addEventListener('click', function() {
     let menuEl = document.querySelector('#menu'),
       isExpandido = menuEl.classList.toggle('expandido');

     // isExpandido = true ou false
     localStorage.setItem('menu-esta-expandido', isExpandido);
   });
   ```
   - (continua no próximo slide)

---
## Exemplo de uso do **localStorage** (cont.)

 - Após a página ter sido carregada (e.g., um _script_ ao final do _body_):
   ```js
   let devoExpandirMenu = localStorage.getItem('menu-esta-expandido');

   if (devoExpandirMenu === 'true') {        // lembre-se: tudo é salvo como String
     let menuEl = document.querySelector('#menu');
     menuEl.classList.add('expandido');
   }
   ```
   - Ou seja, expande o menu se o usuário o havia deixado expandido antes



---
## Interface do **localStorage**

- Salvar um item:
  ```js
  localStorage.setItem('chave', 'valor');
  ```
- Recuperar um item por chave:
  ```js
  localStorage.getItem('chave');
  ```
- Recuperar um item por índice numérico:
  ```js
  localStorage.key(numero);
  ```

---
## Interface do **localStorage** (cont.)

- Excluir uma entrada:
  ```js
  localStorage.removeItem('chave');
  ```
- Limpar todas as entradas:
  ```js
  localStorage.clear();
  ```
- Quantidade de entradas salvas:
  ```js
  localStorage.length;
  ```

---
## **sessionStorage**

- Exata mesma funcionalidade do `localStorage`, porém o navegador armazena
  as informações apenas enquanto o **usuário está "em uma sessão"**
  - Uma sessão é encerrada:
    1. Com o usuário digitando outro endereço na barra
    1. O navegador fechando
    1. O usuário navegando para outro domínio naquela mesma janela/aba
- A interface do `sessionStorage` também é a mesma daquela do `localStorage`

---
## Formato de armazenamento

- Como dito, o _web storage_ armazena apenas _Strings_
  - Mas seria útil armazenar objetos complexos. Por exemplo:
    ```js
    var jogo = { fase: 4, vidas: 5, jogador: 'Ariosvaldo' };
    localStorage.setItem('estado-do-jogo', jogo);

    console.log(localStorage.getItem('estado-do-jogo'));
    // Saída no console: "[object Object]"
    ```

---
## Armazenando objetos serializados

- Na verdade, o Javascript sabe **serializar e desserializar** objetos em
  _Strings_, usando um formato que se chama JSON
    - JSON é Javascript Object Notation
  - Salvando:
    ```js
    localStorage.setItem('estado-do-jogo', JSON.stringify(jogo));
    // Salvou: {"fase":4,"vidas":5,"jogador":"Ariosvaldo"}"
    ```
  - Recuperando:
    ```js
    var jogo = localStorage.getItem('estado-do-jogo');
    jogo = JSON.parse(jogo);
    ```

*[JSON]: JavaScript Object Notation*

---
# JSON

*[JSON]: JavaScript Object Notation*

---
## JSON

*[JSON]: JavaScript Object Notation*

- _Javascript Object Notation_ é um formato leve de troca de dados
- Pode ser usado para troca de informação entre programas escritos em
  diversas linguagens
  - Assim como o XML
- Baseado na notação literal de objetos do Javascript
- Criado pelo autor do nosso livro: [Douglas Crockford](http://tools.ietf.org/html/rfc4627)
- É codificado como texto puro
- Exemplo:
  `produto.json`
  ```json
  {
    "idProduto": 44235,
    "quantidade": 1
  }
  ```

---
## JSON

*[JSON]: JavaScript Object Notation*

- O formato possui seis tipos de valores:
  - Objetos
  - Arrays
  - `String`
  - `Number`
  - `Boolean`
  - `null` <!-- {ul:.multi-column-list-4} -->
- Um objeto JSON é como um objeto Javascript: um container não ordenado de
  propriedades
  - Uma chave é sempre uma string entre aspas duplas
    - Diferente de Javascript, que não precisa de aspas
  - Um valor pode ser qualquer um dos listados acima
- Espaço em branco ou quebras de linha não alteram a semântica

---
## **JSON** vs XML

*[JSON]: JavaScript Object Notation*
*[XML]: eXtensible Markup Language*

```json
[
  {
    "nome": "JavaScript - The Good Parts",
    "autores": ["Douglas Crockford"],
    "ano": 2005
  },
  {
    "nome": "Node.js in Action",
    "autores": ["Mike Cantelon", "Mark Harter"],
    "ano":  2014
  }
]
```
- 216 caracteres

---
<!-- {"state": "show-active-slide-and-previous"} -->
## JSON vs **XML**

*[JSON]: JavaScript Object Notation*
*[XML]: eXtensible Markup Language*

```xml
<livros>
  <livro nome="JavaScript - The Good Parts" ano="2005">
    <autores>
      <autor>Douglas Crockford</autor>
    </autores>
  </livro>
  <livro nome="Node.js in Action" ano="2014">
    <autores>
      <autor>Mike Cantelon</autor>
      <autor>Mark Harter</autor>
    </autores>
  </livro>
</livros>
```
- 319 caracteres (48% maior)

---
## JSON no navegador

- O objeto `window` possui o objeto `JSON` que contém métodos de conversão
  do formato JSON entre _string_ e objetos Javascript
  - De Javascript para _string_ (serialização)
    ```js
    JSON.stringify({ nome: 'Flavio', sobrenome: 'Coutinho' });
    // "{"nome":"Flavio","sobrenome":"Coutinho"}"
    ```
  - De _string_ para Javascript (desserialização)
    ```js
    var banco = JSON.parse('{"nome":"Itaú","codigo":"341"}');
    console.log(banco.nome);    // Itaú
    ```

<!--
# Exercício 1

1. Crie um formulário referente ao cadastro de uma pessoa com os seguintes
   dados: id, nome, telefone. Os dados deverão ser cadastrados utilizando o
   **`localStorage`** para persistir, quando um botão **salvar** for pressionado
   - Os dados deverão ser armazenados em objetos no formato JSON
2. Crie um botão **"carregar"** que possibilite a recuperação dos dados
   cadastrados e os mostre em uma DIV ou nos próprios campos do formulário
   criado
- [Código seminal](https://jsfiddle.net/fegemo/uj42ynbv/1/) no JSFiddle
 -->
---
<!-- {"layout": "regular"} -->
## A biblioteca jQuery

- ![](../../images/jquery-logo.png) <!-- {.push-right} -->
  Criada em 2006 por John Resig
  - Pronuncia-se djeiquéuri
- Objetivos:
  1. Resolver **incompatibilidade entre navegadores**
  1. Aumentar **expressividade do código**
  1. **Simplificar interfaces** complexas
  1. Implementar **funções corriqueiras**
- Chegou a ser **usada** por quase **<u>75% de toda a Web</u>**

---
<!-- {"slideHash": "incluindo-a-biblioteca-jquery"} -->
## Incluindo a biblioteca jQuery

- Em uma página, você deve incluir o arquivo `jquery.js`. Há 2 formas:
  1. Baixando o arquivo `jquery.js` e colocando-o com o seu projeto:
     ```html
       <script src="js/jquery.js"></script>
       <script src="js/meu-proprio-codigo.js"></script>
     </body>
     </html>
     ```
  1. Usando o `jquery.js` hospedado em uma CDN (_i.e._, na nuvem)
     - CDN é uma rede de computadores para hospedar arquivos para sites
       ```html
         <script src="http://algumacdn.com.br/jquery.js"></script>
         <script src="js/meu-proprio-codigo.js"></script>
       </body>
       </html>
       ```

*[CDN]: Content Delivery Network*

---
## Objeto/função exposta por `jquery.js`

- O `jquery.js` disponibiliza apenas 1 objeto/função, que possui
  toda a funcionalidade da biblioteca:
  ```js
  window.jQuery = $ = function(seletor) {
    // ... zilhão de funções úteis aqui
  }
  ```
  - Repare que `$` é um nome válido para uma variável em JavaScript, e é
    exatamente a variável que expõe a "função jQuery"
  - A função `$` (jQuery) recebe uma **string com um seletor CSS**, igual a
    `document.querySelectorAll`

---
<!-- {"slideHash": "jquery-funcionamento-basico"} -->
## Funcionamento básico e seletores (1/3)

- Com jQuery, praticamente tudo é feito **em 2 passos**:
  1. **Seleciona-se** um ou mais elementos
  1. **Executa-se** alguma lógica com eles
- Exemplo: alterando o conteúdo HTML de um elemento usando jQuery e
  em "vanilla JavaScript":
- <!-- {li:.code-split-2} -->
  ```js
  // Usando jQuery
  $('#pokemon').html('Pikachu');

  // $('#pokemon') == jQuery('#pokemon')
  ```
  ```js
  // Em "vanilla js" (js puro)
  let el = document
              .querySelector('#pokemon');
  el.innerHTML = 'Pikachu';
  ```

---
## Funcionamento básico e seletores (2/3)

- Passamos um seletor CSS para a função `$`
  - Veja a [documentação][doc-jquery-fn] da função `$` (ou função jQuery)
  - Ela retorna um **"objeto jQuery"**, que é uma coleção de elementos HTML
- Um **objeto jQuery** possui vários métodos e eles <u>atuam na coleção
  inteira</u>:
  ```js
  $('p').html('It\'s me, Maaaario!');
  // alterou o innerHTML de TODOS os parágrafos da página
  ```
  - **Experimento**: vá para a página do jQuery e execute essa linha!

[doc-jquery-fn]: https://api.jquery.com/jQuery/#jQuery-selector-context

---
## Funcionamento básico e seletores (3/3)

- Exemplo: na prática da **exploração espacial** (botões '+'/'-')
- <!-- {li:.code-split-2} -->
  ```js
  $('button').click(function(e) {
    let $p = $(e.currentTarget)
                           .closest('p');
    $p.toggleClass('expandido');
    $p.html($p.hasClass('expandido')
                            ? '-' : '+');
  });
  ```
  ```js
  let botoes = document
            .querySelectorAll('button');
  for (let bEl of botoes) {
    bEl.addEventListener('click',fnct(e){
      let pEl = e.currentTarget
                    .parentNode;
      let colocou = pEl.classList
                    .toggle('expandido');
      e.currentTarget.innerHTML = colocou
                            ? '-' : '+';
    });
  }
  ```

---
<!-- {"slideHash": "jquery-atribuindo-eventos"} -->
## Atribuindo eventos

- Usando jQuery, há atalhos para **colocar eventos** em elementos ou
  **em coleções deles (objeto jQuery)**
- <!-- {li:.code-split-2} -->
  ```js
  $('.ajuda').click(ajuda);



  ```
  ```js
  document.querySelectorAll('.ajuda')
    .forEach(function(el) {
      el.addEventListener('click', ajuda);
  });
  ```
- Outros eventos:
  ```js
  $colecao.click(callback);       // addEventListener('click', callback)
  $colecao.mousemove(callback);   // 'mousemove'
  $colecao.keyup(callback);       // 'keyup'
  $colecao.change(callback);      // 'change' (no input)
  $colecao.hover(callbackOver, callbackOut);
  ```

---
<!-- {"slideHash": "jquery-estilizando-elementos"} -->
## Estilizando elementos

- **Objetos jQuery** podem ser estilizados, como em "vanilla js", usando:
  - (a) classes:
  - <!-- {li:.code-split-2} -->
    ```js
    $('#tutorial').toggleClass('big');

    ```
    ```js
    document.querySelector('#tutorial')
          .classList.toggle('big');
    ```
  - (b) propriedades CSS diretamente:
  - <!-- {li:.code-split-2} -->
    ```js
    $('#tutorial').css('width', '50px');

    ```
    ```js
    document.querySelector('#tutorial')
          .style.width = '50px';
    ```
- Veja a descrição da [função `.css(prop, valor)`][doc-jquery-css] na
  documentação

[doc-jquery-css]: http://api.jquery.com/css/#css2

---
<!-- {"layout": "regular", "slideHash": "jquery-efeitos-visuais"} -->
## Efeitos visuais

- Algumas funções para fazer efeitos visuais:
  ```js
  $colecao.fadeIn();        // faz elementos surgirem com opacity [0, 1]
  $colecao.fadeOut();       // faz elementos desaparecerem [1, 0]
  $colecao.fadeToggle();    // alterna fadeIn()/fadeOut()

  $colecao.slideDown();     // faz elementos surgirem de cima para baixo
  $colecao.slideUp();       // faz elementos desaparecerem para cima
  $colecao.slideToggle();   // alterna slideDown()/slideUp()
  ```


<iframe width="100%" height="160" src="//jsfiddle.net/fegemo/4L525ow4/1/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

---
<!-- {"slideHash": "jquery-andando-na-arvore"} -->
## Andando na árvore

- A partir do elemento selecionado, é possível chegar até seus parentes:
- ```html
  <div class="sanfona">
    <h2>Tópico 1</h2>
    <p>Sobre o tópico 1...</p>
    <h2>Tópico 2...</h2>
    <p>Sobre o tópico 2...</p>
  </div>
  ```
  ```js
  let $topicos = $('.sanfona h2');
  $topicos.click(function(e) {
    let $topico = $(e.currentTarget);
    let $p = $topico.next(); // ← ← ←
    $p.slideToggle();
  });
  ```
  <!-- {li:.code-split-2} -->

<iframe width="100%" height="250" src="//jsfiddle.net/fegemo/4podo400/embedded/result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

---
<!-- {"layout": "regular", "slideHash": "jquery-andando-na-arvore-metodos"} -->
## Andando na árvore: métodos

- Veja [todos os métodos aqui][jquery-doc-traversing]. Alguns são:
  ```js
  $colecao.next();    // irmão seguinte de cada elemento
  $colecao.prev();    // irmão anterior...
  $colecao.parent();  // pai de cada elemento
  $colecao.find(seletor);     // filhos que atendam ao seletor
  $colecao.closest(seletor);  // ancestral mais próximo -> seletor
  ```

[jquery-doc-traversing]: http://api.jquery.com/category/traversing/

---
<!-- {"slideHash": "ajax"} -->
# AJAX

*[AJAX]: Asynchronous JavaScript and XML*
*[XML]: eXtensible Markup Language*

![Foto do personagem Deadpool enfrentando um limpador multiuso AJAX](../../images/ajax-deadpool.jpg)

---
## Problema

- Algumas vezes, queremos alterar **apenas um pedaço** de uma página Web
  - Exemplo no Facebook:
    1. Botão _like_
    1. Enviar comentário
  - Exemplo no Twitter:
    1. Carregar mais _tweets_
  - Exemplo em lojas virtuais:
    1. Adicionar um produto ao carrinho sem sair da página

---
## Problema

- Se fosse possível enviar e receber apenas um pedaço de página **em vez de
  páginas completas**, o tráfego entre navegador e servidor reduziria bastante
- De fato, os navegadores possibilitam a realização de uma requisição/resposta
  assíncrona, sem o carregamento de uma página completa
  - Essa técnica se chama AJAX
  - Surgiu no Internet Explorer, no ano 2000, por [Jesse Gareth](http://www.adaptivepath.com/ideas/ajax-new-approach-web-applications/)

---
## AJAX

*[AJAX]: Asynchronous JavaScript and XML*
*[XML]: eXtensible Markup Language*

- É a sigla para _Asynchronous JavaScript and XML_
- É uma operação realizada via Javascript no navegador
- Originalmente, usava-se Javascript para fazer uma requisição de dados ao
  servidor, que respondia no formato XML
  - Hoje em dia, responde-se com qualquer objeto reconhecido pelo navegador
- Usamos um objeto do tipo `window.XMLHttpRequest` para fazer a requisição e
  receber a resposta

---
## O **XMLHttpRequest**

- Para cada requisição, devemos instanciar um objeto `XMLHttpRequest`,
  configurá-lo e acioná-lo. Supondo um exemplo de botão "curtir":
  ```js
  var curtirRequest = new XMLHttpRequest();
  curtirRequest.onreadystatechange = callbackCurtir;
  curtirRequest.open('GET', '/curtir/3434', true);
  curtirRequest.send(null);
  ```
- Uma função (configurada em `onreadystatechange`) é invocada a cada **mudança
  de estado** do objeto (veja nos próximos 2 slides)
- [Referência](https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest) e [Tutorial](https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest/Usando_XMLHttpRequest) na MDN

---
## Estados de um XMLHttpRequest

- **`0`	UNSENT:** `open()` ainda não foi invocado
- **`1`	OPENED:**	`send()` ainda não foi invocado
- **`2`	HEADERS_RECEIVED:**	`send()` foi invocado e os cabeçalhos da resposta já estão disponíveis
- **`3`	LOADING:** fazendo _download_ da resposta
  - `responseText` tem informação parcial da resposta
- **`4`	DONE:**	Operação finalizada

---
## _Callback_ de mudança de estado

- Invocada a cada alteração de estado do objeto `XMLHttpRequest`
  ```js
  function callbackCurtir() {
    // 4: DONE
    if (this.readyState === 4) {
      if (this.status === 200) {
        alert('Post curtido!');
      } else {
        console.log('Erro ao curtir post. Código ' +
          'da resposta HTTP: ' + this.status);
      }
    }
  }
  ```

https://github.com/fegemo/cefet-web-starwars

---
## AJAX mais facinho com jQuery

- O jQuery possui uma abstração do objeto `XMLHttpRequest` para agilizar a
  realização de requisições AJAX
  - Veja como ficaria o exemplo do botão "curtir" usando jQuery:
  ```js
    $.ajax({
      url: '/curtir/3434',
      method: 'GET',      // opcional: 'GET' é o valor padrão
      success: function(resposta) {
        console.dir(resposta);  // veja a resposta no terminal
        alert('Post curtido!');
    });
	```
---
# Intro nas Estrelas

- Vamos criar um letreiro Star Wars em Javascript e CSS \o/
- Faça um _fork_ do repositório: http://github.com/daniel-hasan/cefet-web-starwars
- Você deve escrever código Javascript para fazer chamadas AJAX para
  uma API pública com informações sobre Star Wars
  - Disponível em https://swapi.co/
    <div class="resolution">Resolução: http://codepen.io/fegemo/pen/YXGxzN</div>
- O uso de jQuery está liberado neste exercício \o/

---
# Referências

1. Capítulo 12 do livro "Head First: JavaScript"
1. Apêndice E do livro "JavaScript - The Good Parts"
1. Mozilla Developer Network (MDN)
1. Página da jQuery: http://jquery.com/
1. Curso de jQuery da Codeschool: http://try.jquery.com

---
<!-- {"slideHash": "setup-local-server"} -->
## Erro ao fazer o AJAX (slide oculto :P)

- Os navegadores têm uma política de permissões diferente para quando acessamos uma
página via o protocolo file:// que proíbe o uso de requisições AJAX, dentre
outras coisas
- Para contornar a restrição, precisamos hospedar nosso arquivo em um servidor
Web e acessar a página usando o protocolo http
  1. Navegue até seu diretório com o arquivo index.html **pelo terminal**
  1. Use um servidor http simples em python
     ```
     $ python -m SimpleHTTPServer
     ```
  1. Acesse http://localhost:8000 no navegador
