int main()
{
    int x = 0;
    int z = 1;
    if(x >= 1)
    {
        int y = 0;
    }
    else
    {
        x++;
        x = x+z;
        z += x;
    }
    z++;
    return 0;
}