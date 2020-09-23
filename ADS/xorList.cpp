#include <bits/stdc++.h>
#include <inttypes.h>

class Node{
    public:
    int data;
    Node *link;
}


//xor of previous and next nodes
Node* XOR(Node *a, Node *b)  
{  
    return (Node*) ((uintptr_t) (a) ^ (uintptr_t) (b));  
} 

//insert at the beginning
void push(Node **head, int data){
    Node *new_node = new Node(),
    new_node->data = data;
    new_node->link = *head;

    if (*head != NULL){
        (*head)->link = XOR(new_node, *head);
    }

    *head = new_node;
}

//insert at the end
void insert_end(Node **head, int data){
    Node *next=NULL, *prev=NULL, *curr=*head;
    Node *new_node = new Node(),
    new_node->data = data;
    new_node->link = *head;
    if(*head==NULL){
        *head = new_node;
    }
    else{
        while(curr->link != NULL){
            
        }
    }
}

int main(){
    Node *head;
    push(&head, 3);
    push(&head, 4);
    push(&head, 5);

}