#include <stdio.h>
#include <unistd.h>

#define CLRSCR "\033[2J\033[H"
#define CIVIS "\033[?25l"
#define CNORM "\033[34h\033[?25h"
#define GRN "\e[1;92m"
#define RST "\e[0m"

char flag[] = "flag{caught_the_flag_before_it_dissipated_into_nothingness_though_i_hope_you_didnt_use_a_screen_recorder_for_this_one}";

int main() {

	setbuf(stdout, 0);
	printf(CLRSCR CIVIS);

	printf(GRN"What was the flag again? Let me try to recall...\n");
	printf("Hmmm...\n");
	usleep(1000000);
	printf("Hmm...\n");
	usleep(1000000);
	printf("Hm...\n");
	usleep(1000000);
	printf(flag);
	printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
	printf("                                                   ");
	usleep(80000);
	printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
	printf("                                                                                                                       ");
	printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
	printf(GRN"It appeared for 0.01 second but I forgot about it again...\nIf only we could *CAPTURE* the moment :(\n");

	printf(CNORM RST);
}
