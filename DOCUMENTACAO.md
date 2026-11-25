# DOCUMENTAÇÃO TÉCNICA DO PROJETO

## SISTEMA DE CONTROLE DE ENTRADA E SAÍDA DE ALUNOS

**Equipe:** Cristian Bueno · Silas Campos · Vitor Cerqueira · João Wolf
**Período de desenvolvimento:** 25/10/2026 a 25/11/2026
**Repositório:** publicado no GitHub
**Tipo de aplicação:** sistema web

---

## SUMÁRIO

1. Introdução
2. Objetivos
3. Escopo do sistema
4. Tecnologias utilizadas
5. Arquitetura da aplicação
6. Modelo de dados
7. Funcionalidades
8. Organização da equipe
9. Cronograma e marcos
10. Dificuldades encontradas
11. Resultados e conclusão

---

## 1. INTRODUÇÃO

O controle de entrada e saída de alunos em instituições de ensino é feito, em muitos casos, de forma manual: cadernos de portaria, fichas de papel ou planilhas preenchidas à mão. Esse método gera três problemas recorrentes: a dificuldade de localizar um registro antigo, a possibilidade de perda física do registro e a demora para responder a uma pergunta simples como "a que horas este aluno saiu ontem?".

Este projeto propõe a substituição desse controle manual por um sistema web, no qual cada movimentação do aluno é registrada com data e hora e fica permanentemente consultável.

## 2. OBJETIVOS

### 2.1 Objetivo geral
Desenvolver um sistema web capaz de cadastrar alunos e registrar, de forma confiável, cada entrada e cada saída da instituição.

### 2.2 Objetivos específicos
- a) Manter um cadastro único de alunos, evitando duplicidade de registros;
- b) Registrar a movimentação (entrada ou saída) com data e hora automáticas;
- c) Disponibilizar a consulta do histórico de movimentações por aluno;
- d) Garantir que os dados fiquem armazenados em banco de dados, e não em arquivos locais;
- e) Versionar todo o código em repositório Git, permitindo o trabalho simultâneo de quatro pessoas.

## 3. ESCOPO DO SISTEMA

### 3.1 O que o sistema faz
- Cadastro, consulta e edição de alunos;
- Registro de entrada e de saída;
- Listagem das movimentações do dia;
- Histórico de movimentações por aluno.

### 3.2 O que ficou fora do escopo (delimitação)
- Integração com catraca, biometria ou leitor de cartão físico;
- Envio automático de mensagem aos responsáveis;
- Controle de notas, disciplinas ou frequência pedagógica;
- Aplicativo para celular.

A delimitação acima foi uma decisão consciente da equipe: o prazo do projeto era de aproximadamente um mês, e optou-se por entregar o núcleo do sistema funcionando por completo em vez de várias funcionalidades incompletas.

## 4. TECNOLOGIAS UTILIZADAS

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Linguagem | Python | Linguagem de domínio da equipe de back-end |
| Framework web | Django | Já traz sistema de rotas, ORM e painel administrativo prontos, o que acelera o desenvolvimento |
| Banco de dados | PostgreSQL | Banco relacional robusto, adequado a registros históricos que não podem ser perdidos |
| Interface | HTML, CSS e templates do Django | Mantém o front-end integrado ao back-end, sem necessidade de uma API separada |
| Versionamento | Git / GitHub | Permite que quatro pessoas trabalhem no mesmo código sem sobrescrever o trabalho umas das outras |

## 5. ARQUITETURA DA APLICAÇÃO

O sistema segue o padrão **MVT (Model–View–Template)**, que é a organização utilizada pelo Django:

- **Model (modelo):** define as tabelas do banco de dados. É onde ficam as regras do que é um Aluno e do que é um Registro de movimentação.
- **View (visão):** contém a lógica. Recebe a requisição do navegador, consulta ou grava no banco e decide o que será exibido.
- **Template (template):** é a página HTML que o usuário vê, já preenchida com os dados enviados pela View.

### 5.1 Fluxo de uma requisição

```
Navegador  ->  URL  ->  View  ->  Model  ->  Banco de dados (PostgreSQL)
                          |
                          v
                      Template  ->  Página exibida ao usuário
```

Exemplo prático: o funcionário da portaria clica em "Registrar entrada". O navegador chama a URL correspondente; a View identifica o aluno, cria um novo registro de movimentação com a data e a hora do momento e grava no banco; em seguida, devolve o template com a lista atualizada das movimentações do dia.

## 6. MODELO DE DADOS

O sistema utiliza duas entidades principais, com relação de **um para muitos**: um aluno possui muitos registros de movimentação, e cada registro pertence a um único aluno.

