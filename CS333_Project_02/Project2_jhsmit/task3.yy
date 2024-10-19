/*
Jordan Smith
task3.yy
09/25/23
Strips HTML of symbols
*/

%{
#include <stdio.h>
%}

%%
"<"([^>]*)">"        ; /* Remove HTML tags*/
"\t"            ; /* Remove extraneous whitespace */
"\n\n"            ; /* Replace consecutive newlines with a single newline */
"\n+"            ; /* Replace multiple consecutive newlines with a single newline */
%%

int main(int argc, char* argv[]) {
    //reading in file
    if (argc > 1)
        yyin = fopen( argv[1], "r" );

    yylex();

    return 0;
}
