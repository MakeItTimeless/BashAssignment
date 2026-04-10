#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];

    printf("Enter some text: ");
    scanf("%s", buffer);   // unsafe input

    printf("You entered: %s\n", buffer);

    return 0;
}

/*
1) What happens with long input?
If the user enters more than 16 characters, it overflows the buffer and overwrites adjacent memory.

2) Why is this dangerous?
It can crash the program or allow attackers to execute malicious code.

3) How to fix it?
Use safer functions like fgets() or limit input size.
*/
