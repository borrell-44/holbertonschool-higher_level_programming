#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *last;

	current = *head;
	last = *head;

	if (head == NULL)
	{
		return (NULL);
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	while (current->next != NULL)
	{
		if (number < current->n)
		{
			new->next = current;
			last->next = new;
			return (new);
		}
		last = current;
		current = current->next;
	}

	current->next = new;
	new->next = NULL;
	return (new);
}

