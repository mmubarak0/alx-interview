#!/usr/bin/node

const request = require('request');

const getPeople = async (id) => {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  await request.get(url, async (error, response, body) => {
    if (error) {
      throw error;
    }
    const characters = JSON.parse(body).characters;
    await characters.forEach(async (character) => {
      await request(character, async (error, response, body) => {
        if (error) {
          throw error;
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
};

async function main () {
  const id = process.argv[2];
  await getPeople(id);
}

main();
