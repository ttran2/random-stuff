#include <stdlib.h>

/* Declare Structure Node */

// FIY: assume node is an item of an array

/* typedef - let's declare (announce to the compiler) that there'll be */
/* a new type of structure 'Node' called 't_node' (thus t_node = struct node) */

typedef struct node t_node; // tell compiler what 't_node' is

/* Define Structure Node */
typedef struct node { // define t_node how it looks like
	int data; // the actual data stored on the node
	t_node *next; // pointer to the next node
} t_node;

/* Declare & Define Structure List */
typedef struct list {
	t_node *first; // pointer to the first node of the list
	t_node *last; // pointer to the last node of the list
	int size; // size of the list (number of nodes)
} t_list;


/* List Operations */

void list_init(t_list *l)
{
	/* Define stuff */
	l->first = NULL;
	l->last = NULL;
	l->size = 0;
}

int list_empty(t_list *l)
{
	if (l->first == NULL && l->last == NULL)
	{
		return 1;
	}
	return 0;
}

int list_len(t_list *l)
{
	return l->size;
}

void list_push_back(t_list *l, int x)
{
	t_node *n = malloc(sizeof(t_node)); // allocate memory to the new node

	if (list_empty(l))
	{
		l->first = n; // define first node as this new node
	}
	else
	{
		l->last->next = n; // connect current last node to new node
	}

	n->next = NULL; // define next node as nothing

	l->last = n; // define/change the last node pointer to this new node n

	l->size++; // increment the size of the list (since new node has been add)

	n->data = x; // store data x into the node
}

void list_push_front(t_list *l, int x)
{
	t_node *n = malloc(sizeof(t_node)); // allocate memory to the new node
	if (list_empty(l))
	{
		l->last = n; // define last node as this new node
		n->next = NULL; // there is no next node
	}
	else
	{
		n->next = l->first; // define next node as the current first node
	}
	l->first = n; // define/change the first node pointer to this new node n

	l->size++; // increment the size of the list (since new node has been add)

	n->data = x; // store data x into the node
}

int list_pop_back(t_list *l)
{
	return 0;
}

int list_pop_front(t_list *l)
{
	return 0;
}

void list_clear(t_list *l)
{
	t_node *next_node, *i;
	for (i = l->first; i != NULL; i = next_node) // loop through the list
	{
		next_node = i->next; // store next node address into next_node
		free(i); // free the current node
	}
	list_init(l); // reset the list into the initial state
}

/* Main Function */

int main(void)
{
	t_list l;
	list_init(&l);
	list_push_front(&l, 12);
	list_push_front(&l, 10);
	list_clear(&l);
	return 0;
}
