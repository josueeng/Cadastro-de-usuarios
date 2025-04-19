# User Management API

Este projeto é uma API simples para gerenciar usuários, permitindo adicionar, listar, buscar e excluir usuários. A API foi desenvolvida em Python e utiliza expressões regulares para validação de e-mails.

## Funcionalidades

- **Adicionar Usuário**: Adiciona um novo usuário com nome, e-mail e idade.
- **Listar Usuários**: Exibe todos os usuários cadastrados.
- **Buscar Usuário**: Busca um usuário pelo nome.
- **Excluir Usuário**: Remove um usuário pelo nome.

## Estrutura do Código

### Classe `User`
Representa um usuário com os seguintes atributos:
- `name`: Nome do usuário.
- `email`: E-mail do usuário.
- `age`: Idade do usuário.

### Classe `UserManager`
Gerencia a coleção de usuários e fornece métodos para:
- Adicionar usuários (`add_user`)
- Listar usuários (`list_users`)
- Buscar usuários (`find_user`)
- Excluir usuários (`delete_user`)
- Validar e-mails (`is_valid_email`)

### Função Principal
A função `main` exibe um menu interativo para o gerenciamento de usuários.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código em um arquivo, por exemplo, `user_management.py`.
3. Execute o script no terminal:
    ```bash
    python user_management.py
    ```

4. Siga as instruções exibidas no menu.

## Exemplo de Uso

### Adicionar Usuário
```plaintext
Digite sua escolha: 1
Digite o nome: João
Digite o email: joao@example.com
Digite a idade: 25
Usuário adicionado com sucesso!
```

### Listar Usuários
```plaintext
Digite sua escolha: 2
Nome: João, Email: joao@example.com, Idade: 25
```

### Buscar Usuário
```plaintext
Digite sua escolha: 3
Digite o nome para buscar: João
Nome: João, Email: joao@example.com, Idade: 25
```

### Excluir Usuário
```plaintext
Digite sua escolha: 4
Digite o nome para excluir: João
Usuário 'João' removido com sucesso!
```

## Requisitos

- Python 3.x

## Autor

Este projeto foi desenvolvido como um exemplo de gerenciamento de usuários em Python.
