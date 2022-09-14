#!/usr/bin/node

const axios = require('axios');
const path = process.argv[2];
const data = {};

axios.get(path).then(resp => {
  const values = resp.data;
  for (let i = 0; i < values.length; i++) {
    if ((values[i].userId in data) === false) {
      data[values[i].userId] = 0;
    }
    if (values[i].completed === true) {
      data[values[i].userId] += 1;
    }
  }
  console.log(data);
}).catch(err => {
  console.log(err);
  return err;
});
