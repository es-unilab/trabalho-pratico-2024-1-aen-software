# Casos de Uso

**Gerenciar Professor**

**Ator:** Administrador do Sistema;

**Pré-condições:** O administrador deve estar autenticado e autorizado a acessar o sistema.

**Fluxo Principal:**
1. Iniciar Sessão;
2. Acessar Gestão de Professores;
3. Cadastrar Novo Professor (Nome,Email,SIAPE,Regime de trabalho);
4. Editar Dados do Professor;
5. Excluir Professor;
6. Gerar Relatório de Professores;

**Fluxo Alternativo:**
**Edição de Dados**

4a.Dados Inválidos: Se os dados atualizados não forem válidos, o sistema exibe uma mensagem de erro e solicita correção.

**Requisitos Especiais:**
**Segurança**

1a.O sistema deve garantir que apenas administradores autenticados e autorizados possam acessar e realizar operações de gerenciamento de professores.

**Persistência** 

As informações dos professores devem ser armazenadas de forma segura e persistente no banco de dados.

**Cadastrar Atividade**  
**Ator:** Professor(Usuário)  
**Fluxo Normal:**
1. Autenticar professor;
2. Professor informa a catogoria de atividade;  
3. Professor informa a subcategoria;   
4. Professor informa o tipo de ativiade e descrição da atividade;  
5. Professor informa carga horária da atividade;  
6. Sistema efetua o cadastro da atividade.  


**Excepções:**  
3a. Se a subcategoria não tiver tipo de atividade associada, não solicitar tipo de atividade;  
5a. Se a carga horária não estiver nos limites do tipo de atividade referido, solicitar novamente carga horária;  
5b. Se o somatório das cargas horárias da subcategoria não estiver nos limites da referida subcategoria, solicitar novamente a carga horária;
5c. Se o somatório das cargas horárias da categoria não estiver nos limites da referida categoria, solicitar novamente a carga horária;



**Remover Atividade**  
**Ator:** Professor(Usuário)  
**Fluxo Normal:**

**fluxo normal**
1. Autenticar professor;
2. O professor navega até a lista de atividades
3. O professor seleciona a atividade que deseja remover
4. O sistema solicita a confirmação da remoção da atividade.
5. O professor confirma a remoção.
6. O sistema remove a atividade e exibe uma mensagem confirmando a remoção da atividade.

**Excepções:**

1a. Se o professor inserir credenciais inválidas, o sistema exibe uma mensagem de erro;

2a. Se o professor não encontrar a atividade, o sistema exibe uma mensagem informando que a atividade não foi encontrada;

4a. Se o professor optar por não confirmar a remoção da atividade, o sistema cancela a operação;

5a. Se o professor confirmar a remoção da atividade, o sistema remove a atividade;