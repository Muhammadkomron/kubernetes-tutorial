# Specify a base image
FROM node:alpine

WORKDIR /app

COPY package.json .
# Intall some depenendencies
RUN npm install

COPY . .

# Default command
CMD ["npm", "start"]
