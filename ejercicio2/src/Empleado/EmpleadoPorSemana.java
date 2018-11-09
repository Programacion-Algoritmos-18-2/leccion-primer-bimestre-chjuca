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
public class EmpleadoPorSemana extends Empleado {                                   // Creamos la Clase EmpleadoPorSemana que es un Empleado

    int numeroSemanas = 0;                                                          // Atributos de la clase Empleado por Semana
    double valorSemanal = 0.0;

    public EmpleadoPorSemana() {                                                   // Constructores de la clase    
        agregarNumeroSemanas(0);                                                     
        agregarValorSemanal(0.0);
    }

    public void agregarNumeroSemanas(int semanas) {                                 // Funciones para obtener y devolver los valores de los atributos de la clase
        this.numeroSemanas = semanas;
    }

    public int obtenerNumeroSemanas() {
        return this.numeroSemanas;
    }

    public void agregarValorSemanal(double valor) {
        this.valorSemanal = valor;
    }

    public double obtenerValorSemanal() {
        return this.valorSemanal;
    }
        
    public double calcularSueldoFinal() {                                           // Calculamos el sueldo Final
        double sueldoFinal;
        sueldoFinal = obtenerNumeroSemanas() * obtenerValorSemanal() + super.obtenerComisionFija();
        return sueldoFinal;
    }

    @Override                                                                       // Presentamos Datos
    public String toString() {
        return String.format("%s\nNumero Semanas: %d\nValor semanal: %.2f\nSueldo final: %.2f\n", super.toString(), this.obtenerNumeroSemanas(), this.obtenerValorSemanal(), this.calcularSueldoFinal());
    }
}
