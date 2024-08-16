# blur-app

## Intro
The `src` folder contains the application code that allows you to blur the image and the Dockerfile to build image, the `image-blur` folder is the helm-chart.

## Getting started
As it has been developed and tested for GCP, define the **project_id** and **deployment.image.repository** values in the `values file` before installing the chart.
Then build the image and push it to the `GCP Artifactory`.

## Instalattion
To install and upgrade helm chart, use the following commands:
```
helm install image-blur ./image-blur --namespace application --create-namespace

helm upgrade image-blur ./image-blur --namespace application

```
After installing or updating the chart release, you will see a message telling you how to test the blur application. Or check the `NOTES.txt` of the chart.

## Cleaning up
To clean up:
```
helm uninstall -n application  image-blur


```

In case if you deployed an Ingress and added a record into your `/etc/hosts` file:
```

sudo sed -i '' "/$A_RECORD/d" /etc/hosts

```