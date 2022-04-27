#include "lists.h"

int check_cycle(listint_t *head)
{
	listint_t *current, *forward;

	current = head;
	forward = head;

	while(current != NULL && forward != NULL && forward->next != NULL)
	{
		current = current->next;
		forward = forward->next->next;
		if (current == forward)
		{
			return (1);
		}
	}

	return (0);
}
