```
/*
Definition of doubly linked list:
struct ListNode
{
    int val;
    ListNode *next;
    ListNode *prev;
    ListNode()
    {
        val = 0;
        next = NULL;
        prev = NULL;
    }
    ListNode(int data1)
    {
        val = data1;
        next = NULL;
        prev = NULL;
    }
    ListNode(int data1, ListNode *next1, ListNode *prev1)
    {
        val = data1;
        next = next1;
        prev = prev1;
    }
};
*/

class Solution {
public:
    ListNode* deleteTail(ListNode* head) {
        if(head->next == nullptr)
        {
            delete head;
            return nullptr;
        }
        ListNode* temp = head;
        while(temp!=nullptr)
        {
            if(temp->next->next == nullptr)
            {
                delete temp->next;
                temp->next = nullptr;
                break;
            }
            temp = temp->next;
        }
        return head;
    }
};
```