#!/usr/bin/node

const axios = require('axios');
const path = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(path).then(resp => {
  const result = resp.data;
  console.log((result.films).length);
}).catch(err => {
  console.log(err);
  return err;
});
