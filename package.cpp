#include <iostream>
#include <fstream>

using namespace std;


void readFile()
{
    ifstream file;
    file.open ("cases.txt");
    string word;
    char x ;
    word.clear();

    while ( file >> word )
    {
        x = file.get();

        if(file.eof())
            break;

        while ( x != ' ' )
        {
            word = word + x;
            x = file.get();
        }

            cout<< word <<endl;
            word.clear();

    }
}

int main()
{
    readFile();
    return 0;
}