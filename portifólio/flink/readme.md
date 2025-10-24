kubectl create -f https://github.com/jetstack/cert-manager/releases/download/v1.8.2/cert-manager.yaml



helm repo add flink-operator-repo https://downloads.apache.org/flink/flink-kubernetes-operator-1.11.0/
helm install flink-kubernetes-operator flink-operator-repo/flink-kubernetes-operator

kubectl create -f https://raw.githubusercontent.com/apache/flink-kubernetes-operator/release-1.11/examples/basic.yaml
kubectl logs -f deploy/basic-example


kubectl port-forward svc/basic-example-rest 8081



kubectl create -f https://github.com/jetstack/cert-manager/releases/download/v1.8.2/cert-manager.yaml


$ kubectl port-forward svc/python-example-rest 8081
$ docker build -t  edferar/apache_flink_operator:latest .

# apiVersion: flink.apache.org/v1beta1
# kind: FlinkDeployment
# metadata:
#   name: pyflink-job
# spec:
#   image: edferar/apache_flink_operator:latest # Ou sua imagem customizada
#   flinkVersion: v1_17
#   flinkConfiguration:
#     taskmanager.numberOfTaskSlots: "2"
#     parallelism.default: "2"
#     s3.access.key: CFqqfOIRBh1ptpVDuD3e
#     s3.secret.key: q4JBnzD0SVZphpoXGRPv3gYX3F8vmTssKxHkNFsT
#     s3.endpoint: http://172.18.0.2:9000
#     s3.path.style.access: "true"
#     s3.impl: org.apache.hadoop.fs.s3a.S3AFileSystem
#     fs.s3a.aws.credentials.provider: org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider
#   jobManager:
#     resource:
#       memory: "1024m"
#       cpu: 1
#   taskManager:
#     resource:
#       memory: "2048m"
#       cpu: 1
#   serviceAccount: flink
#   job:
#     jarURI: s3a://default/flink_app.py
#     entryClass: "" # em jobs PyFlink, deixar vazio
#     state: running
#     parallelism: 1
#     upgradeMode: stateless



stmt_set = t_env.create_statement_set()

stmt_set.add_insert("output1", t_env.sql_query("SELECT * FROM input WHERE tipo = 'A'"))
stmt_set.add_insert("output2", t_env.sql_query("SELECT * FROM input WHERE tipo = 'B'"))

stmt_set.execute()