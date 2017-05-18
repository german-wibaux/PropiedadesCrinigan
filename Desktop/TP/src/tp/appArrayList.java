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
import java.util.ArrayList;
import static tp.appArray.SEPARATOR;

/**
 *
 * @author Yerman
 */
public class appArrayList {
    private ArrayList<node> users = new ArrayList<node>();   
    
    public void readCSV(String ruta) throws IOException{      
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
            users.add(b);
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
            users.add(b);
            line = br.readLine();          
         }         
      } catch (IOException e) {
         
      } finally {
         if (null!=br) {
            br.close();
         }
      }
     TFin = System.currentTimeMillis(); //Tomamos la hora en que finalizó el algoritmo y la almacenamos en la variable T
     tiempo = TFin - TInicio; //Calculamos los milisegundos de diferencia
     File k = new File("/Users/appList/salidaAlta.csv");
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
         File k = new File("/Users/appList/salidaBusqueda.csv");
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
            boolean s = this.search(d);            
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
    
    public boolean search (int dni){
        int i=0;
        boolean s = false;       
        while ((!s) && (i < users.size())){            
            if (users.get(i) != null){
                if (users.get(i).getDni() == dni){
                    s = true;
                }
                i++;
            } else {
                i = users.size();                
            }
        }       
        return s;
    }
    
}
