#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - There is only one calculation being done


b) O(log(n)) - The outer loop is O(n) but the inner loop cuts the runtime in half


c) O(n) - There is only one calculation being done, the return depends on the value being passed in

## Exercise II

I would approach this problem with a "binary search tree" type of solution, so that I would theoretically half the amount of broken eggs tested:

- Start at the middle floor and drop an egg
    - if the egg breaks, go to the mid of the bottom half
    - if the egg doesn't break, go to the mid of the top half
- Repeat this process until you can't find a mid anymore.
    - If the egg doesn't break, the answer is your current floor.
    - If the egg breaks, the answer is the floor below the current floor.
- The runtime complexity is O(log(n))
