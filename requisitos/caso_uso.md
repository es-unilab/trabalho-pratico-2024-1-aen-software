# Casos de Uso

**Cadastrar Professor**
**Ator:** Administrador
**Cadastro no Sistema**

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