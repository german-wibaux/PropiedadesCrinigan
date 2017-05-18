/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tp;

import java.io.File;
import java.io.IOException;
import javax.swing.JFileChooser;

/**
 *
 * @author Yerman
 */
public class TP {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {       
        
        /*Selecciono archivo de precarga*/
        JFileChooser explorador = new JFileChooser(); 
        int seleccion = explorador.showDialog(null, "Seleccionar archivo a cargar");
        File archivo = explorador.getSelectedFile();
        String rutaPrecarga = archivo.getPath();       
        
        /*Cargo app con arreglo*/
        appArray appA = new appArray();
        appA.readCSV(rutaPrecarga);       
        String ruta1 = "/Users/Yerman/Desktop/datasets/dataset_insert_10000.csv";       
        appA.insCSV(ruta1);       
        String ruta2 = "/Users/Yerman/Desktop/datasets/dataset_busqueda_10000.csv";       
        appA.searchCSV(ruta2);
        
        
        /*Cargo app con una lista simple*/
        appArrayList apList = new appArrayList();        
        apList.readCSV(rutaPrecarga);        
        String ruta3 = "/Users/Yerman/Desktop/datasets/dataset_insert_10000.csv";       
        apList.insCSV(ruta3);        
        String ruta4 = "/Users/Yerman/Desktop/datasets/dataset_busqueda_10000.csv";       
        apList.searchCSV(ruta4);
        
        
        /*Cargo app con lista que añade elementos al principio*/
        appListBeg appLisBeg = new appListBeg();
        appLisBeg.readCSV(rutaPrecarga);        
        String ruta5 = "/Users/Yerman/Desktop/datasets/dataset_insert_10000.csv";       
        appLisBeg.insCSV(ruta5);       
        String ruta6 = "/Users/Yerman/Desktop/datasets/dataset_busqueda_10000.csv";       
        appLisBeg.searchCSV(ruta6);        
    }
    
}
