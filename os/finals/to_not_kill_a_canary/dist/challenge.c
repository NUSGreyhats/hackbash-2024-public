#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int setup() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

int escape() {
    printf("My canary has escaped!\n");
    system("cat flag.txt");
}

int pet() {
    printf("You pet the canary :)\n");
    printf("\n\n\n\n");
    cage();
}

int talk() {
    char input[0x10];
    char password[0x10] = "bPfrUbTRktkGWjA";

    printf("What do you want to say?\n");
    fgets(input, 0x30, stdin);
    if (!strncmp(input, password, 16)) {
        printf("Here's the canary!\n");
        printf("%11$p");
    } else {
        printf("The canary echoes back what you said:\n%s\n", input);
    }
    printf("\n\n\n\n");
    cage();
}

int poison() {
    char input[0x10];

    printf("Input your poison:\n");
    gets(input);
}

int cage() {
    char input[4];
    int choice;
    printf("\033[0;33m");
    printf("▀█▀ █▀█  \033[0;31m ▄▀ █▄░█ █▀█ ▀█▀ ▀▄ \033[0;33m  █▄▀ █ █░░ █░░   ▄▀█   █▀▀ ▄▀█ █▄░█ ▄▀█ █▀█ █▄█\n");
    printf("░█░ █▄█  \033[0;31m ▀▄ █░▀█ █▄█ ░█░ ▄▀ \033[0;33m  █░█ █ █▄▄ █▄▄   █▀█   █▄▄ █▀█ █░▀█ █▀█ █▀▄ ░█░\n");
    printf("\n");
    printf("\033[1;36mDid you know? Canaries were used in history\n");
    printf("as an early warning for toxic gases, as the birds are\n");
    printf("sensitive to toxic gases! Here is my pet canary...\n");
    printf("\n");
    //printf("\033[0;32m");
    printf("--------------------------------\n");
    printf("|                              |\n");
    printf("|    What do you want to do?   |\n");
    printf("|      1. Talk to canary       |\n");
    printf("|      2. Pet the canary       |\n");
    printf("|      3. Test for poison!     |\n");
    printf("|                              |\n");
    printf("--------------------------------\n");
    printf("Option: ");
    fgets(input, 4, stdin);
    choice = atoi(input);
    switch (choice) {
        case 1:
            talk();
            break;
        case 2:
            pet();
            break;
        case 3:
            poison();
            break;
        default:
            printf("\nInvalid choice!\n");
            cage();
    }
}

int main() {
    setup();
    cage();
}