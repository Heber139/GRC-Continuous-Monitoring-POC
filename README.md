# 🛡️ GRC Continuous Monitoring - POC

Este projeto é uma **Prova de Conceito (POC)** desenvolvida para demonstrar a aplicação de **Monitoramento Contínuo** em Controles Internos.

O objetivo é automatizar a validação de regras de negócio (Compliance), substituindo verificações manuais por scripts de auditoria escaláveis.

## 📋 Cenário de Negócio
Em operações financeiras críticas, aprovações manuais fora da janela operacional padrão representam alto risco de fraude ou falha de processo.
* **Regra Auditada:** Nenhuma aprovação manual deve ocorrer entre **00:00 e 05:00**.
* **Método Tradicional:** Análise amostral ou manual em planilhas.
* **Solução Proposta:** Script Python para varredura integral da base de dados e alerta visual automático.

## 🚀 Tecnologias Utilizadas
* **Python 3.10+**
* **Pandas:** Manipulação de dados (ETL).
* **Matplotlib:** Geração de evidências visuais.

## 🛠️ Como Executar
1. O arquivo `transacoes_mock.csv` contém os dados simulados.
2. O script `analise_fraude.py` lê os dados e verifica violações de horário (0h-5h).
3. Se houver fraude, um gráfico de alerta é gerado.

---
**Disclaimer:** Dados fictícios gerados para fins educacionais e de demonstração de competência em auditoria automatizada.
