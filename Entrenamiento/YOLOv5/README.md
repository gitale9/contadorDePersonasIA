# Entrenamiento con YOLOv5
A partir del repositorio de [YOLOv5](https://github.com/ultralytics/yolov5.git) y de enláces a tutoriales presentes en dicho repositorio, se crea [un cuaderno de colab](https://github.com/gitale9/contadorDePersonasIA/blob/66f660311565c2c8b65388fc947d1edfa4f76dc3/Entrenamiento/YOLOv5/EntrenamientoConYOLOv5.ipynb) para un entrenamiento personalizdo, a partir de un dataset propio.

EL dataset propio de este repositorio está ubicado en este [link](https://drive.google.com/drive/folders/1NggL7AcNG1_GGHBRocVCamX7GQkFuHfu?usp=sharing) y tanto su estructura como parte de su elaboración se muestran abajo
  <details close>
  <summary>Estructura y algo más del dataset</summary>
     
  <div align="center">
    <img src="https://github.com/gitale9/contadorDePersonasIA/blob/66f660311565c2c8b65388fc947d1edfa4f76dc3/base.png" width="40%" alt="" /></a>
  </div>
  Este dataset consta de imágenes y de las anotaciones de dónde están las personas en cada una de las imágenes, para hacer dichas anotaciones se puede hacer uso de la herramienta MAKESENSE->https://www.makesense.ai, el siguiente gif ejemplifica estre proceso de crear las etiquetas

<div align="center">
  <img src="./TutoAnotaciones.gif" width="50%" alt="" /></a>
</div>
  
  </details>

Para el correcto funcionamiento del algoritmo del cuaderno de colab se deben cargar a este tanto el dataset como el archivo gía de este ([custom](https://github.com/gitale9/contadorDePersonasIA/blob/66f660311565c2c8b65388fc947d1edfa4f76dc3/Entrenamiento/YOLOv5/custom.yaml)) la ruta donde se debe cargar este se especifíca en el cuaderno.

