struct PriorityQueue<Element> {
    var elements: [Element]
    let priority : (Element, Element) -> Bool
    
    var count : Int {
        return elements.count;
    }
    
    init(elements: [Element] = [], priority: @escaping (Element, Element) -> Bool) {
        self.elements = elements
        self.priority = priority
        build()
    }
    
    mutating func build() {
        for i in (0 ..< count / 2).reversed() {
            sift_down(i)
        }
    }
    
    mutating func dequeue() -> Element? {
        if (is_empty() == true) {
            return nil // Cannot dequeue an empty queue
        }
        
        swap(0, count - 1);
        let elem = elements.removeLast()
        
        if (is_empty() == false) {
            sift_down(0)
        }
        
        return elem
    }
    
    mutating func enqueue(element: Element) {
        elements.append(element);
        sift_up(count - 1);
    }
    
    mutating func sift_down(_ index: Int) {
        let child = highest_priority_index(parent: index)
        
        if child == index {
            return
        }
        
        swap(index, child)
        sift_down(child)
    }
    
    mutating func sift_up(_ index: Int) {
        let parent = self.parent(of: index)
        if (is_root(index) == true) {
            return
        }
        
        if (is_higher_priority(index, than: parent)) {
            swap(index, parent);
            sift_up(parent);
        }
    }
    
    mutating func swap(_ first: Int, _ second: Int) {
        elements.swapAt(first, second);
    }
    
    func highest_priority_index(parent: Int) -> Int {
        return highest_priority_index(parent: highest_priority_index(parent: parent, child: left_child(of: parent)), child: right_child(of: parent));
    }
    
    func highest_priority_index(parent: Int, child: Int) -> Int {
        guard child < count && is_higher_priority(child, than: parent) else {
            return parent;
        }
        
        return child;
    }
    
    func left_child(of index: Int) -> Int {
        return (2 * index) + 1;
    }
    
    func is_empty() -> Bool {
        return elements.isEmpty;
    }
    
    func is_higher_priority(_ first_index: Int, than second_index: Int) -> Bool {
        return priority(elements[first_index], elements[second_index]);
    }
    
    func is_root(_ index: Int) -> Bool {
        return index == 0;
    }
    
    func parent(of index: Int) -> Int {
        return (index - 1) / 2;
    }
    
    func peak() -> Element? {
        return elements.first;
    }
    
    func right_child(of index: Int) -> Int {
        return (index * 2) + 2;
    }
}

var pq = PriorityQueue(elements: [4,5,6,3,8], priority: >)

