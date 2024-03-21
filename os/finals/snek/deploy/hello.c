// just gcc hello.c -o hello
int main()
{
   setuid( 0 );
   system( "/home/player/.hello.py" );

   return 0;
}