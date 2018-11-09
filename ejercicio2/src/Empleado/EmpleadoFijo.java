/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Empleado;

/**
 *
 * @author Carlos Juca
 */
public class EmpleadoFijo extends Empleado {                                            // Creamos la Clase EmpleadoFijo que es un Enpleado

    double sueldoFijo, descuentoSeguro;                                                 // Atributos de la Clase

    public EmpleadoFijo() {                                                             // Constructor de la clase                                                       
        this.agregarSueldoFijo(0.0);
        this.agregarDescuentoSeguro(0.0);
    }

    public void agregarSueldoFijo(double sueldo) {                                      // Funciones para agregar y devolver los atributos de la clase
        this.sueldoFijo = sueldo;
    }

    public void agregarDescuentoSeguro(double descuento) {
        this.descuentoSeguro = descuento;
    }

    public Double obtenerSueldoFijo() {
        return this.sueldoFijo;
    }

    public Double obtenerDescuentoSeguro() {
        return this.descuentoSeguro;
    }

    public Double calcularSueldoFinal() {                                               // Calculo del sueldo Final
        double valor = this.obtenerSueldoFijo() * (100 - this.obtenerDescuentoSeguro());
        valor += super.obtenerComisionFija();
        return valor;
    }

    @Override                                                                           
    public String toString() {
        return String.format("%s\nEmpleado Fijo\nSueldo fijo: %.2f\nDescuento seguro: %.2f\nSueldo final: %.2f\n",
                super.toString(), this.obtenerSueldoFijo(), this.obtenerDescuentoSeguro(), this.calcularSueldoFinal());
    }
}
