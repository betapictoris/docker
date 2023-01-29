# Beta Pictoris's Docker Compose files

## What's set

- Traefik and Flame labels
- Ports
- Rootless volumes
- Auto-restart
- Container names
- Docker Compose 3+

## Running a container

1. Change into the directory of the service you want.
2. Edit the `docker-compose.env` file, if there is one present.
3. Edit Traefik and Flame labels to match your system/hostname.
4. Run `docker-compose up -d` or `docker compose up -d`, this will depend on
   how you have Docker Compose setup and installed.
5. _Enjoy!_

## Using with Portainer or Yacht

Add the template file with this URL:

```
https://github.com/BetaPictoris/docker/raw/dev/templates.json
```

## Docker Compose structure

All of the Docker Compose files are structured in the same way.
Starting with the image, command, container name, and restart
`unless-stopped` settings. Then devices and volumes are set.
Finally networking related changes are set, this includes ports
and labels.
