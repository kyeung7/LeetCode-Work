// Merge two sorted linked lists and return it as a new sorted list. 
// The new list should be made by splicing together the nodes of the first two lists.

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        /*
        cout << l1->val << endl;
        l1 = l1->next;
        cout << l1->val << endl; 
        
        l1 = l1->next;
        cout << l1->val << endl;
        
        l1 = l1->next;
        cout << l1->val << endl;  
        
        
        */
     
        ListNode l3; // not pointer so must use .val .next
     //   cout << "List 3: " << l3.val << endl;  
        
        while (l1 != NULL){
            cout << "List 1: " << l1->val << endl;  
            cout << "List 2: " << l2->val << endl;  

            if (l1->val <= l2->val) {
                l3.val = l1->val;
            } else {
                l3.val = l2->val;
            }
            
            l3.next;
            
            l1 = l1->next;
            l2 = l2->next;
        
        }
       
        /* while (l3 != NULL){
            cout << "List 3: " << l3.val << endl; 
            l3 = l3->next;
        } */
        
        return 0;
    }
};
