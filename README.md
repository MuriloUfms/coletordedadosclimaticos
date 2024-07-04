# Coletor de Dados Climáticos FACOM/UFMS

Aplicação fullstack para coletar dados climáticos da FACOM.

## Descrição

Este projeto baseado em microserviços consiste em uma aplicação fullstack para coletar dados climáticos de uma localização geográfica específica. A aplicação é composta por três serviços:

- [Coletor Service](coletor_service/README.md): API para coletar dados climáticos de uma localização geográfica.
- [Newsletter Service](newsletter_service/README.md): API para inscrição na newsletter de dados climáticos.
- [Web Service](web_service/README.md): Frontend da aplicação de coleta de dados climáticos.

## Requisitos

- Docker
- Docker Compose

PS: Para executar a aplicação sem Docker, deve-se ter o python 3.10+ instalado e o poetry para gerenciar as dependências. 
Os serviços devem ser executados e configurados individualmente.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/MuriloUfms/coletordedadosclimaticos.git
   cd coletordedadosclimaticos
   ```

2. Altere as variáveis de ambiente no arquivo `docker-compose.yml`:

3. Execute o Docker Compose:

   ```bash
   docker-compose up
   ```
4. O serviço estará disponível nas seguintes URLs:

   - Web Service: [http://localhost](http://localhost)
   - Coletor Service: [http://localhost/coletor/docs](http://localhost/coletor/docs)
   - Newsletter Service: [http://localhost/newsletter/docs](http://localhost/newsletter/docs)


## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.