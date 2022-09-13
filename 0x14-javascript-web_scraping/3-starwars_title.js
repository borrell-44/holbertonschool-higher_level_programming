#!/usr/bin/node

const axios = require('axios');
const path = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`

axios.get(path).then(resp => {
  var result = resp.data
  console.log(result.title)
}).catch(err => {
  console.log(err);
  return err;
});
