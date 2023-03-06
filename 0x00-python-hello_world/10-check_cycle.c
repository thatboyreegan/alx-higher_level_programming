#include "lists.h"

/**
 * check_cycle - function that cjhecks for a cycle in a singly linked list.
 * @list: to be checked.
 * Return: 0 if no cycle and 1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
