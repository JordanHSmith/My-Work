/*
Jordan Smith
part_1_task_4.yy
09/25/23
Parser for Clite
*/


%{
#include <stdio.h>
%}

%option noyywrap

%%
//check for digit
[0-9]+ {
    printf("Integer-%s\n", yytext);
}

//check for float
[0-9]+"."[0-9]+ {
    printf("Float-%s\n", yytext);
}

//check for keyword
if|else|while|for|int|float {
    printf("Keyword-%s\n", yytext);
}

//check for idnentifier
[a-zA-Z_][a-zA-Z0-9_]* {
    printf("Identifier-%s\n", yytext);
}

//check for assingment statement
"=" {
    printf("Assignment\n");
}

//check for comparison operator
"=="|"<"|">"|"<="|">=" {
    printf("Comparison-%s\n", yytext);
}

//check for mathemeical operator
"\\+"|"-"|\\*|"/" {
    printf("Operator-%s\n", yytext);
}

"{" {
    printf("Open-bracket\n");
}

"}" {
    printf("Close-bracket\n");
}

//check for open parenthesis
"\(" {
    printf("Open-paren\n");
}

//check for close parenthesis
"\)" {
    printf("Close-paren\n");
}

//check for new line; prints nothing
"\n" {

}

. {
    //Ignore and skip other characters.
}

%%
int main(int argc, char* argv[]) {
    //reading in file
    if (argc > 1)
        yyin = fopen( argv[1], "r" ); //where yylex reads its input 

    yylex();
    return 0;
}
