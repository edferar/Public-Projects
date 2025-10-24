Siga os passos abaixo para execucao do jupyter dentro do ambiente do kubernetes, certifique-se de ter o Kubernetes devidamente configurado.


1 - Criando o namespace que iremos utilizar
    - kubectl create namespace jupyter

2 - Adicionando repositorios ao helm

    helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    helm repo update

    O comando abaixo ira apoiar na identificacao das versoes disponiveis dentro do repo adicionado, neste exemplo iremos seguir com a versao 4.2.0  do jupyter

    - helm search repo jupyter
    - helm show values jupyterhub/jupyterhub > values.yaml #gerar arquivo values.yaml

3 - Realizando a instalacao
    - helm install jupyterhub jupyterhub/jupyterhub --namespace jupyter --version 4.2.0 --values values.yaml

4 - Acessando o Jupyter
    Para acessar digite o endereco http://localhost:80 no seu navegador, as credenciais configuradas estao presentes no arquivo values.yaml