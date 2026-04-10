#include <stdio.h>

int main() {
    int port = 80;
    int *ptr;

    ptr = &port;

    // Print using variable
    printf("Port value using variable: %d\n", port);

    // Print using pointer
    printf("Port value using pointer: %d\n", *ptr);

    // Change value using pointer
    *ptr = 443;

    printf("Updated port value: %d\n", port);

    return 0;
}
