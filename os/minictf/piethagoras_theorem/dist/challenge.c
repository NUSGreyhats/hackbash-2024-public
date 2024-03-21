#include <stdio.h>

void setup() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
}

void win() {
	execve("/bin/sh", 0, 0);
}

void get_feedback() {
	char feedback[0x100];
	printf("What do you think of our PI-predicting machine?");
	scanf("%s", feedback);
}

int main() {

	setup();
	printf("Let me tell you what PI is. PI is 3.14159%lld.\nDo with that whatever you want.", main);
	get_feedback();

}
