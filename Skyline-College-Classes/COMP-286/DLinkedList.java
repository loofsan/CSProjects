// Lynn T. Aung
// 10-17-2023
// Doubly Linked List
import java.util.AbstractList;

public class DLinkedList<E> extends AbstractList<E>{

	private DNode<E> head;
	private DNode<E> tail;
	private int size;

	public DLinkedList(){
		head = new DNode<E>();
		tail = head;
		size = 0;
	}
    
    private boolean isValidIndex(int i){
		return i >= 0 && i < size;
	}
    
    /* Helper Method, a method for traversing the doubly linked list */
    public DNode<E> getNode(int index) {
        if (!isValidIndex(index))
            throw new IndexOutOfBoundsException();  
             
        DNode<E> current = head;
        for (int i=0; i<(index-1); i++) {
            current = current.next;
        }
        
        return current;
    }

	/* appends element to end of the list */
	public boolean add(E e){
		if (size == 0) 
        {
            head = new DNode<>(e);
            tail = head;
            size++;
            return true;
        }
        
        DNode<E> node = new DNode<>(e);
        DNode<E> current = head;
        while (current.next != null) { //loop the nodes
            current = current.next;
        }
        // Make sure tail node can direct back
        current.prev = tail;
        tail.next = node; 
        tail = node;
        size++;
        return true;
	}

	/* insert element at the given index 
	if the index is out of bounds throw an IndexOutOfBoundsException */
	public void add(int index, E e){
		if (index == 0) {
            DNode<E> node = new DNode<>(e);
            head.prev = node.next; // The original head links back to the new node
            node.next = head.prev; // The new node links to the original head
            head = node; // The new node becomes the head
            size++;   
        }
        
        else if (index == size) {
            add(e);
        }
        
        else {
            DNode<E> newNode = new DNode<>(e);
            DNode<E> next = getNode(index);
            DNode<E> prev = getNode(index - 1);
            // Assign the prev of the next node to the new node
            // and link back
            next.prev = newNode;
            newNode.next = next.prev;
            // Assign the next of the prev node to the new node
            // and link back
            prev.next = newNode;
            newNode.prev = prev.next;
            size++;
        }

	}

	public void clear(){
		head.next = null;
		tail = head;
		size = 0;
	}

	/* get the data from the node at the given index 
		if the index does not exist throw an IndexOutOfBoundsException */
	public E get(int index){
		DNode<E> current = getNode(index);
        return current.data;
	}

	/* remove the node at the given index from the list and return its data 
		if the index does not exist throw an IndexOutOfBoundsException */
	public E remove(int index){
		if (size==0)
            throw new IndexOutOfBoundsException();
        if (index == 0)
        {
            E content = head.data;
            //The new head node will be pointing to nothing;
            head.next.prev = null;
            head = head.next; // replace head
            size--;
            return content;
        }
        DNode<E> prev = getNode(index - 1);
        E content = prev.next.data;
        // The next node of the previous, which is current node,
        // will point to the previous pointer of the next node.
        prev.next.next.prev = prev;
        // The next pointer of the previous node will point to
        // the next node of the current node.
        prev.next = prev.next.next;
        size--;
        return content;
	}

	/* replace the contents at the given index with the data given
		return the data that was previously at that index 
		if the index does not exist throw an IndexOutOfBoundsException */
	public E set(int index, E element){
		if (size == 0)
            throw new IndexOutOfBoundsException();
        DNode<E> current = getNode(index);
        E content = current.data;
        current.data = element;
		return content;
	}

	public int size(){
		return size;
	}

	public String toString(){
		String list = "{";
        int i = 0;
        DNode<E> current = head;
        while (current.next != null)
        {
            list += current.data.toString() + ",";
            current = current.next;
            i++;
        }
		return list + "}";
	}

	// internal class for single linking nodes
	class DNode<E> {
		E data;
		DNode<E> next;
		DNode<E> prev;

		public DNode(){
			this(null);
		}

		public DNode(E data){
			this.data = data;
			next = null;
			prev = null;
		}

		public DNode(E data, DNode<E> prev, DNode<E> next){
			this.data = data;
			this.prev = prev;
			this.next = next;
		}
	}
	
}