#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
    listint_t * temp = *head;
    int size = 0;
    int i = 0;
    int flag = 0;
    int * array_end;
    while (temp != NULL)
    {
        size++;
        temp = temp->next;
    }
    array_end = calloc(size, sizeof(int));

    while (*head != NULL)
    {
        temp = *head;
        array_end[i] = (*head)->n;
        *head = (*head)->next;
        free(temp);
    }
    for (int j = 0; j < size/2 && size != 0; j++)
    {
        if (array_end[j] != array_end[size - i - 1])
        {
            flag = 1;
            break;
        }
    }
    free(array_end);
    return (flag);
}