#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    const usersAndTasks = {};

    for (const task of tasks) {
      if (task.completed === true) {
        if (usersAndTasks[task.userId] === undefined) {
          usersAndTasks[task.userId] = 1;
        } else {
          usersAndTasks[task.userId]++;
        }
      }
    }
    console.log(usersAndTasks);
  }
});
