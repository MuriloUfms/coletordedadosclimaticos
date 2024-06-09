# Coletor de Dados Climáticos

API para coletar dados climáticos de uma localização geográfica.

## Descrição

Esta API permite a coleta de dados climáticos, como temperatura, umidade, velocidade e direção do vento, de uma localização geográfica específica. A API utiliza dados fornecidos pela API do OpenWeather.

## Requisitos

- Python 3.11+
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

## Rotas da API

### Coletas

- `POST /api/v1/coletas`
  
  Coleta dados climáticos de uma localização geográfica.

  **Request Body:**
  
  ```python
  {
    "latitude": float,
    "longitude": float
  }
  ```

  **Response:**
  
  ```python
  {
    "id": int,
    "latitude": float,
    "longitude": float,
    "temperatura": float,
    "umidade": int,
    "velocidade_vento": float,
    "direcao_vento": int
  }
  ```

- `GET /api/v1/coletas?page=1&size=10`
  
  Lista as coletas de dados climáticos.

  **Response:**
  
  ```python
  {
    "items": [
      {
        "id": int,
        "latitude": float,
        "longitude": float,
        "temperatura": float,
        "umidade": int,
        "velocidade_vento": float,
        "direcao_vento": int
      }
    ],
    "total": int,
    "page": int,
    "size": int,
    "pages": int,
    "links": {
      "first": str,
      "last": str,
      "self": str,
      "next": str,
      "prev": str,
    }
  }
  ```

## Estrutura do Projeto

```bash
.
├── src
│   ├── db.py             # Configurações do banco de dados
│   ├── main.py           # Inicialização da aplicação FastAPI
│   ├── models.py         # Definição dos modelos de dados
│   ├── routers
│   │   └── coleta.py     # Rotas relacionadas a coletas
│   ├── schemas.py        # Schemas para validação de dados
│   └── services.py       # Funções de serviço para coleta de dados
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.