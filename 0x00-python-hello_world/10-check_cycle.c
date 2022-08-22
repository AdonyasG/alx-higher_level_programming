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
	listint_t *temp;
	listint_t *temp2;

	if (list == NULL)
		return (0);
	temp = list;
	temp2 = list;

	while (temp2->next != NULL && temp2->next->next != NULL)
	{
		temp = temp->next;
		temp2 = temp2->next->next;
		if (temp == temp2)
		{
			temp = list;
			while (temp != temp2)
			{
				temp = temp->next;
				temp2 = temp->next;
			}
			return (1);
		}
	}
	return (0);
}
