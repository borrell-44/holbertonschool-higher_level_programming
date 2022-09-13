#!/usr/bin/node

const axios = require('axios');
const path = process.argv[2];
let count = 0;

axios.get(path).then(resp => {
  const result = resp.data;

  for (let i = 0; i < (result.results).length; i++) {
    for (let j = 0; j < (result.results[i].characters).length; j++) {
      if (result.results[i].characters[j].includes('18')) count++;
    }
  }
  console.log(count);
}).catch(err => {
  console.log(err);
  return err;
});
