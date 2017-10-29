#!/usr/bin/env node

var fmap = [0, 1];

/*
 * Return the Fibonacci number for the given integer. Prior results are stored
 * (fmap) to reduce recursion (dynamic programming).
 * parameters:
 *   n - integer
 * returns:
 *   Fibonacci number
 */
function fib(n) {
    if (n >= fmap.length) {
        fmap.push(fib(n - 1) + fib(n - 2));
    }
    return fmap[n];
}

nums = [1, 2, 5, 9];

process.stdout.write("N Fn\n");    
for (var n = 0; n < nums.length; n++) {
    process.stdout.write(`${nums[n]} ${fib(nums[n])}\n`);
}