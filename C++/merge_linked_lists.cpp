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

class CleanerSolution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return divide(lists, 0, lists.size() - 1);
    }
    
    ListNode* divide(vector<ListNode*>& lists, int start, int end) {
        if (lists.size() == 0) {
            return NULL;
        }
        
        ListNode *list_0, *list_1;
        
        if (end - start == 1) {
            list_0 = lists[start];
            list_1 = lists[end];
            return conquer(list_0, list_1);
        } else if (end - start == 0) {
            return lists[start];
        } else {
            int half = (end - start) / 2;
            list_0 = divide(lists, start, start + half);
            list_1 = divide(lists, start + half + 1, end);
            return conquer(list_0, list_1);
        }
        
        return NULL;
    }
    
    ListNode* conquer(ListNode* left, ListNode* right) {
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
        
        if (left != NULL) {
            prev->next = left;
        } else if (right != NULL) {
            prev->next = right;
        }
                
        return ans->next;
    }
};