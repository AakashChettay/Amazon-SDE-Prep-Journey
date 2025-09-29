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
    ListNode* deleteTail(ListNode* &head) {
        ListNode* temp = head;
        if(head->next == nullptr) return nullptr;
        while(temp != nullptr)
        {
            if(temp->next->next == nullptr)
            {
                temp->next = nullptr;
            }
            temp = temp->next;
        }
        return head;
    }
};
```