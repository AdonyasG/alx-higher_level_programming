#include "lists.h"
#include <stdlib.h>
/**
*insert_node - insert node at index where number
*@head: head of the list
*@number: number
*Return: NULL if failed or head list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp, *new;
new = *head;
temp = malloc(sizeof(listint_t));
if (temp == NULL)
return (NULL);
temp->n = number;
temp->next = NULL;
if (*head == NULL)
*head = temp;
else
{
while (new->next != NULL)
{
if (number < new->n || number < new->next->n)
break;
new = new->next;
}

if (*head == new)
	{
	  temp->next = new;
	  *head = temp;
	return (*head);
	}
temp->next = new->next;
new->next = temp;
}
return (*head);
}
