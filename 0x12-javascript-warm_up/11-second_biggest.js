#!/usr/bin/node

let nums = process.argv.slice(2);
nums = nums.map((num) => Number(num));

let max = -Infinity;
let prev;

for (let i = 0; i < nums.length; i++) {
  if (nums[i] > max) {
    prev = max;
    max = nums[i];
  }
}

if (nums.length > 1) {
  console.log(prev);
} else {
  console.log(0);
}