### 6.1 Entidade ALUNO

| Campo | Tipo | Observação |
|---|---|---|
| id | inteiro | Chave primária, gerada automaticamente |
| nome | texto | Nome completo do aluno |
| matrícula | texto | Identificador único do aluno na instituição |
| turma | texto | Turma ou série |
| responsável | texto | Nome do responsável |
| telefone | texto | Contato do responsável |
| ativo | booleano | Indica se o aluno está matriculado |

### 6.2 Entidade REGISTRO

| Campo | Tipo | Observação |
|---|---|---|
| id | inteiro | Chave primária, gerada automaticamente |
| aluno | chave estrangeira | Referência ao aluno (entidade ALUNO) |
| tipo | texto | "entrada" ou "saída" |
| data_hora | data e hora | Preenchido automaticamente no momento do registro |
| observação | texto | Campo livre, por exemplo "saída antecipada autorizada" |

### 6.3 Diagrama da relação

```
   ALUNO  1 ----------------- N  REGISTRO
   (um aluno)              (muitas movimentações)
```

## 7. FUNCIONALIDADES

| Código | Funcionalidade | Descrição |
|---|---|---|
| F01 | Cadastrar aluno | Inclui um novo aluno na base |
| F02 | Listar alunos | Exibe todos os alunos cadastrados |
| F03 | Editar aluno | Permite corrigir dados cadastrais |
| F04 | Registrar entrada | Cria um registro do tipo "entrada" com data e hora atuais |
| F05 | Registrar saída | Cria um registro do tipo "saída" com data e hora atuais |
| F06 | Movimentações do dia | Lista todos os registros da data corrente |
| F07 | Histórico do aluno | Lista todas as movimentações de um aluno específico |

## 8. ORGANIZAÇÃO DA EQUIPE

| Integrante | Função | Responsabilidades no projeto |
|---|---|---|
| Cristian Bueno | Desenvolvedor Back-end | Modelagem do banco de dados, registro de entrada e saída, integração final, administração do repositório GitHub |
| Silas Campos | Analista | Levantamento de requisitos com a escola, testes, documentação |
| Vitor Cerqueira | Desenvolvedor Front-end | Protótipo das telas, telas de cadastro e de registro |
| João Wolf | Desenvolvedor Back-end | Cadastro de alunos, relatório de presença e histórico |

### 8.1 Método de trabalho
A equipe dividiu o projeto em quatro frentes (análise, banco de dados e back-end, front-end e testes). O controle de versão foi feito pelo GitHub, de modo que cada integrante trabalhava em sua parte e integrava o código ao repositório comum, evitando conflitos e retrabalho.

## 9. CRONOGRAMA E MARCOS

O cronograma completo, com as doze tarefas e seus responsáveis, encontra-se no arquivo `CRONOGRAMA.md` e está representado graficamente no Gráfico de Gantt do projeto.

### 9.1 Marcos de controle

| Data | Marco |
|---|---|
| 01/11 | Requisitos levantados e banco de dados modelado |
| 13/11 | Núcleo do sistema (registro de entrada e saída) funcionando |
| 22/11 | Sistema testado e estável |
| 25/11 | Entrega e apresentação |

## 10. DIFICULDADES ENCONTRADAS

- **a) Definição do escopo.** A tendência inicial foi querer incluir biometria e aviso aos responsáveis. A equipe optou por delimitar o escopo ao controle de movimentação, conforme item 3.2.
- **b) Modelagem da movimentação.** Discutiu-se se entrada e saída deveriam ser duas tabelas distintas. Optou-se por uma única tabela com um campo de tipo, solução mais simples e que facilita a geração do histórico em ordem cronológica.
- **c) Trabalho simultâneo no mesmo código.** Resolvido com o uso disciplinado do Git, com cada integrante responsável por arquivos distintos.

## 11. RESULTADOS E CONCLUSÃO

O sistema foi concluído dentro do prazo estabelecido, com todas as funcionalidades previstas no escopo em funcionamento e o código versionado no GitHub.

O principal aprendizado da equipe não foi técnico, mas de organização: delimitar o escopo no início e dividir claramente as responsabilidades foi o que permitiu concluir o projeto em um mês. A escolha de Django e PostgreSQL mostrou-se adequada, pois o framework reduziu significativamente o volume de código necessário e o banco relacional atendeu bem à natureza histórica dos dados.

Como evolução futura, a equipe aponta a integração com leitor de cartão ou biometria na portaria e o envio automático de notificação aos responsáveis no momento do registro.
