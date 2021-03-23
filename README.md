# ITMO-CPO-LAB_1

This repo is the Lab1 of Computational Process Organization in ITMO, 2021 spring.

## TITLE

Set based on hash-map (collision resolution: open address, link)

## GROUP NAME AND LIST OF GROUP MEMBERS

Group Name: **ASAP**.

Members:

- Chen Ben
  - ID:202320054
  - Email:374733147@qq.com
- Wang Xiaoyan
  - ID: s202320084
  - Email: xiaoyan.wang@hdu.edu.cn

## LABORATORY WORK NUMBER: 5

## VARIANT DESCRIPTION

1. Set based on hash-map (collision resolution: open address, link)

   - You can use the built-in list for storing buckets and a bucket itself

   - You need to check that your implementation correctly works with None value

   - A user should specify growing factor

     The growth factor is all about efficient memory usage and performance. How it works:

     (a) You have a chunk of memory. The chunk has a capacity (how many elements it can contain) and length (how many elements it contains right now).

     (b) You need to add a new element, but capacity == length. You don’t have space for a new element. What will we need to do?

     1. Allocateanewchunkofmemory(inPython,usually,it looks like [None]*(capacity * growth_factor)).
     2. Copy data from the old chunk to the new chunk.
     3. Add a new element to the new chunk.

## SYNOPSIS

Design two versions of list based hashMap(mutable and immutable), and implement several methods(add, remove, map, reduce filter etc.)

## CONTRIBUTION SUMMARY FOR EACH GROUP MEMBER

Chen ben:

- design and implement the mutable version;
- Test the mutable version；

Wang Xiaoyan:

- Design and implement the inmutable version;
- Test the inmutable version;

## EXPLANATION OF TAKEN DESIGN DECISIONS AND ANALYSIS

We implement a Class to represent HashMap, which has property of `data` and `size`;

When we `new` a HashMap, it may has a `size` or not, so in the constructor, we set the  `size` to 0 by default; And allocate memory using method `allocate_memory`. And when allocate new memory, we have to rehash all the values.

When `add` a new value into HashMap, we need to do `%` to get a location for the value. And if collision happens, we use open address strategy: find a `None` from the location until end of list. If we can not find a empty loaction, we need to allocate new memory and do `add` again.

When `remove` a value, we do hash to find a start position and search the value tail the end of list. Return `True` if we get the value and turn it to None, return `False` if not find.

Logic of `find` method is similar to `remove`.

The `size` method, we just return the `len` property of HashMap.

As to `filter` \ `map` \ `reduce`, method:

- `filter`, we find all the values in HashMap which match the condition, and return the list formed by those values;
- `map`, we process every values using a given function, and return the list fromed by the return values of the function;
- `reduce`, we provide a initial value and process every values in HashMap with it, and return one value;

As for inmutable version, we implement the methods by the same logic, but into individual function, the main difference is the methods take one more argument - the HashMap instance that we want to manipulate.

## WORK DEMONSTRATION

For details, see the comments in mutable.py.

## CONCLUSION

For this lab, we have implement the hashMap and deal with collision by open address strategy.

And we also learn how to collerbrate with each other by git and GitHub.