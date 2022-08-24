int squarerootfinder(int number,int divisor)
{
    if(divisor ==1){
        return 1;
    }
    else{
        if((number / (divisor * divisor))%1 !=0){
            divisor = squarerootfinder(number, divisor -1);
        }
        if((number/ (divisor * divisor)) %1 ==0 ){
            return divisor;
        }
    }
}