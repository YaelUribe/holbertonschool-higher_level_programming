#include "lists.h"
/**
 * check_cycle - function to check cycles
 * @list: Singly linked list to check
 * Return: 0 if no cycle 1 if there are cycle(s)
 */
int check_cycle(listint_t *list)
{
	listint_t *copya = list, *copyb = list;
	int check_cycle = 0;

	if (!list)
		return (check_cycle);
	while (copyb != NULL && copyb->next != NULL)
	{
		copya = copya->next;
		copyb = copyb->next->next;
		if (copya == copyb)
		{
			check_cycle = 1;
			return (check_cycle);
		}
	}
	return (check_cycle);
}
