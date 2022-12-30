# Hacking The Virtual Memory

This repository contains code used to change data in the virtual memory of a process at runtime.

## replace_heap

This file replaces a single occurrence of a string (`search_string`) in the heap of a process identified by it's ID (`pid`) with another string (`replace_string`).

#### USAGE

```bash
./replace_heap.py pid search_string replace_string
```

## replace_stack

This file replaces a single occurrence of a string (`search_string`) in the stack of a process identified by it's ID (`pid`) with another string (`replace_string`).

#### USAGE

```bash
./replace_heap.py pid search_string replace_string
```


