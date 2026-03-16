import java.util.Scanner;

public class Videojuego {

    public String nombre;
    public String plataforma;
    public int cantidadJugadores;

    public Videojuego(String nombre, String plataforma){
        this.nombre=nombre;
        this.plataforma=plataforma;
        this.cantidadJugadores= 0 ;
    }

    public Videojuego(String nombre, String plataforma, int cantidadJugadores){
        this.nombre=nombre;
        this.plataforma=plataforma;
        this.cantidadJugadores=cantidadJugadores;
    }

    public void agregarJug(){
        cantidadJugadores = cantidadJugadores + 1;
    }

    public void agregarJugs(int cantidad){
        cantidadJugadores= cantidadJugadores + cantidad;
    }

    @Override
    public String toString(){
        return "nombre=" + nombre + ", plataforma=" + plataforma + ", jugadores=" + cantidadJugadores ;
    }
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        Videojuego  juego1= new Videojuego("DOTA", "PlayStation", 2);
        Videojuego  juego2 = new Videojuego("ROBLOX", "celular", 5);

        juego1.agregarJugs(1);

        System.out.println("Ingrese jugadores:");
        int cantidad = teclado.nextInt();


        juego2.agregarJugs(cantidad);

        System.out.println(juego1); 
        System.out.println(juego2);

    
    
}
}
