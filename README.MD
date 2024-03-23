# API de Sporte 

## Descrição

`API` com `CRUD` de esportes, contendo jogadores, treinadores, e times.
Com documentação `Swagger` e `JWT` para autenticação.


## Tecnologias

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Django Rest Framework-092E20?style=for-the-badge&logo=django&logoColor=white">

<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black">


## Tutorial de como utilizar a API no Django

Neste tutorial, vamos abordar os passos para rodar a API em um ambiente virtual no Windows e Linux. É altamente recomendado o uso de ambientes virtuais para isolar as dependências do projeto e garantir um ambiente limpo e independente para a API.


## Clonando e configurando o projeto Django

1. Baixe ou clone o projeto Django da API.

2. Navegue para o diretório do projeto no terminal e execute o seguinte comando para clonar.

```bash
git clone https://github.com/Wenderson-Oscar/API_Sport.git
```

3. Dentro do projeto abra o terminal

## Configurando o ambiente virtual

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

No Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalando as dependências do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

##  Realizando as migrações do banco de dados

```bash
python manage.py migrate
```

## Iniciando o servidor de desenvolvimento

```bash
python manage.py runserver
```



