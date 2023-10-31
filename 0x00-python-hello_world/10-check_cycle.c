#include "lists.h"
/**
 * check_cycle - Use Floyd's hare and tortoise algo to check for loop in a list
 * @list: the list to check
 *
 * Return: 0 if no loop is found else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *advance = list;
	listint_t *trail = list;

	while (trail && advance && advance->next)
	{
		trail = trail->next;
		advance = advance->next->next;
		if (advance == trail)
			return (1);
	}
	return (0);
}
