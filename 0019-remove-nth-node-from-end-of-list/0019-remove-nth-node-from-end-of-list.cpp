class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        int length = 0;
        ListNode* temp = head;
        while (temp) {
            length++;
            temp = temp->next;
        }
        
        int position = length - n;
        ListNode* prev = dummy;
        
        for (int i = 0; i < position; i++) {
            prev = prev->next;
        }
        
        ListNode* toDelete = prev->next;
        prev->next = prev->next->next;
        
        delete toDelete;
        
        ListNode* result = dummy->next;
        delete dummy;
        
        return result;
    }
};