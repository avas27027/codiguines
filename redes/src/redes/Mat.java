/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package redes;

import java.util.Scanner;

/**
 *
 * @author ASUS
 */
public class Mat {

    Scanner sc = new Scanner(System.in);
    private int mat[][];
    private String out[][];
    private int tam;

    public Mat() {
        System.out.println("Ingrese numero de routers:");
        int tam = sc.nextInt();
        this.tam = tam;
        this.mat = new int[tam][tam];
        this.out = new String[tam][tam];
        for (int i = 0; i < tam; i++) {
            for (int j = 0; j < tam; j++) {
                out[i][j] = "/R";
                mat[i][j] = -1;
            }
        }
    }

    public void ady() {
        
        String a=sc.nextLine();
        int num;
        int cont = 0;
        for (int i = 0; i < tam; i++) {
            System.out.println("routers adyacentes al router " + i);

            a = sc.nextLine();
            while (!a.equals("") && cont < tam) {
                num = Integer.parseInt(a);
                while (num > tam || num < 0) {
                    num = sc.nextInt();
                }
                mat[i][i] = 0;
                mat[i][num] = 1;
                out[i][i] = "/";
                out[i][num] = "/R"+i;
                
                cont++;
                a = sc.nextLine();
            }
            cont = 0;
        }
    }

    public void completar() {
        int metr, sal;
        for (int i = 0; i < tam; i++) {
            for (int j = 0; j < tam; j++) {
                if (mat[i][j] == -1) {
                    metr = buscar(i, j, 0);
                    sal = salida(i,j,0, 0);
                    out[i][j] = out[i][j]+sal;
                    mat[i][j] = metr;
                }
            }
        }
    }

    public int buscar(int a1, int a2, int cont) {
        if (cont < 16) {
            for (int i = 0; i < tam; i++) {
                if (mat[i][a1] == 1 && mat[i][a2] == 1) {
                    return cont + 2;
                }
            }
            for (int i = 0; i < tam; i++) {
                if (mat[i][a2] == 1) {
                    cont++;
                    buscar(a1, i, cont);
                }

            }
        } else {
            return -1;
        }
        return cont + 2;
    }
    
    public int salida(int a1, int a2, int cont, int sal) {
        if (cont < 16) {
            for (int i = 0; i < tam; i++) {
                if (mat[i][a1] == 1 && mat[i][a2] == 1) {
                    if (cont == 0){
                        sal = i;
                    }
                    return sal;
                }
            }
            for (int j = 0; j < tam; j++) {
                if (mat[j][a2] == 1) {
                    if (cont == 0){
                        sal = j;
                    }
                    cont++;
                    buscar(a1, j, cont);
                }

            }
        } else {
            sal=-1;
        }
        return sal;
    }

    public void imp() {
        
        String a = "\t\t\t";
        for (int i = 0; i < tam; i++) {
            a+=i+"\t";
        }
        
        
        System.out.println("Rutas de los routers (metrica/sig. salto)");
        for (int i = 0; i < tam; i++) {
            System.out.print(a+"\ndesde el router "+i+"\t");
            for (int j = 0; j < tam; j++) {
                System.out.print(mat[j][i] + out[j][i]+ "\t");;
            }
            System.out.println("\n\n");
        }
    }
}
