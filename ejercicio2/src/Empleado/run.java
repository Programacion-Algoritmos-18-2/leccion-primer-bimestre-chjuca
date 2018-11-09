/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Empleado;

import java.util.Scanner;

/**
 *
 * @author Carlos Juca
 */
public class run {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         // Instanciamos un scanner
        Scanner entrada = new Scanner(System.in);           // Objeto Scanner
       
        Empleado e = new Empleado();                        // Creamos el Objeto 		
        e.agregarNombre("Luis");			
        e.agregarApellido("Benitez");	
        e.agregarCedula(1110001);		
        System.out.println(e);		


        EmpleadoPorHoras e1 = new EmpleadoPorHoras();        //Creamos el Objeto EmpleadoPorHoras			
        System.out.printf("Ingrese su nombre: ");            // Leemos por Teclado el nombre
        String nombre = entrada.nextLine();
        e1.agregarNombre(nombre);                            // Asignamos valores a los atributos     	
        e1.agregarApellido("Andrade");              
        e1.agregarCedula(112233);			
        e1.agregarNumeroHoras(15);			
        e1.agregarValorHoras(20.2);		
        System.out.println(e1);                             // Presentamos el objeto	
        
        
        EmpleadoFijo e2 = new EmpleadoFijo();                   //  Creamos el Objeto EmpleadoFijo                                 
        e2.agregarNombre("Ana");                                // Asignamos valores a los atributos				
        e2.agregarApellido("Diaz");				
        System.out.printf("Ingrese comision: ");                // Leemos por Teclado la comision
        double comision = entrada.nextDouble();
        e2.agregarComisionFija(comision);		
        e2.agregarSueldoFijo(300.2);                            // Asignamos valores a los atributo	
        e2.agregarDescuentoSeguro(10);			
        System.out.println(e1);                                 // Presentamos el Objeto		
    }
    }

