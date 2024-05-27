# Sistema Bancário Simples

Este é um programa Python que simula as operações básicas de um sistema bancário, incluindo depósito, saque, exibição de extrato, cadastro de novo usuário, criação de nova conta e listagem de contas.

## Funcionalidades

1. **Depósito (`d`)**:
   - Solicita ao usuário o valor do depósito.
   - Realiza o depósito na conta.
   - Atualiza o extrato da conta.

2. **Saque (`s`)**:
   - Solicita ao usuário o valor do saque.
   - Verifica se o saldo é suficiente.
   - Verifica se o valor do saque excede o limite diário ou o limite de saques.
   - Realiza o saque na conta, se todas as condições forem atendidas.
   - Atualiza o extrato da conta.

3. **Extrato (`e`)**:
   - Exibe o extrato da conta, incluindo todas as transações realizadas.

4. **Cadastrar Novo Usuário (`u`)**:
   - Permite ao usuário cadastrar-se no sistema fornecendo informações como nome, CPF, data de nascimento e endereço.

5. **Criar Nova Conta (`c`)**:
   - Cria uma nova conta bancária associada a um usuário existente, fornecendo o número da agência e o número da conta.

6. **Lista de Contas (`l`)**:
   - Lista todas as contas criadas, exibindo informações como agência, número da conta e nome do titular.

7. **Sair (`q`)**:
   - Encerra a execução do programa.

## Estrutura do Código

### Classes Principais

- **Transacao (Abstract Base Class)**: Classe base para todas as transações (Depósito e Saque).
- **Deposito**: Classe para representar a operação de depósito.
- **Saque**: Classe para representar a operação de saque.
- **Historico**: Classe para registrar o histórico de transações de uma conta.
- **Conta**: Classe base para representar uma conta bancária.
- **ContaCorrente**: Subclasse de `Conta` que adiciona limites para saques.
- **Cliente (Abstract Base Class)**: Classe base para representar um cliente.
- **PessoaFisica**: Subclasse de `Cliente` para representar uma pessoa física.

### Funções Principais

- **menu**: Exibe o menu principal e captura a opção escolhida pelo usuário.
- **exibir_extrato**: Exibe o extrato da conta do usuário.
- **criar_usuario**: Permite o cadastro de um novo usuário.
- **filtrar_usuarios**: Filtra e retorna um usuário pelo CPF.
- **criar_conta**: Permite a criação de uma nova conta para um usuário existente.
- **lista_contas**: Exibe a lista de todas as contas criadas no sistema.
- **selecionar_conta**: Permite que o usuário selecione uma conta entre as contas associadas ao seu CPF.
- **main**: Função principal que controla o fluxo do programa.


## Instruções de Uso

- Ao iniciar o programa, o usuário é apresentado a um menu com as opções disponíveis.
- O usuário pode selecionar uma das opções digitando o caractere correspondente.
- Dependendo da opção selecionada, o programa solicitará informações adicionais, como valores para depósito/saque ou dados pessoais para cadastro de usuário.
- O programa executa a operação selecionada e retorna ao menu principal, onde o usuário pode escolher outra operação ou sair do programa.
