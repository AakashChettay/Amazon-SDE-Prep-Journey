```
/*
Definition of singly linked list:
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int data1)
    {
        val = data1;
        next = NULL;
    }
    ListNode(int data1, ListNode *next1)
    {
        val = data1;
        next = next1;
    }
};
*/

class Solution {
public:
    ListNode* insertAtTail(ListNode* &head, int X) {
        ListNode* tailNode = new ListNode(X);
        if(head == nullptr)
            return tailNode;
        ListNode* temp = head;
        while(temp != nullptr)
        {
            if(temp->next == nullptr)
            {
                temp->next = tailNode;
                return head;
            }
            temp = temp->next;
        }
    }
};
```