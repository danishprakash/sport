#include <stdio.h>
#include <ctype.h>
#include <malloc.h>
#include <string.h>
typedef struct node * nptr;

char ch[100];


struct node{
    char ch;
    nptr next;
};

nptr op_top = NULL;
nptr out_top = NULL;

void out_push(char);
void op_push(char);
char op_pop();
void calculate();
void display();


int main()
{
    gets(ch);
    //reverse(s);
    calculate();
    display();
    return 1;
}

void reverse(char str[])
{

    int j=strlen(str)-1;
    int i=0;
    char temp;
    while(i<j)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }

}


int priority(char ch)
{
    switch(ch){
        case '^':
            return 3;

        case '*':
            return 2;

        case '/':
            return 2;

        case '+':
            return 1;

        case '-':
            return 1;

        default:
            return 0;
    }
}

void calculate()
{
    int i=0;

    while(ch[i] != '\0')
    {
        if(isalpha(ch[i]))
            out_push(ch[i]);
        else if(ch[i] == '(')
            op_push(ch[i]);
        else
        {
            if(op_top == NULL)
                op_push(ch[i]);

            else if(ch[i] == ')')
            {
                while(op_top->ch != '(')
                    out_push(op_pop());
                op_pop();
            }

            else
            {
                while (op_top != NULL && priority(ch[i]) <= priority(op_top->ch))
                {
                    out_push(op_pop());
                }
                op_push(ch[i]);
            }
        }
        i++;
    }

    nptr temp1 = op_top;
    while(temp1 != NULL)
    {
        out_push(op_pop());
        temp1=temp1->next;
    }
}

void out_push(char a)
{
    nptr newnode = (nptr)malloc(sizeof(nptr));
    newnode->next=NULL;
    newnode->ch=a;

    if(out_top == NULL)
        out_top = newnode;
    else
    {
        newnode->next=out_top;
        out_top=newnode;
    }
}

void op_push(char a)
{
    nptr newnode = (nptr)malloc(sizeof(nptr));
    newnode->next=NULL;
    newnode->ch=a;

    if(op_top == NULL)
        op_top = newnode;
    else
    {
        newnode->next=op_top;
        op_top=newnode;
    }
}


char op_pop()
{
    char x;
    if(op_top == NULL)
        printf("Underflow!\n");
    else
    {
        x = op_top->ch;
        op_top = op_top->next;
    }
    return x;
}

void display()
{
    nptr temp = out_top;
    char a[100] = {0};
    int i = 0;
    while(temp != NULL)
    {
        a[i] = temp->ch;
        temp = temp->next;
        i++;
    }
    reverse(a);
    printf("%s", a);
}

