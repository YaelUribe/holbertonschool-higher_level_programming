#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, req, body) {
  if (err) {
    console.log(err);
  }
  const DaBody = JSON.parse(body);
  const completed = {};
  for (const x in DaBody) {
    const duty = DaBody[x];
    const IDs = duty.userId;
    if (duty.completed === true) {
      if (completed[IDs] === undefined) {
        completed[IDs] = 1;
      } else {
        completed[IDs] += 1;
      }
    }
  }
  console.log(completed);
});
