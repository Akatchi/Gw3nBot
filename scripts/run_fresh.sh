# Build and up the containers in the main docker-compose file
docker-compose -f ../docker-compose.yml build
docker-compose -f ../docker-compose.yml up -d
