#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char **argv)
{
    for (int i =0; i<argc; i++) {cout << argv[i] << endl; }
    if (strcmp(argv[0], "ls") == 0)
    {
        cout << "Do work of ls \n";
    }
    else if (strcmp(argv[0], "cd") == 0)
    {
        cout << "Do work of cd \n";
    }
    else cout << "This is a very usefule tool\n";
    return 0;
}