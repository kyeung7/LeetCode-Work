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
        
        ListNode* l3 = new ListNode(); // not pointer so must use .val .next
        
        while ((l1 != NULL) && (l2 != NULL)) {
            cout << "List 1: " << l1->val << endl;  
            cout << "List 2: " << l2->val << endl;  

            if (l2->val <= l1->val) {                
                if (l3->val == NULL) {
                    cout << "initializing l3, is null" << endl;
                    l3 = l2;
                } else {
                    l3->next = l2; // adds to l3 head (single ll so cannot move)
                    cout << "adding: " << l2->val << " to end of l3" << endl;
                }

                l2 = l2->next;
                // l3->val = l1->val; // update l3 val
            } else {
                //ListNode* tempNode = new ListNode();
                //tempNode->val = l1->val; //l1 val is greater than l2 val
                //tempNode->next = l2; // append l2 list to end of tempNode
                //l3->next = tempNode; // update l3

                if (l3->val == NULL) {
                    cout << "initializing l3, is null" << endl;
                    l3 = l1;
                } else {
                    l3->next = l1; // adds to l3 head (single ll so cannot move)
                    cout << "adding: " << l1->val << " to end of l3" << endl;
                }
                
                l1 = l1->next;
            }
                        
        }
        
       /*
        while (l3 != NULL){
            cout << "List 3: " << l3->val << endl; 
            l3 = l3->next;
        }
        */
        
        return l3;
    }
    
};
