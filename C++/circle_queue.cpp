class CircularQueue {
    int size;
    int front;
    int back;
    int *queue;
    
public:
    MyCircularQueue(int k) {
        size = k;
        front = -1;
        back = -1;
        queue = (int*)malloc(sizeof(int) * size);
    }
    
    bool enQueue(int value) {
        if (isFull() == true) {
            // Cannot add more to a full queue
            return false;
        }
        
        // If the list is completely empty
        if (isEmpty()) {
            front = 0;
        }

        back = (back + 1) % size;
        queue[back] = value;
        
        return true;
    }
    
    bool deQueue() {
        if (isEmpty() == true) {
            // Can't dequeue and empty array
            return false;
        }
        
        if (front == back) {
            front = -1;
            back = -1;
        } else {
            front = (front + 1) % size;
        }
        
        return true;
    }
    
    int Front() {
        return isEmpty() == true ? -1 : queue[front];
    }
    
    int Rear() {
        return isEmpty() == true ? -1 : queue[back];
    }
    
    bool isEmpty() {
        if (front == -1) {
            return true;
        }
        
        return false;
    }
    
    bool isFull() {
        if (front == 0 && back == size - 1) {
            return true;
        }
        
        if (front == (back + 1)) {
            return true;
        }
        
        return false;
    }
};