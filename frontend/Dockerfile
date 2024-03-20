FROM node:16-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/

COPY . /app/frontend/

RUN npm install --no-optional && npm cache clean --force

RUN chown -R node /app/frontend/node_modules

USER node

CMD ["npm", "start"]
