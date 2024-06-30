# https://docs.tilt.dev
load('ext://namespace', 'namespace_create', 'namespace_inject')
namespace_create('metatrader-terminal')

docker_build('metatrader', 'services/metatrader', dockerfile = 'services/metatrader/Dockerfile.mt5')
docker_build('exchange', 'services/exchange', dockerfile = 'services/exchange/Dockerfile.dev')


yaml = helm(
  'infrastructure/k8s',
  # The release name, equivalent to helm --name
  name='app',
  # The namespace to install in, equivalent to helm --namespace
  namespace='metatrader-terminal',
  # The values file to substitute into the chart.
  values=['infrastructure/k8s/values.yaml', 'infrastructure/k8s/env.yaml'],
  # Values to set from the command-line
  #   set=['service.port=1234', 'ingress.enabled=true']
)

k8s_yaml(yaml)

k8s_resource('metatrader', port_forwards=['5900', '8000'])
k8s_resource('db', port_forwards='5432')


# command:
# tilt up --namespace=metatrader-terminal
# 
