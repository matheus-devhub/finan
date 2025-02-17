# Finan - Gerenciador de Despesas Pessoais

📌 Este documento readme está disponível em [Inglês](README.md).

![Finan](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Finan é uma aplicação para controle de despesas pessoais, desenvolvida em **Python** com uma interface gráfica intuitiva utilizando **Tkinter**. O objetivo do projeto é fornecer uma solução para gerenciar finanças, permitindo o acompanhamento de receitas e despesas.

## 📌 Funcionalidades

✅ Adicionar, editar e excluir despesas e receitas
✅ Classificação por categorias (Alimentação, Transporte, Lazer, etc.)
✅ Visualização de saldo atualizado em tempo real
✅ Geração de relatórios financeiros
✅ Interface amigável e responsiva
✅ Persistência de dados em banco SQLite
✅ Exportação de dados para CSV

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**
- **Tkinter** (Interface gráfica)
- **SQLite** (Banco de dados local)
- **Matplotlib** (Geração de gráficos)
- **Pandas** (Manipulação de dados)

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/finan.git
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

## 🖥 Capturas de Tela

*Adicione aqui imagens da interface do aplicativo para ilustrar seu funcionamento.*

## 🗂 Estrutura do Projeto
```
finan/
│-- main.py  # Arquivo principal
│-- gui.py  # Interface gráfica com Tkinter
│-- database.py  # Gerenciamento do banco de dados SQLite
│-- models.py  # Estrutura de dados e classes
│-- reports.py  # Geração de relatórios financeiros
│-- assets/  # Ícones e imagens
│-- README.md  # Documentação do projeto
│-- requirements.txt  # Dependências
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

📧 Email: [seuemail@dominio.com](mailto:seuemail@dominio.com)

🌍 GitHub: [github.com/seuusuario](https://github.com/seuusuario)

🔗 LinkedIn: [linkedin.com/in/seuusuario](https://linkedin.com/in/seuusuario)