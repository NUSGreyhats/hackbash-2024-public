#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// don't need to care about how this function works
// all you need to know is that this is the win function/the objective
void get_flag() {

	char flag[0x100];
	puts("You made it.");
	FILE* f = fopen("flag.txt", "r");
	if (f == NULL) {
		printf("An error has occurred. Contact an admin for help.");
		exit(-1);
	}
	flag[fread(flag, 0x1, 0x100, f)] = 0;
	fclose(f);

	puts(flag);
	exit(0);
}

void vuln() {
	char input[0x1000];

	// if we receive a SIGSEGV signal, we call the get_flag function
	signal(SIGSEGV, get_flag);

	puts("Give it your all. Scream all you can!");
	gets(input);
}

void setup() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
}

int main() {

	setup(); // ignore the setup
	vuln();
	puts("Almost there. Try harder!");
	return 0;
}
