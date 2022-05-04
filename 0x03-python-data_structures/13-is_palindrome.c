#include "lists.h"
#include "stdio.h"
#include "stdlib.h"

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *ptr;
	int size, i, j;

	if (head == NULL || tmp == NULL)
	{
		return (1);
	}

	for (size = 0; tmp != NULL; size++)
	{
		tmp = tmp->next;
	}

	if (size % 2 != 0)
	{
		return (0);
	}

	ptr = malloc(sizeof(int) * (size / 2));
	if (ptr == NULL)
	{
		return (0);
	}

	printf("\nSize: {%d}\n", size);
	return (0);
}
