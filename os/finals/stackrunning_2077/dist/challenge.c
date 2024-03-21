#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int setup() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

int secret() {
    printf("You have reached the data core!\n");
    system("cat flag.txt");
}

int stackrunner() {
    char watchdog[0x10] = "CHhMf9iW0F21LC74";
    char verify[0x10] = "QoSgWIl8RPOA5gi6";
    char checker[0x10] = "OWEa8iZOfQIFQyl1";
    char mark2[0x10] = "d4IuSl9wYiqxeUMh";
    char password[0x10] = "QoSgWIl8RPOA5gi6";
    char mark[0x10] = "d4IuSl9wYiqxeUMh";
    char input[0x10];

    printf("\033[0;93mEntering hackbash secure space...\n\n\n");
    sleep(1);

    printf("██╗░░██╗░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░░██████╗██╗░░██╗  ░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗\n");
    printf("██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔════╝██║░░██║  ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝\n");
    printf("███████║███████║██║░░╚═╝█████═╝░██████╦╝███████║╚█████╗░███████║  ╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░\n");
    printf("██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══██╗██╔══██║░╚═══██╗██╔══██║  ░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░\n");
    printf("██║░░██║██║░░██║╚█████╔╝██║░╚██╗██████╦╝██║░░██║██████╔╝██║░░██║  ██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗\n");
    printf("╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝\n\n");
    printf("░██████╗██████╗░░█████╗░░█████╗░███████╗\n");
    printf("██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝\n");
    printf("╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░\n");
    printf("░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░\n");
    printf("██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗\n");
    printf("╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝\n");

    printf("\n\n\033[0;39mPlease enter your input: ");
    gets(input);

    printf("\nVerifying...\n");
    if (strncmp(input, password, 16)) {
        printf("\033[0;31mPassword is wrong, stackrunning failed.\033[0;39m\n");
        exit(1);
    }

    if (strncmp(mark, mark2, 16)) {
        printf("\033[0;31mMark verification failed, stackrunning failed.\033[0;39m\n");
        exit(1);
    }

    if (strncmp(checker, "OWEa8iZOfQIFQyl1", 16)) {
        printf("\033[0;31mIntrusion detected, stackrunning failed.\033[0;39m\n");
        exit(1);
    }

    if (strncmp(watchdog, "CHhMf9iW0F21LC74", 16)) {
        printf("\033[0;31mWatchdog alerted, stackrunning failed.\033[0;39m\n");
        exit(1);
    }

    if (strncmp(verify, password, 16)) {
        printf("\033[0;31mPassword modified, stackrunning failed.\033[0;39m\n");
        exit(1);
    }

    printf("\nVerification complete. User does not have access to requested file.\n");
    printf("Exiting...\n");
}

int main() {
    setup();
    stackrunner();
}