#!/usr/bin/node
// a script that prints x times “C is fun”

if (process.argv[2] === 'undefined' || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  for (; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
