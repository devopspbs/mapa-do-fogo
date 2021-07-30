# Back-end do mapa do fogo

## Iniciando o ambiente de desenvolvimento e teste

Com o git instalado e devidamente configurado rodar:

```console
git clone https://gitlab.com/devopspbs/community/mapa-do-fogo-backend.git
cd mapa-do-fogo-backend
```

Em seguida é necessário criar o volume para o conteiner de banco de dados:
```console
docker-compose volume create mapa-do-fogo
```

Com docker e docker-compose devidamente instalados e configurados. Execute o ambiente:

```console
docker-compose up
```

Se você estiver rodando Docker diretamente sobre Linux pode ser necessário ajustar as permissões. Lembre-se de repetir o comando abaixo sempre que estiver com problemas para acessar os arquivos diretamente no Docker host.

```console
sudo chown -R $USER:$USER .
```

Após iniciar o ambiente é preciso realizar rodar os scripts de incialização do banco de dados e criar o usuário administrador:

Iniciando o banco de dados:

```console
docker-compose exec web python manage.py migrate
```

OBS: deve ser executado logo após o comando migration.

Criando super usuário:
```console
docker-compose exec web python manage.py createsuperuser --username=teste --email=teste@gmail.com
```

Após esses passos a API Django estará acessível em http://localhost:8000.

## Referências

https://git-scm.com/downloads

https://docs.docker.com/install/

https://docs.docker.com/compose/install/

https://docs.docker.com/compose/django/

https://gitlab.com/devopspbs/django/django-docker-compose

## License

GPLv3 or later.
