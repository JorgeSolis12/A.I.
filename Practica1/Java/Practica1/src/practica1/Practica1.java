/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

/**
 *
 * @author pumas
 */
public class Practica1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        File archivo = null;
      FileReader fr = null;
      BufferedReader br = null;

      try {
         // Apertura del fichero y creacion de BufferedReader para poder
         // hacer una lectura comoda (disponer del metodo readLine()).
         archivo = new File ("C:\\Users\\pumas\\Documents\\NetBeansProjects\\Practica1\\src\\practica1\\file\\matriz.txt");
         fr = new FileReader (archivo);
         br = new BufferedReader(fr);

         // Lectura del fichero
         ArrayList laberinto = new ArrayList();
         ArrayList fila = new ArrayList();
         String linea;
         while((linea=br.readLine())!=null){
            System.out.println(linea);
                String[] values = linea.split(",");
            for( int i = 0; i < values.length; i++ ){
                fila.add(Integer.parseInt(values[i]));
            }
            laberinto.add(fila.clone());
            fila.clear();
         }
         
         System.out.println(laberinto);
         System.out.println("\n\n");
         
         for (int i = 0; i < laberinto.size(); i++){
             fila.add(laberinto.get(i));
             for(int j = 0; j< fila.size() ; j++){
                 System.out.print(fila.get(j));
             }
             fila.clear();
         }
         
         System.out.println("\n\n");
        
      }
      catch(Exception e){
         e.printStackTrace();
      }finally{
         // En el finally cerramos el fichero, para asegurarnos
         // que se cierra tanto si todo va bien como si salta 
         // una excepcion.
         try{                    
            if( null != fr ){   
               fr.close();     
            }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
      }
   }    
}
