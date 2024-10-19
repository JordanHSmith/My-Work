/*
Jordan Smith
replace.yy
09/25/23
Hello World program
*/

%%

blah    printf("hello world");

%%

int main ( int argc, char *argv[] ) {

	yylex();

	return 0;

}