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
public class Empleado {                                           // Creamos la clase empleado

    String nombre, apellido;
    int cedula;
    double comision_fija;

    public Empleado() {                                                // Atributos de la Clase Empleado
        agregarApellido("");
        agregarCedula(0);
        agregarComisionFija(0.0);
        agregarNombre("");
    }

    public void agregarComisionFija(double comision) {               // Metodos que agregan y devuelven los valores de los atributos de la clase
        this.comision_fija = comision;
    }

    public double obtenerComisionFija() {
        return this.comision_fija;
    }

    public void agregarNombre(String nombre) {
        this.nombre = nombre;
    }

    public String obtenerNombre() {
        return this.nombre;
    }

    public void agregarApellido(String apellido) {
        this.apellido = apellido;
    }

    public String obtenerApellido() {
        return this.apellido;
    }

    public void agregarCedula(int cedula) {
        this.cedula = cedula;
    }

    public int obtenerCedula() {
        return this.cedula;
    }

    @Override                                                            // Presentamos Datos
    public String toString() {
        return String.format("\nInformacion de %s %s\n\tCEDULA: %s\n", this.obtenerNombre(), this.apellido, this.obtenerCedula());
    }
}
