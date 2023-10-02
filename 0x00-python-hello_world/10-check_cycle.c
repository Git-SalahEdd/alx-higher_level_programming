#include "lists.h"

/**
*main - Entry point
*Return: always 0 (success)
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		return (1);
	}
	return (0);
}
