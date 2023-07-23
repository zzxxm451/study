#include <stdio.h>
#include <string.h>

char a[10005], b[10005];

int main() {
    scanf("%s%s", a, b);
    int la = strlen(a), lb = strlen(b);
    int i = la - 1, j = lb - 1, carry = 0; // carry 表示进位
    char c[10005] = {0};
    int k = 0;
    while (i >= 0 || j >= 0 || carry) {
        int x = i >= 0 ? a[i--] - '0' : 0;
        int y = j >= 0 ? b[j--] - '0' : 0;
        int sum = x + y + carry;
        c[k++] = sum % 10 + '0';
        carry = sum / 10;
    }
    for (int i = k - 1; i >= 0; --i)
        printf("%c", c[i]);
    printf("\n");
    return 0;
}
/*
给你两个正整数A，B，计算A+B

输入格式:
第一行一个正整数A
第二行一个正整数B

数据范围：
1<=A,B<=10 
10000
*/
