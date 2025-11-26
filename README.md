# 🎲 Simulador de Lançamento de Moeda — Streamlit + Render

Este projeto foi desenvolvido como parte do **Sprint 5: Ferramentas de Desenvolvimento de Software**, com foco em criar, expandir e implantar um aplicativo web utilizando **Python**, **Streamlit** e **Render**.

O objetivo é simular lançamentos de moeda, exibir o progresso em tempo real e manter um histórico de resultados entre execuções utilizando o `st.session_state` do Streamlit.

---

## 🚀 Funcionalidades

✔️ Controle deslizante para definir o número de tentativas
✔️ Botão para iniciar o experimento
✔️ Gráfico de linha atualizando em tempo real
✔️ Cálculo da média cumulativa das tentativas
✔️ Tabela de resultados de todas as execuções
✔️ Persistência via `session_state`
✔️ Aplicativo totalmente implantado no **Render**

---

## 🧠 Lógica do Aplicativo

O app simula lançamentos de moeda utilizando uma distribuição Bernoulli:

* `0` representa cara
* `1` representa coroa

A cada resultado, a média é recalculada e adicionada ao gráfico, mostrando como o valor converge para **0.5** conforme o número de tentativas aumenta.

O histórico completo é salvo em um DataFrame persistente usando:

```python
st.session_state['df_experiment_results']
```

Isso permite guardar:

* número do experimento
* quantidade de tentativas
* média final

Mesmo após múltiplos cliques no botão.

---

## 🗂 Estrutura do Projeto

```
.
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

---

## 📦 Dependências

As bibliotecas usadas são:

```
pandas==1.3.1  
scipy==1.6.2  
streamlit==1.12.2
```

---

## ▶️ Como rodar o app localmente

1. Clone o repositório:

```
git clone https://github.com/SEU_USUARIO/render-newapp.git
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o aplicativo:

```
streamlit run app.py
```

Acesse pelo navegador:

```
http://0.0.0.0:10000/
```

---

## ☁️ Deploy no Render

O Render foi configurado com:

**Build Command**

```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command**

```
streamlit run app.py
```

Todo commit enviado ao GitHub dispara automaticamente uma nova implantação.

---

## 🛠 Tecnologias Utilizadas

* **Python**
* **Streamlit** (framework rápido para apps de dados)
* **SciPy** (geração de amostras Bernoulli)
* **Pandas** (armazenamento e manipulação de resultados)
* **Render** (deploy contínuo)
* **Git + GitHub**

---


## 📚 Aprendizados desse projeto

* Como estruturar um aplicativo Streamlit
* Uso de widgets (slider, button, charts)
* Como manter estados entre execuções com `session_state`
* Processo completo de deploy com Render
* Versionamento com Git e GitHub

