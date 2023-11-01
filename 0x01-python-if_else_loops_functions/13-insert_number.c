#include "lists.h"
/**
 * insert_node - insert a node in a sorted linked list
 * @head: address of the pointer to the first node
 * @number: int value for the inserted node
 *
 * Return: the address of the inserted node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insrtnode = NULL, *traverser = NULL;

	insrtnode = malloc(sizeof(listint_t));
	if (!insrtnode)
		return (NULL);
	insrtnode->n = number;
	insrtnode->next = NULL;
	if (!(*head) || (*head)->n >= number)
	{
		insrtnode->next = *head;
		*head = insrtnode;
	}
	else
	{
		traverser = *head;
		while (traverser->next)
		{
			if (number <= traverser->next->n)
				break;
			traverser = traverser->next;
		}
		insrtnode->next = traverser->next;
		traverser->next = insrtnode;
	}
	return (insrtnode);
}
