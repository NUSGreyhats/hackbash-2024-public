FROM node:18-bullseye-slim

RUN apt-get update && \
apt-get install -y dumb-init && \
rm -rf /var/lib/apt/lists/*

ENV NODE_ENV=production

RUN addgroup cookies && \
adduser --disabled-password --gecos "" --ingroup cookies cookies

WORKDIR /home/cookies/app
RUN chown -R cookies:cookies .

COPY ./static ./static
COPY main.js package.json ./

RUN npm install

USER cookies

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["node", "./main.js"]
