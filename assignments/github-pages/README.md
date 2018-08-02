- Crie um repositório com o nome `nome-do-usuario.github.io`:

- No terminal, baixe o repositório em sua máquina (i.e. clone):

```
git clone https://github.com/nome-do-usuario/nome-do-usuario.github.io
```

- Acesse o projeto. Nele você poderá criar arquivos que estarão disponíveis em `nome-do-usuario.github.io`:

```
cd nome-do-usuario.github.io
echo "Hello World" > index.html
```

- Para enviar as alterações feitas no diretório, "de push" ou seja, execute o seguinte:

```
git add --all
git commit -m "Initial commit"
git push -u origin master
```
- Você pode também enviar arquivos na interface web do GitHub.

- Caso tenha alterado em outro computador (ou na interface web do git) e queira obter as modificações em seu computador, execute:

```
git pull origin master
```
