for demonstration in class

```
---------------------
|  char buffer[8]   |   <-- 8 bytes
---------------------
|     saved RBP     |   <-- + 8 bytes
---------------------
|   return address  |   <-- + p64(unreachable) # 64-bit little endian packing
---------------------
```
