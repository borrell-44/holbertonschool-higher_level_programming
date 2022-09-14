#!/usr/bin/node

const axios = require('axios');
const path = 'https://swapi-api.hbtn.io/api/films';
const id = parseInt(process.argv[2]) - 1;

axios.get(path).then(resp => {
  const values = resp.data;

  for (let i = 0; i < (values.results).length; i++) {
    if (i === id) {
      const api = values.results[i].characters;
      for (let j = 0; j < api.length; j++) {
        for (let k = 0; k < api.length; k++) {
          axios.get(api[k]).then(response => {
            if (api[j] === response.data.url) {
              console.log(response.data.name);
            }
          });
        }
      }
      return;
    }
  }
}).catch(err => {
  console.log(err);
  return err;
});
