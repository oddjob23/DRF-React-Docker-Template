# pull official base image
FROM node:14.8.0-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json .

RUN yarn
# copy project
COPY . .
CMD ["yarn", "start"]

