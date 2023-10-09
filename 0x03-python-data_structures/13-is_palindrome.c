#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome.
 *@head: head of the list to check
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t  *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next_node;
	listint_t  *first_half = *head, *second_half = NULL;

	if (!*head || !(*head)->next) 
	{
		return (1);
	}
	if (!(*head)->n || !(*head)->next->n)
	{
		return (0);
	}
	while (fast && fast->next)
	{
	 slow = slow->next;
	 fast = fast->next->next;
	}
	while (slow)
	{
		next_node = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_node;
	}
	while (first_half && second_half)
	{
		if (first_half->n == second_half->n)
		{
			return (1);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (0);
}
