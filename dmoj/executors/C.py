from .GCCExecutor import GCCExecutor


class Executor(GCCExecutor):
    command = 'gcc'
    command_paths = ['gcc']
    flags = ['-std=c99']
    ext = '.c'
    name = 'C'
    test_program = '''
#include <stdio.h>

int main() {
    int ch;
    while ((ch = getchar()) != EOF)
        putchar(ch);
    return 0;
}
'''
