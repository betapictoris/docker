# Creates template (JSON) files for Yacht and Portainer

import os
import json
import yaml

composeFiles = [x for x in os.listdir(".") if not x.startswith(".")]

def makeTemplate(container: str):
  details: dict = {}
  composeFile: dict = {}
  envFile: dict = []


  with open(f'{container}/about.yml') as f:
    details = yaml.safe_load(f)
  with open(f'{container}/docker-compose.yml') as f:
    composeFile = yaml.safe_load(f)
  if 'docker-compose.env' in os.listdir(f'./{container}'):
    with open(f'{container}/docker-compose.env') as f:
      for l in f.readlines():
        values = l.replace('\n', '').split('=')
        envFile.append({"name": values[0], "label": values[0], "default": values[1]})

  serviceCompose: dict = composeFile['services'][list(composeFile['services'])[0]]
  
  volumes: list = []

  if serviceCompose.get('volumes'):
    for v in serviceCompose['volumes']:
      container = v.split(":")
      volumes.append({'container': container[1], 'bind': container[0]})

  return {
    'type': 1,
    'title': details['title'],
    'name': serviceCompose['container_name'],
    'description': details['description'],
    'logo': details['logo'] if details.get('logo') else '//',
    'image': serviceCompose['image'],
    'categories': details['categories'],
    'platform': 'linux',
    'restart_policy': serviceCompose['restart'],
    
    'ports': serviceCompose['ports'],
    'network_mode': serviceCompose['network_mode'] if serviceCompose.get('network_mode') else 'bridge',
    'volumes': volumes,

    'env': envFile,
  }


templates: list = []

for c in composeFiles:
  print(f'Converting {c}...')
  templates.append(makeTemplate(c))

tempalteData = json.dumps(templates, indent=4)
 
# Writing to sample.json
with open("templates.json", "w") as outfile:
  print(f'Dumping template...')
  outfile.write(tempalteData)

print('Done!')