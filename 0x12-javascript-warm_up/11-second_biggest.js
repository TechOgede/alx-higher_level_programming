#!/usr/bin/node

let nums = process.argv.slice(2);
nums = nums.map((num) => Number(num));

if (nums.length > 1) {
  let max = Math.max.apply(null, nums);
  const idx = nums.indexOf(max);
  nums.splice(idx, 1);
  max = Math.max.apply(null, nums);
  console.log(max);
} else {
  console.log(0);
}
