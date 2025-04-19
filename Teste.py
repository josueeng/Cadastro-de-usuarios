import re

# Define uma classe `User` para representar um usuário com os atributos: nome, email e idade.
class User:
    def __init__(self, name, email, age):
        # Inicializa o nome, email e idade do usuário.
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        # Define uma representação em string para o objeto usuário.
        return f"Nome: {self.name}, Email: {self.email}, Idade: {self.age}"

# Define uma classe `UserManager` para gerenciar uma coleção de usuários.
class UserManager:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os usuários.
        self.users = []

    def add_user(self, name, email, age):
        # Verifica se o email é válido.
        if not self.is_valid_email(email):
            print("Email inválido. Tente novamente.")
            return

        # Cria um novo objeto usuário e o adiciona à lista de usuários.
        user = User(name, email, age)
        self.users.append(user)
        # Exibe uma mensagem de sucesso.
        print("Usuário adicionado com sucesso!")

    def is_valid_email(self, email):
        # Usa uma expressão regular para validar o formato do email.
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def list_users(self):
        # Verifica se a lista de usuários está vazia.
        if not self.users:
            # Exibe uma mensagem caso nenhum usuário seja encontrado.
            print("Nenhum usuário encontrado.")
        else:
            # Itera sobre a lista de usuários e exibe cada um.
            for user in self.users:
                print(user)

    def find_user(self, name):
        # Procura um usuário pelo nome na lista de usuários.
        for user in self.users:
            if user.name == name:
                # Exibe o usuário encontrado.
                print(user)
                return
        # Exibe uma mensagem caso o usuário não seja encontrado.
        print("Usuário não encontrado.")

    def delete_user(self, name):
        # Procura e remove um usuário pelo nome.
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                print(f"Usuário '{name}' removido com sucesso!")
                return
        # Exibe uma mensagem caso o usuário não seja encontrado.
        print("Usuário não encontrado.")

# Função principal que gerencia o menu e as interações do programa.
def main():
    # Cria uma instância de `UserManager`.
    user_manager = UserManager()

    while True:
        # Exibe o menu de opções.
        print("\n1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Buscar Usuário")
        print("4. Excluir Usuário")
        print("5. Sair")

        # Solicita ao usuário que escolha uma opção.
        choice = input("Digite sua escolha: ")

        if choice == '1':
            # Solicita os dados do usuário e adiciona à lista.
            name = input("Digite o nome: ")
            email = input("Digite o email: ")
            age = input("Digite a idade: ")
            user_manager.add_user(name, email, age)
        elif choice == '2':
            # Lista todos os usuários.
            user_manager.list_users()
        elif choice == '3':
            # Solicita o nome do usuário a ser buscado.
            name = input("Digite o nome para buscar: ")
            user_manager.find_user(name)
        elif choice == '4':
            # Solicita o nome do usuário a ser excluído.
            name = input("Digite o nome para excluir: ")
            user_manager.delete_user(name)
        elif choice == '5':
            # Encerra o programa.
            break
        else:
            # Exibe uma mensagem para escolhas inválidas.
            print("Escolha inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente.
if __name__ == "__main__":
    main()
