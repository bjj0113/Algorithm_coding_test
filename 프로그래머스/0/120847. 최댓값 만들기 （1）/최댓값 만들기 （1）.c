#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int max =0;
    int max2 =0;
    int cnt;
    for(int i=0; i<numbers_len;i++)
    {
        if(max<numbers[i]){
            max = numbers[i];
            cnt =i;
        }
    }
    for(int i=0; i<numbers_len;i++)
    {
        if(max2<numbers[i] && i != cnt)
            max2 = numbers[i];
    }
    answer= max* max2;
    return answer;
}