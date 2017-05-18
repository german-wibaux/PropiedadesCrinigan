/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tp;

/**
 *
 * @author Yerman
 */
public class listBeg {
    node root;
    
    public listBeg(){
        root = null;
    }
    
    
    public void add (node a){
        a.setNext(this.root);
        this.root = a;
    }
    
    public int size (){
        int c = 0;
        node aux = root;
        while (aux != null){
            c++;
            aux = aux.getNext();
        }
        return c;
    }
    
    public node returnPos(int pos){
        int c = 0;
        node aux = this.root;
            if (pos<this.size()){            
                while (c < pos){
                    aux = aux.getNext();
                    c++;
                }
            }
        return aux;
    }
    
    public boolean search (int dni){
        node aux = root;
        boolean s = false;        
        while ((!s) && (aux != null)){            
            if (aux.getDni() == dni){
                    s = true;                                
            } else {
                aux = aux.getNext();
            }               
        }
        return s;        
    }
    
}
