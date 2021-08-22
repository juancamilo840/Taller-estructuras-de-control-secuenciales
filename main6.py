int main (){
    int A,B,C,D;
    
    printf("Ingrese el valor de los 4 digitos: ");
    scanf("%d %d %d %d",&A,&B,&C,&D);
    
    if( B>=9 && C>=5){
        A++;
        B=0;
        C=0;
        D=0;
    }
    else if(B>=9 && C<5){
    B= B;
    C=0;
    D=0;
    }   
    else if(B<9 && C>=5){
        B++;
        C=0;
        D=0;
    }
    else{
        C=0,
        D=0;
    }
    
 
    
    printf("La centenas mas proxima es: %d %d %d %d\n",A,B,C,D);
    
    system("pause");
    return 0;
}