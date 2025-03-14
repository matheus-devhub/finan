# Finan - Gerenciador de Despesas Pessoais

📌 Este documento readme está disponível em [Inglês](README.md).

![Python](https://img.shields.io/badge/Python-3.13.2%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)
![matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos-purple)
![pandas](https://img.shields.io/badge/Pandas-Dados-brown)
![Status](https://img.shields.io/badge/Status_do_projeto-Em_Desenvolvimento-yellow)

Finan é uma aplicação para controle de despesas pessoais, desenvolvida em **Python** com uma interface gráfica intuitiva utilizando **Tkinter**. O objetivo do projeto é fornecer uma solução prática e eficiente para gerenciar finanças, permitindo o acompanhamento de receitas e despesas financeiras.

## 📌 Funcionalidades

✅ Adicionar e excluir despesas e receitas.
✅ Classificação por categorias (Alimentação, Transporte, Lazer, etc.).
✅ Visualização de saldo atualizado em tempo real.
✅ Persistência de dados em banco SQLite.


## 🛠 Tecnologias Utilizadas

- **Python 3.13.2+** (Linguagem de programação)
- **Tkinter** (Interface gráfica)
- **SQLite** (Banco de dados local)
- **Matplotlib** (Geração de gráficos)
- **Pandas** (Manipulação de dados)

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/matheus-devhub/finan.git
   cd finan
   ```
2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Linux/Mac
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python main.py
   ```

<!-- ## 🖥 Capturas de Tela

*Imagens da interface do aplicativo para ilustrar seu funcionamento a serem adicionadas.* -->

## 🗂 Estrutura do Projeto
```
finan/
│-- img/  # Icones e imagens
│-- .gitignore  # arquivos ignorados pelo Git
│-- createDB.py  # Criação das tabelas do banco de dados
│-- finan.db  # banco de dados
│-- main.py  # Arquivo principal
│-- README.md  # Documentação do projeto em Inglês
│-- README.pt-BR.md  # Documentação do projeto em Português
│-- requirements.txt  # Dependências
│-- view.py  # Criação do banco de dados
```

## 📋 Roadmap

🔹 Implementar suporte a múltiplas moedas
🔹 Melhorar o design da interface com Tkinter e ttk
🔹 Criar versão web com Flask/Django
🔹 Adicionar suporte a notificações e lembretes

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b minha-feature`)
3. Faça suas alterações e commit (`git commit -m 'Adicionando nova funcionalidade'`)
4. Envie para o repositório (`git push origin minha-feature`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Caso tenha dúvidas, sugestões ou feedbacks, sinta-se à vontade para entrar em contato:

📧 Email: [matheus.softwaredev@gmail.com](mailto:matheus.softwaredev@gmail.com)

🌍 GitHub: [github.com/matheus-devhub](https://github.com/matheus-devhub)

🔗 LinkedIn: [linkedin.com/in/matheusdevhub](https://www.linkedin.com/in/matheusdevhub)