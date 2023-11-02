docker build -t movie-sentiment-prediction-app .
docker images
docker run -it imageid sh
docker run -p 7860:7860 --name movie-review-sentiment movie-sentiment-prediction-app
docker ps -a 
docker logs -f movie-review-sentiment       