#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, req, body) {
  if (err) {
    console.log(err);
  }
  const result = JSON.parse(body).results;
  let incidences = 0;

  for (const idx in result) {
    const characters = result[idx].characters;
    for (const x in characters) {
      if (characters[x].includes('18')) {
        incidences++;
      }
    }
  }
  console.log(incidences);
});
