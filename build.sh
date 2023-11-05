# builds a Docker image
docker build -t movie-sentiment-prediction-app .

# lists all Docker images
docker images

#  run a Docker container based on the image
docker run -it imageid sh

#  run Docker container
docker run -p 7860:7860 --name movie-review-sentiment movie-sentiment-prediction-app

#  list all containers 
docker ps -a 

# display the logs
docker logs -f movie-review-sentiment       