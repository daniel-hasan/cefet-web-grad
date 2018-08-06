# Significado de cada comando

- `git status`: verifica o estado dos arquivos em seu repositório local
- `git add -A`: adiciona os arquivos em seu repositório local
- `git commit -m "mensagem"`: faz commit de seus arquivos para o repositório local
- `git push origin nome-da-branch`: envia os arquivos para o respositório remoto na branch chamada `nome-da-branch`
- `git pull origin nome-da-branch`: obtém os arquivos do repositório remoto
- `git branch`: exibe as branches existentes e mostra em qual branch você está atualmente trabalhando
- `git branch nome-da-branch`: cria uma nova branch
- `git checkout nome-da-branch`: vai para uma determinada branch


# Comandos mais frequentes


- Baixar um repositório na sua máquina:

```
git clone https://github.com/usuario/nome-do-repositorio.git
```



- Enviar as alterações:

```
git add --all
git commit -m "Initial commit"
git push -u origin gh-pages
```

- Você pode também enviar arquivos na interface web do GitHub.
- `gh-pages` é o branch que o GitHub usa para que você possa acessar esses arquivos por meio do GitHub pages. Ou seja, caso tenha um `index.html`, você poderá acessar a página web desenvolvida por meio da URL: https://nome-do-usuario.github.io/nome-do-respositorio 


- Caso tenha alterado em outro computador (ou na interface web do git) e queira obter as modificações em seu computador, execute:

```
git pull origin gh-pages
```
