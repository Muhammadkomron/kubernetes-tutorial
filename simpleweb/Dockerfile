# Specify a base image
FROM node:alpine

WORKDIR /usr/app

COPY ./ ./
# Intall some depenendencies
RUN npm install

# Default command
CMD ["npm", "start"]
