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
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* left = lists[0];
        ListNode* right = lists[1];
        ListNode* prev = new ListNode();
        ListNode* ans = prev;
        
        while (left != NULL && right != NULL) {
            if (left->val <= right->val) {
                ListNode *next = new ListNode(left->val);  
                prev->next = next;
                left = left->next;
            } else {  
                ListNode *next = new ListNode(right->val);
                prev->next = next;
                right = right->next;
            }
            
            prev = prev->next;
        }
        
        while (left != NULL) {
            prev->next = left;
            left = left->next;
        }
        
        while (right != NULL) {
            prev->next = right;
            right = right->next;
        }
        
        return ans->next;
    }
};