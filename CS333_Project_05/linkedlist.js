/*
Jordan Smith
linkedlist.js
10/25/23
Linked List
*/

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // Creates a new LinkedList and returns it
    static ll_create() {
        return new LinkedList();
    }

    // Adds a node to the front of the list, storing the given data in the node
    ll_push(data) {
        const newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
    }

    // Removes the node at the front of the list and returns the associated data
    ll_pop() {
        if (!this.head) {
            return null;
        }
        const data = this.head.data;
        this.head = this.head.next;
        this.size--;
        return data;
    }

    // Adds a node to the end of the list, storing the given data in the node
    ll_append(data) {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
        this.size++;
    }

    // Removes the first node in the list whose data matches the target using the comparison function
    // Returns the pointer to the data in the removed node
    ll_remove(target, compfunc) {
        if (!this.head) {
            return null;
        }
        if (compfunc(target, this.head.data)) {
            const data = this.head.data;
            this.head = this.head.next;
            this.size--;
            return data;
        }

        let current = this.head;
        while (current.next) {
            if (compfunc(target, current.next.data)) {
                const data = current.next.data;
                current.next = current.next.next;
                this.size--;
                return data;
            }
            current = current.next;
        }

        return null;
    }

    // Returns the size of the list
    ll_size() {
        return this.size;
    }

    // Removes all of the nodes from the list, freeing the associated data using the given function
    ll_clear(freefunc) {
        let current = this.head;
        while (current) {
            const nextNode = current.next;
            if (freefunc) {
                freefunc(current.data);
            }
            current = nextNode;
        }
        this.head = null;
        this.size = 0;
    }

    // Traverses the list and applies the given function to the data at each node
    ll_map(mapfunc) {
        let current = this.head;
        while (current) {
            if(mapfunc(current.data) != null)
            {
                current.data = mapfunc(current.data); // Update the data
            }
            current = current.next;
        }
    }    
}

module.exports = {LinkedList};