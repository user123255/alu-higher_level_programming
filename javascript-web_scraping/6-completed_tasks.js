#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

request(url, { json: true }, (err, response, todos) => {
  if (err) {
    console.error(err);
    return;
  }

  const completedTasks = {};

  todos.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });

  console.log(completedTasks);
});
