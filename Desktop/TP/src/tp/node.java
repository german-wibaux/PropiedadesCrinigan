/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tp;

import java.util.Vector;

/**
 *
 * @author Yerman
 */
public class node {
    private int dni;
    private String [] likes = new String[SIZELIK];
    private node next;
    
    public static final int SIZELIK=5;
    
    public node (){
        dni = 0;       
        next = null;       
    }
    
    public void setDni (int d){
        dni = d;
    }
    
    public void setLike (String l){
        int c = 0;        
        while (likes[c] != null){            
            c++;
        }
        if (c < SIZELIK){
            likes[c]=l;
        }
    }
    
    public void setNext (node a){
        this.next = a;
    }
    
    public int getDni (){
        return this.dni;
    }
    
    public String [] getLikes (){
        return this.likes;
    }
    
    public node getNext(){
        return this.next;
    }
}
