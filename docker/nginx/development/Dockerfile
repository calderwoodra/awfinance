# To build and run this container on it's own:
# docker build -t nginx . -f docker/nginx/Dockerfile && docker run -it nginx

####### The first stage #######
##  Build React static files ##

# Use node (for npm) and alpine (small size)
# label it as `build` so that we can copy from it later
FROM node:13.12.0-alpine as build

# Create the directory /app/frontend/ in the docker container/image
WORKDIR /app/frontend

# Copy local files package.json and package-lock.json to the container
# in the working directory (/app/frontend/) so that the project
# dependencies and be installed via npm
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./

# Install the project dependencies.
# npm is a package manager (node package manager)
# `npm ci` is similar to `npm install` except that it expects a
#   package-lock.json file to be present and will install all deps
#   exactly as they are specified in the package-lock.json file.
#   `npm install` will always delete package-lock.json and rebuild it.
# --silent suppresses errors/logging output
RUN npm ci --silent

# Copy all local files in awsick/frontend/ to WORKDIR (/app/frontend/)
# COPY ./frontend/ ./

# Using the deps we've just installed and the code we've just copied,
# run the `build` command located in package.json (builds the production
# react app).
#RUN npm run build

# Using the deps we've just installed and the code we've just copied,
# run the `start` command located in package.json (builds the development
# react app).
# RUN npm run start


############## The second stage ##############
##  Copy React static files and start nginx ##

# Use nginx so that we can run nginx commands
# Use alpine because it is small
# FROM nginx:stable-alpine

# Copy the files from the previous image/FROM labeled `build` located at
# /app/frontend/build to /usr/share/nginx/html.
# /app/frontend/build because this is where `npm run start` outputs the react build
# /usr/share/nginx/html because the nginx:stable-alpine image installs nginx here
# COPY --from=build /app/frontend/build /usr/share/nginx/html

# nginx is a proxy server + load balancer... need to expand here.
# deamon on is the default setting for nginx and it will cause the
#  nginx server to spawn in the background which will cause docker
#  to hang. To prevent this, we use the -g CLI flag to easily modify
#  the nginx.conf file to set deamon off, which will start the nginx
#  server in the foreground and not break docker.
CMD ["npm", "start"]
