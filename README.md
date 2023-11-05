# kbs-eks-alb
Machine Learning App hosted on EKS Cluster and exposed through a AWS Application Load Balancer

In https://github.com/vinods03/k8s-eks-clb, we saw a Classic Load Balancer (CLB) being used to host machine learning apps on a Kubernetes (EKS) cluster.
Here, we will be using an Application Load Balancer (ALB).
We will also setup our own domain (Route 53) and enable SSL on the domain.

Why ALB ? These are some of the main advantages:

ALB supports context path-based routing for our applications. So a single load balancer can be leveraged for using multiple applications based on context paths.
ALB supports host-based routing.
ALB supports routing based on fields inside the request like HTTP headers, HTTP methods, query parameters, and source IP addresses.
ALB supports redirecting request from one URL to another.
ALB supports authentication of users of our applications through their corporate or social identities before routing requests.

One important aspect of using an ALB with EKS is and Ingress Controller (also known as the Load Balancer Controller)
The controller triggers the creation of an application load balancer and the necessary support AWS resources whenever an ingress resource is created in the EKS cluster.
