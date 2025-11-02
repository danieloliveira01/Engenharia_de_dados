Engenharia de Dados com Apache Airflow e Consumo de API

Este projeto tem como objetivo desenvolver uma pipeline de engenharia de dados utilizando o Apache Airflow para realizar a extração de dados de uma API contendo postagens do Twitter, armazenando-os em um Data Lake para posterior análise por equipes de Ciência de Dados e Machine Learning.

🔄 Arquitetura da Pipeline

A pipeline segue as etapas clássicas de ETL:

Extração: Realiza requisições para a API do Twitter e coleta as postagens.

Transformação: Limpeza e padronização dos dados coletados.

Carregamento: Armazenamento no Data Lake, organizando os dados em diretórios particionados por data de execução, facilitando consultas futuras.

🛠️ Tecnologias Utilizadas

Python → Desenvolvimento dos scripts de extração, transformação e carregamento.

Apache Airflow → Orquestração e automação da pipeline.

API do Twitter → Fonte de dados.

✅ Benefícios da Solução

Automação completa do fluxo de dados

Organização dos arquivos por data de execução

Melhor governança e rastreabilidade dos dados

Base preparada para consumo eficiente por modelos de dados e análises

▶️ Como Executar

Certifique-se de que o Apache Airflow está instalado e configurado corretamente.

Mova os arquivos do projeto para o diretório dags/ do seu Airflow.


