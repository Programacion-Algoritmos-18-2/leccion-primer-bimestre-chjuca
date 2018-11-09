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
public class EmpleadoPorHoras extends Empleado {                                        // Se crea la clase EmpleadoPorHoras que es un Empleado

    int numeroHoras = 0;                                                                // Atributos de la clase
    double valorHoras = 0.0;

    public EmpleadoPorHoras() {      // Costructores de EmpleadoPorHoras
        agregarNumeroHoras(0);
        agregarValorHoras(0.0);
    }

    public void agregarNumeroHoras(int horas) {                                              // Funciones para agregar y devolver los atributos de la clase
        this.numeroHoras = horas;
    }

    public int obtenerNumeroHoras() {
        return this.numeroHoras;
    }

    public void agregarValorHoras(double valor) {
        this.valorHoras = valor;
    }

    public double obtenerValorHoras() {
        return this.valorHoras;
    }

    public double calcularSueldoFinal() {                                                       // Calcula Sueldo Final
        double valor = this.obtenerNumeroHoras() * this.obtenerValorHoras();
        valor += super.obtenerComisionFija();
        return valor;
    }

    @Override
    public String toString() {
        return String.format("%s\nEmpleado Por Horas\nNumero horas: %d\nValor hora: %.2f\nSueldo final: %.2f\n", super.toString(), this.obtenerNumeroHoras(), this.obtenerValorHoras(), this.calcularSueldoFinal());
    }

}
