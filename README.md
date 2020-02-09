# cloud-process-music [![Build Status](https://travis-ci.com/K-u-K/cloud-process-music.svg?branch=master)](https://travis-ci.com/K-u-K/cloud-process-music)

The goal is to create an AWS Webservice which allows 
the upload, conversion and download of MIDI audio 
sound files into a self-defiend output format. For this 
purpose two microservices are implemented, one either
for frontend and backend. 

The frontend is made using SPA - technologies 
(React, Vue, Inferno) while the backend is based on 
the Python technologies (Django, Flask). 

All uploaded files are cached in a RedisDB - which is 
also realised as an own service as well - to increase
conversion performance and to reuse the already
converted results

All services are dockerized and pushed to a 
docker registry on every commit using TravisCI 
as the CI/CD solution

After pushing to the registry, the images are deployed
and provisioned with a Kubernetes cluster running on
either an AWS EC2 or AWS EKS instance. 

Optionally, AWS Lambda is used to implemented
only the specific code fragment which performs
the conversion of the audio files

TLDR: do not use thies program