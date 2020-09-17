#include <bits/stdc++.h>
using namespace std;

class node{
    public:
    int data;
    node* next;
};

void push(node**head, int data){
    node* newNode = new node();
    newNode->data = data;
    newNode->next= (*head);
    (*head) = newNode;
    return;
}

void append(node**head, int data){
    node* newNode = new node();
    node* last= *head;
    newNode->data = data;
    newNode->next = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    while(last->next != NULL){
        last = last->next;
    }
    last->next=newNode;
    return;
}

void insertAfter(node**head, int data, int pos){
    node* newNode = new node();
    node* prev = NULL; 
    node* curr = *head;
    int count=0;
    newNode->data = data;
    while(count<pos){
        prev = curr;
        curr = curr->next;
        count+=1;
    }
    prev->next = newNode;
    newNode->next = curr;
    return;
}

void printList(node* n){
    while(n!=NULL){
        cout<<n->data<<' ';
        n=n->next;
    }
}

int main(){
    node* head = NULL;
    int ch, data, pos;
    while(1){
        cout<<endl<<"Enter your choice 1.push 2.append 3.insert after 4.print 5.exit"<<endl;
        cin>>ch;
        switch(ch){
            case 1: cout<<"Enter data to be pushed"<<endl;
                    cin>>data;
                    push(&head, data);
                    break;

            case 2: cout<<"Enter data to be appended"<<endl;
                    cin>>data;
                    append(&head, data);
                    break;
            
            case 3: cout<<"Enter data and position to be inserted after"<<endl;
                    cin>>data>>pos;
                    insertAfter(&head, data, pos);
                    break;
            
            case 4: cout<<"The elements in the list are"<<endl;
                    printList(head);
                    break;

            case 5: exit(0);
        }
    }
    
    return 0;
}