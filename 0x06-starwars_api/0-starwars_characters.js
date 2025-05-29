#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie in order of appearance
 */
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

request(apiUrl, (err, res, body) => {
  if (err) return;

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index === characters.length) return;
    request(characters[index], (err2, res2, body2) => {
      if (!err2) {
        const characterName = JSON.parse(body2).name;
        console.log(characterName);
        printCharacter(index + 1);
      }
    });
  };

  printCharacter(0);
});
