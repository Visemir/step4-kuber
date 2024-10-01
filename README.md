#MOST ACTIONS WERE CARRIED OUT THROUGH CI/CD GITLAB
1. Creating a simple application

●      Use Python programming language to create a simple [web application with MySQL database](https://github.com/Visemir/step4-kuber/tree/main/src)

●      Create a [Dockerfile](https://github.com/Visemir/step4-kuber/blob/main/src/Dockerfile) to build a container image of your application.

.

2. Setting up a Kubernetes Cluster

●      MiniKube:

○      Install MiniKube on your local machine to create a single-node Kubernetes cluster.

○      Start the cluster using minikube start.

●      Kubernetes Configuration Files:

○      [Create YAML files to define your application's deployment, service, and other resources.](https://github.com/Visemir/step4-kuber/tree/main/cluster)

3. Deploying the Application

●      Use kubectl to apply your YAML files to the Kubernetes cluster.

●      Check the status of your deployment and service using kubectl get pods and kubectl get services.

4. Integrating with GitLab

●      Configure GitLab CI/CD to automatically build, test, and deploy your application to Kubernetes.

●      Create a GitLab CI/CD pipeline using a [.gitlab-ci.yml file.](https://github.com/Visemir/step4-kuber/blob/main/.gitlab-ci.yml)

5. [Persistent Volumes](https://github.com/Visemir/step4-kuber/blob/main/cluster/add-volumes.yaml)

●      Create a persistent volume claim (PVC) to request storage for your application.

●      Create a persistent volume (PV) to provision storage for the PVC.

●      Mount the PV to your application's pod.

![](https://github.com/Visemir/step4-kuber/blob/main/image/cluster.jpg)

![](https://github.com/Visemir/step4-kuber/blob/main/image/build.jpg)

![](https://github.com/Visemir/step4-kuber/blob/main/image/test.jpg)

![](https://github.com/Visemir/step4-kuber/blob/main/image/push.jpg)

![](https://github.com/Visemir/step4-kuber/blob/main/image/deploy.jpg)

![](https://github.com/Visemir/step4-kuber/blob/main/image/site.jpg)





