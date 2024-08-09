#!/usr/bin/node

const request = require('request');

const getPeople = async (id) => {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  request(url, async (err, response, body) => {
    if (err) {
      console.log(err);
    }
    for (const Id of JSON.parse(body).characters) {
      await new Promise((resolve, reject) => {
        request(Id, (err, response, body) => {
          if (err) {
            reject(err);
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
};

async function main () {
  const id = process.argv[2];
  await getPeople(id);
}

main();
