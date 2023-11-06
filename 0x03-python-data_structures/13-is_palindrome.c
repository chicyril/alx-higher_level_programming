#include "lists.h"

/**
 * list_reverse - Reverse a linked list
 * @head: address of the pointer to the first node of the list
 */
void list_reverse(listint_t **head)
{
	listint_t *switcher = *head, *tail = NULL;

	while (*head)
	{
		*head = (*head)->next;
		switcher->next = tail;
		tail = switcher;
		switcher = *head;
	}
	*head = tail;
}

/**
 * is_palindrome - checks whether a list is a palindrome
 * @head: address of the pointer to the list
 *
 * Return: 1 if it's a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = NULL, *mid = NULL, *slow = NULL;
	listint_t *half = NULL, *temp = NULL, *hdup = NULL;
	int ispalin = 1;

	if (*head && (*head)->next)
	{
		fast = mid = *head;
		while (fast->next)
		{
			fast = fast->next->next;
			if (!fast)
				break;
			slow = mid;
			mid = mid->next;
		}
		half = mid->next;
		if (!fast)
			slow = mid;
		slow->next = NULL;
		list_reverse(&half);
		temp = half;
		hdup = *head;
		while (hdup && temp)
		{
			if (!hdup || !temp)
				break;
			if (hdup->n != temp->n)
			{
				ispalin = 0;
				break;
			}
			hdup = hdup->next;
			temp = temp->next;
		}
		list_reverse(&half);
		mid->next = half;
		if (slow != mid)
			slow->next = mid;
	}
	return (ispalin);
}
