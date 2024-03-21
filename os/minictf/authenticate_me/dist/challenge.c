#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void setup() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
}

void win() {
	system("/bin/sh");
}

void vuln() {

	char input[32] = "";
	char password[32] = "sup3r_s3cr37_s3cur3_p@ssw0rd_:))";
	char status[32] = "user";

	// prompt and get input
	printf("Enter your password: ");
	scanf("%72s", input);

	// check if input == password
	if (!strncmp(input, password, 32)) {

		// check if status == "sudo"
		if (!strncmp(status, "sudo", 4)) {
			win();
		} else {
			printf("You got the password, but you are only a %s.\n", status);
		}

	} else {
		printf("Wrong password!\n");
	}
}

int main() {

	// you may ignore this setup function.
	// it is not relevant to the challenge.
	setup();
	vuln();
}
