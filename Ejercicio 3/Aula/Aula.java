public class Aula {

    private String nombreAula;
    private int piso;
    private String[] estudiantes;
    private int[] notas;

    // Constructor
    public Aula(String nombreAula, int piso){
        this.nombreAula = nombreAula;
        this.piso = piso;

        estudiantes = new String[]{"Luis","Aracely"};
        notas = new int[]{67,89};
    }

    public void mostrar(){
        System.out.println("Aula: " + nombreAula);
        System.out.println("Piso: " + piso);

        for(int i=0; i<estudiantes.length; i++){
            System.out.println(estudiantes[i] + " Nota: " + notas[i]);
        }
    }

    public void mostrar(int opcion){

        for(int i=0; i<estudiantes.length; i++){

            if(notas[i] >= 51){
                System.out.println(estudiantes[i] + " APROBADO");
            }else{
                System.out.println(estudiantes[i] + " REPROBADO");
            }
        }
    }

    @Override
    public String toString(){
        return "nombre=" + nombreAula + ", piso:" + piso;
    }
    public static void main(String[] args) {

        Aula aula1 = new Aula("computacion",2);
        aula1.mostrar();

        System.out.println();
        aula1.mostrar(1);

    }
}