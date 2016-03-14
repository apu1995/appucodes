#include <stdio.h>

long long int numPaths=0;

void moveRobot(int row, int column, int field[4][4]);
void moveRobotUp(int row, int column, int field[4][4]);
void moveRobotDown(int row, int column, int field[4][4]);
void moveRobotLeft(int row, int column, int field[4][4]);
void moveRobotRight(int row, int column, int field[4][4]);

void main()
{
	int field[4][4],i,j;
	for (i = 0; i < 4; i++)
	{
	    for (j = 0; j < 4; j++)
	    {
	        field[i][j] = 0;
	    }
	}
	field[0][0] = 1;
	moveRobot(0, 0, field);
	printf("%lld\n",numPaths);
}

void moveRobot(int row, int column, int field[4][4])
{
    moveRobotUp(row, column, field);
    moveRobotDown(row, column, field);
    moveRobotLeft(row, column, field);
    moveRobotRight(row, column, field);
}

void moveRobotUp(int row, int column, int field[4][4])
{
    if (row == 0) return;
    else 
    {
        if (field[row-1][column] == 1) return;
        field[row-1][column] = 1;
        moveRobot(row-1, column, field);
        field[row-1][column] = 0;
    }
}

void moveRobotDown(int row, int column, int field[4][4])
{
    if (row == 3 && column == 3) 
    {
        numPaths++;
        return;
    }
    else if (row == 3) return;
    else
    {
        if (field[row+1][column] == 1) return;
        field[row+1][column] = 1;
        moveRobot(row+1, column, field);
        field[row+1][column] = 0;
    }
}

void moveRobotLeft(int row, int column, int field[4][4])
{
    if (column == 0) return;
    else
    {
        if (field[row][column-1] == 1) return;
        field[row][column-1] = 1;
        moveRobot(row, column-1, field);
        field[row][column-1] = 0;
    }
}

void moveRobotRight(int row, int column, int field[4][4])
{
    if (column == 3 && row == 3) 
    {
        numPaths++;
        return;
    }
    else if (column == 3) return;
    else 
    {
        if (field[row][column+1] == 1) return;
        field[row][column+1] = 1;
        moveRobot(row, column+1, field);
        field[row][column+1] = 0;
    }
}