# Site Institucional da ONG Mãos Unidas :handshake:

 Este repositório contém o código-fonte do site institucional da ONG Mãos Unidas, desenvolvido como parte de um projeto de extensão universitária. O objetivo é criar uma plataforma digital para aumentar a visibilidade da ONG e facilitar o contato com os voluntários e o público interessado.

## Sobre a ONG Mãos Unidas :globe_with_meridians:

A Mãos Unidas é uma organização que realiza tratamentos e oferece suporte para pessoas com autismo. Seu foco está em proporcionar um ambiente inclusivo e acolhedor para as pessoas atendidas, promovendo o bem-estar e a inclusão social através de atividades terapêuticas e educacionais.

## Funcionalidades do Projeto :computer:

    - Agentamento de Consulta
    - Cadastro de Voluntário
    - Lista de Eventos atualizada

## Tecnologias Utilizadas :hammer_and_wrench:

    - Frontend: HTML5, CSS3, JavaScript
    - Backend: Django (Python)
    - Banco de Dados: MySql
    - Deploy: PythonAnywhere


## Como Rodar o Projeto :rocket:

### Pré-requisitos

    - Python 3.x
    - Virtualenv
    - Git

### Bliblotecas utilizadas

    - validate-docbr
    - pillow
    - psycopg2
    
## Tutorial 

#### Crie um ambiente virtual:

    python -m venv venv

### Ative o ambiente virtual:

#### Windows 

    venv\Scripts\activate

#### Linux 
 
    source venv/bin/activate

#### Clone este repositório:

    git clone git@github.com:Luis5Felipe/webisiteong.git

#### Instale as dependências:

    pip install -r requirements.txt

#### Rode as migrações do banco de dados:

    python manage.py migrate

#### Inicie o servidor:

    python manage.py runserver


## Contato :mailbox_with_mail:

Desenvolvido por [Luis Felipe](https://www.linkedin.com/in/luis-felipe-dos-santos/) e [Keven Pinto](https://www.linkedin.com/in/keven-pinto-fernandes-912ab521a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) como parte do projeto de extensão da Unilasalle.

# Licença :page_facing_up:
