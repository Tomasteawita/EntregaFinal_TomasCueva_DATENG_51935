# 51940-CuevaTomas

construir la imagen
```bash
docker build -t jupyter-env .
```
Ejecutar el contenedor
```bash
docker run -p 8888:8888 -v <ruta_absoluta_al_directorio_local>:/home/jovyan/work jupyter-env
```

```bash:copy
#en mi caso 
docker run -p 8888:8888 -v "C:\\Users\tomas\OneDrive\Escritorio\DataEngineer\ProyectoFinalCoderhouse:/home/jovyan/work" jupyter-env
```