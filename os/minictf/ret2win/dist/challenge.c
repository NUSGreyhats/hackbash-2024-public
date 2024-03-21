#include <stdio.h>
#include <stdlib.h>

void win() {
	execve("/bin/sh", 0, 0);
}

void setup() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
}

int main() {

	char input[0x20];

	setup();
	printf("Your first ret2win! Let's give it a go\n");
	scanf("%s", input);
}
