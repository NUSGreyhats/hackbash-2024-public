#include <stdio.h>
#include <string.h>

int main() {
        char status[8];
        char input[8];

        strcpy(status, "lose");

        scanf("%20s", input);
        printf("You %s!\n", status);
}

