class ListNode:
    prev:Optional[ListNode]
    val: str
    nxt: Optional[ListNode]

    def __init__(
        self,
        val: str, 
        prev: Optional[ListNode], 
        nxt: Optional[ListNode]
    ):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class BrowserHistory:
    head: Optional[ListNode]
    tail: Optional[ListNode]
    cur: Optional[ListNode]

    def __init__(self, homepage: str):
        new_homepage = ListNode(homepage, None, None)
        self.head = new_homepage
        self.tail = new_homepage
        self.cur = new_homepage

    def visit(self, url: str) -> None:
        #adiciona linkedin
        new_page = ListNode(
            url,
            self.cur,
            None
        )
        # se estou em facebook e adiciono linkedin, o proximo de facebook deve se tornar linkedin
        self.cur.nxt = new_page

        self.tail = new_page
        self.cur = new_page

        

    def back(self, steps: int) -> str:
        count = 0
        cur = self.cur
        print("steps", steps)
        while cur is not None:
            print("cur,val", cur.val)
            if steps == count or cur.prev is None:
                self.cur = cur
                return cur.val

            cur = cur.prev
            count += 1

        self.cur = cur
        return cur.val
        
    def forward(self, steps: int) -> str:
        cur = self.cur
        count = 0
        print("steps", steps)

        while cur is not None:
            if count == steps or cur.nxt is None:
                self.cur = cur
                return cur.val

            cur = cur.nxt
            count += 1
            
        return cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)