#!/usr/bin/node

const request = require('request');

const getPeople = async (id) => {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  await request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
};

function main () {
  const id = process.argv[2];
  getPeople(id);
}

main();
