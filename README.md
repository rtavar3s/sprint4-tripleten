# Dashboard de anúncios de vendas de carros

Aplicativo web interativo construído com Streamlit para exploração visual do conjunto de dados de anúncios de vendas de carros (`vehicles_us.csv`).

## Funcionalidades

- Botão que cria um histograma interativo da coluna `odometer` (plotly-express)
- Botão que cria um gráfico de dispersão `odometer` × `price` (plotly-express)
- Análise exploratória de dados preliminar no notebook `notebooks/EDA.ipynb`

## Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Aplicativo publicado no Render: URL disponível aqui após o deploy (a preencher: https://<APP_NAME>.onrender.com/).
