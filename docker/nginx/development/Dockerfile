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

# Using the deps we've just installed and to run the `start` command located
# in package.json (builds the development react app).
# RUN runs the command inside the container and builds a cachable image
# CMD runs the command inside the container but uses the last built image to execute continuosly
CMD ["npm", "start"]
