/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class SwapPairs {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL) {
            return NULL;
        } else if (head->next == NULL) {
            return head;
        }
        
        ListNode *node = head;
        ListNode *ans = head->next;
        ListNode *prev = NULL;
        
        // A -> B -> C 
        while (node != NULL) {            
            // temp is B
            ListNode *temp = node->next;
            
            // Node is A
            // A need to point to C  
            if (node->next != NULL) {
                node->next = node->next->next;
                
                if (prev != NULL) {
                    prev->next = temp;
                }
                
                // A & B -> C
                // B needs to point to A
                if (temp != NULL) {
                    temp->next = node;
                }
            } else {
                // If the node is the last in the list
                if (prev != NULL) {
                    prev->next = node;
                }
            }
            
            // Now iterate through
            // A is now C
            prev = node;
            node = node->next;
        }
        
        return ans;
    }
};