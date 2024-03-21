#include <stdio.h>
#include <stdlib.h>

int win() {
    printf("Good job :)\n");
    system("cat flag.txt");
    return 0;
}

int main() {
    char name[0x10];
    //fix buffer for remote
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    printf("Is this stack overflow?\n");
    printf("Enter username:\n");
    fgets(name, 0x20, stdin);
    printf("Access denied >:(\n");
    return 0;
}