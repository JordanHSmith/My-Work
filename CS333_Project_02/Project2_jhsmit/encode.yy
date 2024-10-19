/*
Jordan Smith
encode.yy
09/25/23
Shifts letter of the alphabet 13 spaces forward (with wraparound)
*/

%{
#include <stdio.h>
%}

%%
[a-zA-Z] { //checks for any letter
    int newChar = (int)yytext[0] + 13;  // Shift the character by 13 positions
    //Checks for wraparound
    if (yytext[0] >= 'a' && yytext[0] <= 'z' && newChar > 'z') {
        newChar -= 26;
    } else if (yytext[0] >= 'A' && yytext[0] <= 'Z' && newChar > 'Z') {
        newChar -= 26;
    }
    printf("%c", newChar );
}

%%
int main() {
    yylex();
    return 0;
}
