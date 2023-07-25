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
        if (task.userId in usersAndTasks) {
          usersAndTasks[`${task.userId}`]++;
        } else {
          usersAndTasks[`${task.userId}`] = 1;
        }
      }
    }
    console.log(usersAndTasks);
  }
});
