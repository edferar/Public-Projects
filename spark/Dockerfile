# Usando uma imagem base do Spark
FROM gcr.io/spark-operator/spark:v3.1.1

# Adiciona scripts ou configurações personalizados, se necessário
# COPY path/to/your/custom/config /opt/spark/conf/

# Adiciona bibliotecas dependentes, se necessário
# RUN apt-get update && apt-get install -y some-package

# Exemplo de adicionar um arquivo jar ao Spark
# COPY your-application.jar /opt/spark/jars/
RUN mkdir -p /app
COPY script_example.py /app/
WORKDIR /app
RUN ls -l

CMD ["/opt/spark/bin/spark-submit"]


