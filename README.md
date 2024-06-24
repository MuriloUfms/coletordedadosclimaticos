# Coletor de Dados Climáticos

**Source Code**: https://github.com/MuriloUfms/coletordedadosclimaticos

---

Aplicação baseada em microserviços para coleta de dados climáticos e subscrição para notificações periodicas.


## Entregas Parciais

### [TP - Entrega 1] Newsletter Service - Registro de usuários para envio

- Organização do repositorio utilizando o padrão de mono-repo.

- Definição do serviço `coletor_service` para coleta de dados climáticos.

- Criação do serviço `newsletter_service` para registro de usuários e envio de notificações.

- docker-compose para execução dos serviços usando postgresql como banco de dados.


### [TP - Entrega 2] Newsletter Service - Envio de boletins informativos

- Adicionado agendador de tarefas que coleta os dados de 30 em 30 minutos e envia emails para os usuários cadastrados.

- Mudança na forma de armazenar o intervalo de envio de boletins (antes era uma palavra fixa, agora um inteiro que representa o intervalo em horas).
