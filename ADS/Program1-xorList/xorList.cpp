#include <bits/stdc++.h>
#include <inttypes.h>
using namespace std;

class Node{
    public:
    int data;
    Node *link;
};


//xor of previous and next nodes
Node* XOR(Node *a, Node *b)  
{  
    return (Node*) ((uintptr_t) (a) ^ (uintptr_t) (b));  
} 

//insert at the beginning
void push(Node **head, int data){
    Node *new_node = new Node();
    new_node->data = data;
    new_node->link = *head;

    if (*head != NULL){
        (*head)->link = XOR(new_node, (*head)->link);
    }

    *head = new_node;
}

void insert_end(Node **head, int data){
    Node *next;
    Node *curr=*head;
    Node *prev=NULL;

    Node *new_node = new Node();
    new_node->data = data;

    //if there are no elements
    if(curr == NULL){
        new_node->link = *head;
        *head = new_node;
        return;
    }

    while (curr != NULL)
    {
        next = XOR(prev, curr->link);
        prev=curr;
        curr=next;
    }
    prev->link = XOR(prev->link, new_node);
    new_node->link = XOR(NULL, prev);
}

void printList(Node *head){
    Node *curr = head;
    Node *prev = NULL;
    Node *next;
    while(curr != NULL){
        cout<<curr->data<<" ";
        next = XOR(prev, curr->link);
        prev = curr;
        curr = next;
    }
} 


int main(){
    Node *head=NULL;
    insert_end(&head, 60);
    push(&head, 10);
    push(&head, 20);
    push(&head, 30);
    push(&head, 40);
    push(&head, 50);
    printList(head);

    return (0);
}
