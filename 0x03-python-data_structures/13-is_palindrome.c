#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 *is_palindrome - checks if a singly linked list is a palindrome.
 *@head: head of the list to check
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *rev_list, *mid_list;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	while (slow)
	{
		size++;
		slow = slow->next;
	}

	slow = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		slow = slow->next;

	if ((size % 2) == 0 && slow->n != slow->next->n)
		return (0);

	slow = slow->next->next;
	rev_list = reverse_listint(&slow);
	mid_list = rev_list;

	slow = *head;
	while (rev_list)
	{
		if (slow->n != rev_list->n)
			return (0);
		slow = slow->next;
		rev_list = rev_list->next;
	}
	reverse_listint(&mid_list);

	return (1);
}
