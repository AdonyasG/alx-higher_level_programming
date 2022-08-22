#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * check_cycle - checks if the list is circular or not
 * @list: head
 * Return: 0 if non cyclic, 1 if it is
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
