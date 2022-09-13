#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');
const path = process.argv[2];
const file = process.argv[3];

axios.get(path).then(resp => {
  fs.writeFile(file, resp.data, 'utf-8', (error) => {
    if (error) console.log(error);
  });
}).catch(err => {
  console.log(err);
  return err;
});
