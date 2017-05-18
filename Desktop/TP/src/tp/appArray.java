/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author Yerman
 */
public class appArray {    
    private node [] users = new node[SIZEARRAY];
    
    public static int SIZEARRAY = 10000;
    public static final String SEPARATOR=";";
    
    public appArray (){
        int s = 0;
        while (s < SIZEARRAY){
            users[s] = null;
            s++;
        }
    }
    
    public void addUser(node ins){
        int c = 0;
        boolean v = false;
        while ((!v) && (c < SIZEARRAY)){            
            if (users[c]!=null){               
                c++;
            } else {
                v = true;
            }
            
        }        
        if (users[SIZEARRAY-1] != null){            
            this.toExtend();
            this.addUser(ins);
        } else {            
            users[c] = ins;
        }
    }
    
    public void readCSV(String ruta) throws IOException {      
      BufferedReader br = null;      
      try {         
         FileReader u = new FileReader (ruta);
         br = new BufferedReader(u);
         br.readLine();
         String line = br.readLine();
         while (null!=line) {
            String [] fields = line.split(SEPARATOR);
            node b = new node();
            int d = Integer.parseInt(fields[0]);
            b.setDni(d);
            for (int i=1;i<fields.length;i++){
                b.setLike(fields[i]);
            }
            this.addUser(b);
            line = br.readLine();          
         }         
      } catch (IOException e) {
         
      } finally {
         if (null!=br) {
            br.close();
         }
      }         
    }
    
    public void insCSV (String ruta) throws IOException{
        long TInicio, TFin, tiempo; //Variables para determinar el tiempo de ejecución
        TInicio = System.currentTimeMillis(); 
        BufferedReader br = null;      
      try {         
         FileReader u = new FileReader (ruta);
         br = new BufferedReader(u);         
         String line = br.readLine();
         while (null!=line) {
            String [] fields = line.split(SEPARATOR);
            node b = new node();
            int d = Integer.parseInt(fields[0]);
            b.setDni(d);
            for (int i=1;i<fields.length;i++){
                b.setLike(fields[i]);
            }
            this.addUser(b);
            line = br.readLine();          
         }         
      } catch (IOException e) {
         
      } finally {
         if (null!=br) {
            br.close();
         }
      }
     TFin = System.currentTimeMillis(); //Tomamos la hora en que finalizó el algoritmo
     tiempo = TFin - TInicio; //Calculamos los milisegundos de diferencia
     File k = new File("/Users/app/salidaAlta.csv");
     FileWriter n1 = new FileWriter(k); 
     BufferedWriter br1 = new BufferedWriter(n1);
     br1.write("Operacion"+";"+"Tiempo(ms)");
     br1.newLine();
     String strLong = Long.toString(tiempo); 
     br1.write("Alta"+";"+strLong);
     br1.flush();
    }
    
    public void searchCSV (String ruta) throws IOException{
         
        BufferedReader br = null;       
      try {         
         File k = new File("/Users/app/salidaBusqueda.csv");
         FileWriter n1 = new FileWriter(k);          
         BufferedWriter br1 = new BufferedWriter(n1);         
         br1.write("Resultado busqueda"+";"+"Tiempo(ms)");
         br1.newLine();
         FileReader u = new FileReader (ruta);
         br = new BufferedReader(u);         
         String line = br.readLine();
         while (null!=line) {
            String [] fields = line.split(SEPARATOR);
            int d = Integer.parseInt(fields[0]);
            long TInicio = System.currentTimeMillis();            
            boolean s = search(d);
            long TFin = System.currentTimeMillis(); //Tomamos la hora en que finalizó el algoritmo                   
            long t;
            t = TFin - TInicio;            
            br1.write(String.valueOf(s)+";"+t);
            br1.newLine();
            line = br.readLine();          
         }
         br1.flush();
      } catch (IOException e) {
         
      } finally {
         if (null!=br) {
            br.close();            
         }
      }    
    }
    
    public void toExtend (){
        int j = users.length*2;
        node [] aux = new node[j];        
        for(int i=0;i<users.length;i++){
            aux[i] = users[i];
        }
        this.users = aux;
        SIZEARRAY = users.length;
        System.out.println("Se extendio a"+" "+SIZEARRAY+" "+"usuarios");
    }
    
    public boolean search (int dni){
        int i=0;
        boolean s = false;       
        while ((!s) && (i < SIZEARRAY)){            
            if (users[i] != null){
                if (users[i].getDni() == dni){
                    s = true;
                }
                i++;
            } else {
                i = SIZEARRAY;                
            }
        }       
        return s;
    }
    
    public node retPos(int n){
        node aux = null;
        if (n < SIZEARRAY){
            aux = users[n];
        }
        return aux;
    }
    
}
