# Coletor de Dados Climáticos

API para coletar dados climáticos de uma localização geográfica.

## Descrição

Esta API permite a coleta de dados climáticos, como temperatura, umidade, velocidade e direção do vento, de uma localização geográfica específica. A API utiliza dados fornecidos pela API do OpenWeather.

## Requisitos

- Python 3.10+
- FastAPI
- SQLAlchemy
- requests
- fastapi-pagination

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/MuriloUfms/coletordedadosclimaticos.git
   cd coletordedadosclimaticos
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
   Opcionalmente, você pode usar o poetry para gerenciar as dependências.


4. Configure as variáveis de ambiente:

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

   ```env
   OPEN_WEATHER_API_KEY=your_open_weather_api_key
   ```
   
   Também é possível definir as seguintes variaveis de ambiente para configurar o banco de dados e url do OpenWeather:

   ```env
   DATABASE_URL=sqlite:///database.db
   OPEN_WEATHER_URL=https://api.openweathermap.org/data/2.5/weather
   ```

## Execução

1. Inicie o servidor FastAPI:

   ```bash
   uvicorn src.main:app
   ```

2. Acesse a documentação interativa da API:

   Abra o navegador e acesse `http://127.0.0.1:8000/` para visualizar a documentação gerada pelo Swagger UI.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.